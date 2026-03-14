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
# Importamos nossas métricas definidas acima
from shared.infrastructure.monitoring import metrics 
from shared.infrastructure.monitoring.tracing import setup_tracing, OTelLogFilter

# --- Logic for Logging SOTA Configuration (with OTel Trace Correlation) ---
os.makedirs(settings.app.log_dir, exist_ok=True)

# SOTA: Log format with trace_id and span_id for Loki → Tempo correlation
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
        logging.StreamHandler()
    ]
)

# Attach OTel filter to root logger (all handlers inherit it)
otel_filter = OTelLogFilter()
for handler in logging.root.handlers:
    handler.addFilter(otel_filter)

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1. Create tables on startup (In production, use Alembic)
    Base.metadata.create_all(bind=engine)
    
    # 2. Bootstrap Distributed Tracing (Infrastructure Layer)
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
    lifespan=lifespan
)

# 1. Adicionamos a rota /metrics para o Prometheus raspar (Default + Custom)
# O make_asgi_app() já traz as Default Metrics do Python por padrão 
metrics_app = make_asgi_app()
app.mount("/metrics", metrics_app)

@app.middleware("http")
async def prometheus_middleware(request: Request, call_next):
    # Ignorar a própria rota de métricas para não sujar os dados
    if request.url.path == "/metrics":
        return await call_next(request)

    method = request.method
    # SOTA Tip: Use o template da rota (ex: /users/{id}) em vez da URL real
    path = request.scope.get("route").path if request.scope.get("route") else request.url.path
    
    # 1. IN-FLIGHT (Concorrência): Incrementa ao entrar
    metrics.IN_FLIGHT_REQUESTS.labels(method=method, endpoint=path).inc()
    
    # 2. PAYLOAD SIZE (Request): Sempre registrar bytes de entrada
    request_content_length = request.headers.get("content-length")
    if request_content_length:
        try:
            req_size = int(request_content_length)
            metrics.HTTP_REQUEST_SIZE.labels(method=method, endpoint=path).observe(req_size)
            metrics.NETWORK_TRANSMIT_BYTES_TOTAL.labels(direction="inbound", context="api").inc(req_size)
        except ValueError:
            pass

    start_time = time.perf_counter()
    
    try:
        response = await call_next(request)
        duration = time.perf_counter() - start_time
        status_code = str(response.status_code)
        
        # 3. Registrando Sinais de Ouro e Duração
        metrics.HTTP_REQUEST_DURATION.labels(method=method, endpoint=path).observe(duration)
        metrics.HTTP_REQUESTS_TOTAL.labels(method=method, endpoint=path, status=status_code).inc()
        
        # 4. PAYLOAD SIZE (Response): Sempre registrar bytes de saída
        content_length = response.headers.get("content-length")
        if content_length:
            try:
                resp_size = int(content_length)
                metrics.HTTP_RESPONSE_SIZE.labels(method=method, endpoint=path).observe(resp_size)
                metrics.NETWORK_TRANSMIT_BYTES_TOTAL.labels(direction="outbound", context="api").inc(resp_size)
            except ValueError:
                pass

        if response.status_code >= 400:
            metrics.HTTP_REQUESTS_FAILED_TOTAL.labels(
                method=method, endpoint=path, error_type=status_code
            ).inc()
            
        return response
        
    except Exception as e:
        # Erros Críticos (500)
        metrics.HTTP_REQUESTS_FAILED_TOTAL.labels(
            method=method, endpoint=path, error_type=type(e).__name__
        ).inc()
        raise e
        
    finally:
        # 1. IN-FLIGHT (Concorrência): Decrementa sempre ao sair (Garante consistência matemática)
        metrics.IN_FLIGHT_REQUESTS.labels(method=method, endpoint=path).dec()

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "FLY.AI Core operational"}

# Register Domain Routers
app.include_router(companies_router, prefix="/api/v1")

# Future routers
# app.include_router(financials_router, prefix="/api/v1")
# app.include_router(market_data_router, prefix="/api/v1")
