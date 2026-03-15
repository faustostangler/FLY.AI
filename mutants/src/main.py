from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from companies.presentation.api.routes import router as companies_router
from shared.infrastructure.database.connection import engine
from companies.infrastructure.adapters.database.models import Base

import logging
import os
import time
from shared.infrastructure.config import settings
from prometheus_client import make_asgi_app
from shared.infrastructure.monitoring import metrics
from shared.infrastructure.monitoring.tracing import setup_tracing, OTelLogFilter

# Ensure the logging directory exists before initializing file handlers.
# Standard fail-fast principle during infrastructure bootstrap.
os.makedirs(settings.app.log_dir, exist_ok=True)

# Standardized Log format for observability.
# Injecting trace_id and span_id allows seamless correlation between
# logs in Loki and distributed traces in Tempo.
LOG_FORMAT = (
    "%(asctime)s [%(levelname)s] "
    "[trace_id=%(trace_id)s span_id=%(span_id)s] "
    "%(name)s: %(message)s"
)

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(f"{settings.app.log_dir}/{settings.app.log_name}"),
        logging.StreamHandler(),
    ],
)

# Apply the OTel filter to global logging logic.
otel_filter = OTelLogFilter()
for handler in logging.root.handlers:
    handler.addFilter(otel_filter)

logger = logging.getLogger(__name__)
from typing import Annotated
from typing import Callable

MutantDict = Annotated[dict[str, Callable], "Mutant"]  # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg=None):  # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os  # type: ignore

    mutant_under_test = os.environ["MUTANT_UNDER_TEST"]  # type: ignore
    if mutant_under_test == "fail":  # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException  # type: ignore

        raise MutmutProgrammaticFailException("Failed programmatically")  # type: ignore
    elif mutant_under_test == "stats":  # type: ignore
        from mutmut.__main__ import record_trampoline_hit  # type: ignore

        record_trampoline_hit(orig.__module__ + "." + orig.__name__)  # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs)  # type: ignore
        return result  # type: ignore
    prefix = orig.__module__ + "." + orig.__name__ + "__mutmut_"  # type: ignore
    if not mutant_under_test.startswith(prefix):  # type: ignore
        result = orig(*call_args, **call_kwargs)  # type: ignore
        return result  # type: ignore
    mutant_name = mutant_under_test.rpartition(".")[-1]  # type: ignore
    if self_arg is not None:  # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)  # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)  # type: ignore
    return result  # type: ignore


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manages Application Startup and Shutdown lifecycles.

    Nested Logical Steps:
        1. Database Bootstrap: Synchronize base models with pgStore.
        2. Telemetry Bootstrap: Initialize OpenTelemetry auto-instrumentation.
    """
    # Create tables automatically.
    # TODO(Issue-Arch): Transition to Alembic for production migrations.
    Base.metadata.create_all(bind=engine)

    # Bootstrap Distributed Tracing if enabled in settings.
    if settings.otel.enabled:
        setup_tracing(
            app=app,
            engine=engine,
            service_name=settings.otel.service_name,
        )
        logger.info("SRE: Distributed tracing enabled → Grafana Tempo")
    else:
        logger.info("SRE: Distributed tracing DISABLED (otel.enabled=False)")

    yield


app = FastAPI(
    title=settings.app.title,
    description=settings.app.description,
    version=settings.app.version,
    lifespan=lifespan,
)

# Mount the Prometheus exporter on the /metrics sub-path.
# Separation of concerns between domain APIs and infrastructure telemetry.
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)


@app.middleware("http")
async def prometheus_middleware(request: Request, call_next):
    """Captures 'The Four Golden Signals' for every HTTP transaction.

    This middleware ensures that throughput, latency, errors, and
    saturation are measured consistently across the entire API surface.

    Args:
        request (Request): The incoming FastAPI request.
        call_next: The next handler in the ASGI chain.
    """
    # Prevent the scraper from scraping its own scraper metrics.
    if request.url.path == "/metrics":
        return await call_next(request)

    method = request.method
    # Use the route template (e.g., /api/v1/companies/{ticker}) to avoid
    # cardinality explosion in Prometheus labels.
    path = (
        request.scope.get("route").path
        if request.scope.get("route")
        else request.url.path
    )

    # 1. SATURATION/CONCURRENCY: Track active requests.
    metrics.IN_FLIGHT_REQUESTS.labels(method=method, endpoint=path).inc()

    # 2. TRAFFIC: Inbound payload measurement.
    request_content_length = request.headers.get("content-length")
    if request_content_length:
        try:
            req_size = int(request_content_length)
            metrics.HTTP_REQUEST_SIZE.labels(method=method, endpoint=path).observe(
                req_size
            )
            metrics.NETWORK_TRANSMIT_BYTES_TOTAL.labels(
                direction="inbound", context="api"
            ).inc(req_size)
        except ValueError:
            pass

    start_time = time.perf_counter()

    try:
        response = await call_next(request)
        duration = time.perf_counter() - start_time
        status_code = str(response.status_code)

        # 3. LATENCY & THROUGHPUT: Observe performance per endpoint/status.
        metrics.HTTP_REQUEST_DURATION.labels(method=method, endpoint=path).observe(
            duration
        )
        metrics.HTTP_REQUESTS_TOTAL.labels(
            method=method, endpoint=path, status=status_code
        ).inc()

        # 4. TRAFFIC: Outbound payload measurement.
        content_length = response.headers.get("content-length")
        if content_length:
            try:
                resp_size = int(content_length)
                metrics.HTTP_RESPONSE_SIZE.labels(method=method, endpoint=path).observe(
                    resp_size
                )
                metrics.NETWORK_TRANSMIT_BYTES_TOTAL.labels(
                    direction="outbound", context="api"
                ).inc(resp_size)
            except ValueError:
                pass

        # 5. ERRORS: Track non-2xx status codes for SLI calculation.
        if response.status_code >= 400:
            metrics.HTTP_REQUESTS_FAILED_TOTAL.labels(
                method=method, endpoint=path, error_type=status_code
            ).inc()

        return response

    except Exception as e:
        # Track unhandled exceptions as critical errors (Type 500 equivalent).
        metrics.HTTP_REQUESTS_FAILED_TOTAL.labels(
            method=method, endpoint=path, error_type=type(e).__name__
        ).inc()
        raise e

    finally:
        # Decrement concurrency gauge to maintain mathematical consistency.
        metrics.IN_FLIGHT_REQUESTS.labels(method=method, endpoint=path).dec()


@app.get("/health")
def health_check():
    """Liveness probe for infrastructure health (K8s/Docker)."""
    return {"status": "ok", "message": "FLY.AI Core operational"}


# Register Domain Bounded Contexts.
# Keeps the API surface modular as we add new domains.
app.include_router(companies_router, prefix="/api/v1")

# Future Domain Modules placeholders:
# app.include_router(financials_router, prefix="/api/v1")
# app.include_router(market_data_router, prefix="/api/v1")
