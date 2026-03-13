from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from starlette.responses import Response
from companies.presentation.api.routes import router as companies_router
from shared.infrastructure.database.connection import engine
from companies.infrastructure.adapters.database.models import Base

import logging
import os
import time
from shared.infrastructure.config import settings
from shared.infrastructure.monitoring.metrics import metrics

# --- Logic for Logging SOTA Configuration ---
os.makedirs(settings.app.log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    # format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[
        logging.FileHandler(f"{settings.app.log_dir}/{settings.app.log_name}"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore
# --------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Ensure tables are created on startup 
    # (In a real scenario, use Alembic)
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title=settings.app.title,
    description=settings.app.description,
    version=settings.app.version,
    lifespan=lifespan
)

# --- SOTA Observability Middleware (Golden Signals) ---
@app.middleware("http")
async def prometheus_middleware(request: Request, call_next):
    # Traffic & Latency Logic
    method = request.method
    path = request.url.path
    
    # Start timer
    start_time = time.perf_counter()
    
    try:
        response = await call_next(request)
        duration = time.perf_counter() - start_time
        
        # Labels for labels
        status_code = str(response.status_code)
        
        # 1. LATENCY
        metrics.http_request_duration_seconds.labels(method=method, endpoint=path).observe(duration)
        
        # 2. TRAFFIC
        metrics.http_requests_total.labels(method=method, endpoint=path, status=status_code).inc()

        # 4. NETWORK (Outbound)
        content_length = response.headers.get("content-length")
        if content_length:
            resp_size = int(content_length)
            metrics.http_response_size_bytes.labels(method=method, endpoint=path).observe(resp_size)
            metrics.network_transmit_bytes_total.labels(direction="outbound", context="api").inc(resp_size)
        
        # 3. ERRORS (Non-2xx/3xx)
        if response.status_code >= 400:
            metrics.http_requests_failed_total.labels(
                method=method, 
                endpoint=path, 
                error_type=status_code
            ).inc()
            
        return response
        
    except Exception as e:
        # Capture unexpected crashes as Errors
        metrics.http_requests_failed_total.labels(
            method=method, 
            endpoint=path, 
            error_type=type(e).__name__
        ).inc()
        raise e

@app.get("/metrics")
def metrics_endpoint():
    """Exposes Prometheus metrics for scraping."""
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "FLY.AI Core operational"}

# Register Domain Routers
app.include_router(companies_router, prefix="/api/v1")

# Future routers
# app.include_router(financials_router, prefix="/api/v1")
# app.include_router(market_data_router, prefix="/api/v1")
