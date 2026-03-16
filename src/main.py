from contextlib import asynccontextmanager

from fastapi import FastAPI
from prometheus_client import make_asgi_app

from companies.presentation.api.routes import router as companies_router
from shared.infrastructure.config import settings
from shared.infrastructure.database.connection import engine
from shared.infrastructure.monitoring.tracing import setup_tracing

from shared.infrastructure.monitoring.logging import setup_structlog
import structlog

# Bootstraps structlog (12-Factor App)
# We use is_local_dev if we want colored output locally.
is_local_dev = settings.app.environment in ("development", "local") if hasattr(settings.app, "environment") else False
# Fallback if environment doesn't exist on settings.app
# We'll just assume local dev if not explicitly production.
# Actually, the user's instructions didn't specify exactly about environment, but let's default to False or check settings.
setup_structlog(log_level="INFO", is_local_dev=is_local_dev)

logger = structlog.get_logger().bind(bounded_context="api")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manages Application Startup and Shutdown lifecycles.

    Nested Logical Steps:
        1. Database Bootstrap: Synchronize base models with pgStore.
        2. Telemetry Bootstrap: Initialize OpenTelemetry auto-instrumentation.
    """

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
