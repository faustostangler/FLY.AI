"""
CLI Presentation Layer — Composition Root for Worker Containers.

This module is the entry point for the Docker Worker container.
It wires the exact same Hexagonal dependency graph (Ports & Adapters)
used by the FastAPI API, ensuring a Single Source of Truth (SSOT)
for business logic execution.

Usage (from Docker):
    python -m src.shared.presentation.cli sync-companies
"""
import asyncio
import logging
import sys
import os

# --- Logging Setup (mirrors main.py SOTA configuration) ---
from shared.infrastructure.config import settings

os.makedirs(settings.app.log_dir, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s]: %(message)s",
    handlers=[
        logging.FileHandler(f"{settings.app.log_dir}/{settings.app.log_name}"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger(__name__)


def _create_sync_use_case():
    """
    Composition Root: Manually wires the dependency graph
    outside of FastAPI's DI container.

    This is the CLI equivalent of dependencies.py, following
    the Hexagonal Architecture pattern where the Composition Root
    lives at the outermost layer (Presentation/Infrastructure).
    """
    from shared.infrastructure.database.connection import engine, SessionLocal
    from companies.infrastructure.adapters.database.models import Base
    from companies.infrastructure.adapters.database.postgres_company_repository import (
        PostgresCompanyRepository,
    )
    from companies.infrastructure.adapters.data_sources.playwright_b3_data_source import (
        PlaywrightB3DataSource,
    )
    from companies.application.use_cases.sync_b3_companies import (
        SyncB3CompaniesUseCase,
    )

    # Ensure tables exist (same as FastAPI lifespan)
    Base.metadata.create_all(bind=engine)

    # Wire Adapters into Ports
    session = SessionLocal()
    repository = PostgresCompanyRepository(session=session)
    data_source = PlaywrightB3DataSource()

    use_case = SyncB3CompaniesUseCase(
        data_source=data_source,
        repository=repository,
    )
    return use_case, session


async def _run_sync_companies():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = _create_sync_use_case()
    try:
        logger.info("Worker: Starting B3 Companies Synchronization...")
        await use_case.execute()
        logger.info("Worker: Synchronization completed successfully.")
    except Exception as e:
        logger.error(f"Worker: Synchronization failed: {e}", exc_info=True)
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")
        
        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway, REGISTRY
        pushgateway_url = os.getenv("PUSHGATEWAY_URL", "http://metrics-ingestion:9091")
        
        try:
            logger.info(f"Empurrando métricas para o Pushgateway em {pushgateway_url}...")
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(pushgateway_url, job='worker_sync_companies', registry=REGISTRY)
            logger.info("Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion).")
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}")


async def main():
    if len(sys.argv) < 2:
        print("Usage: python -m src.shared.presentation.cli [command]")
        print("Available commands: sync-companies")
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        await _run_sync_companies()
    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
