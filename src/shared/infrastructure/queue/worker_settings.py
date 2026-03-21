import structlog
from arq.connections import RedisSettings as ArqRedisSettings
from prometheus_client import start_http_server

from shared.infrastructure.config import settings
from shared.infrastructure.database.connection import AsyncSessionLocal, engine
from shared.infrastructure.monitoring.logging import setup_structlog
from shared.infrastructure.monitoring.tracing import setup_tracing
from shared.infrastructure.adapters.prometheus_telemetry import PrometheusTelemetryAdapter
from shared.application.constants.task_names import TaskNames

from companies.presentation.worker_dependencies import get_sync_b3_companies_use_case

logger = structlog.get_logger().bind(bounded_context="worker")


async def startup(ctx):
    """Lifecycle hook: Initializes infrastructure dependencies for the worker pool."""
    is_local_dev = settings.app.environment in ("development", "local") if hasattr(settings.app, "environment") else False
    setup_structlog(log_level="INFO", is_local_dev=is_local_dev)
    
    if settings.otel.enabled:
        setup_tracing(
            app=None, 
            engine=engine, 
            service_name=f"{settings.otel.service_name}_worker"
        )
        logger.info("Worker Distributed Tracing enabled")

    # Start a dedicated Prometheus metrics server for the worker on port 8081
    start_http_server(8081)
    logger.info("Worker Prometheus metrics server started on port 8081")


async def shutdown(ctx):
    """Lifecycle hook: Gracefully releases resources."""
    await engine.dispose()
    logger.info("Worker Database engine disposed")


async def run_sync_b3_companies(ctx):
    """ARQ Task Hook: Maps the worker execution to the Application DDD Use Case."""
    logger.info("Starting B3 Companies Synchronization task")
    
    async with AsyncSessionLocal() as db_session:
        use_case = get_sync_b3_companies_use_case(db_session=db_session)
        
        try:
            await use_case.execute()
        except Exception as e:
            logger.error("Sync task failed", error=str(e))
            raise e
        finally:
            await db_session.close()


class WorkerConfig:
    """ARQ Worker configuration singleton."""
    
    functions = [run_sync_b3_companies]
    
    # Using the same canonical configuration defined in the Shared Kernel
    redis_settings = ArqRedisSettings(
        host=settings.redis.host,
        port=settings.redis.port,
        database=settings.redis.db,
    )
    
    on_startup = startup
    on_shutdown = shutdown
    
    # Saturation limit: We strictly control concurrency to ensure the Node 
    # doesn't hit Out of Memory (OOM) due to high Playwright browser footprint.
    max_jobs = 5
