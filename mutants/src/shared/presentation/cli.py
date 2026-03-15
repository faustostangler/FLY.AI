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
from typing import Annotated
from typing import Callable
from typing import ClassVar

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


def _create_sync_use_case():
    args = []  # type: ignore
    kwargs = {}  # type: ignore
    return _mutmut_trampoline(
        x__create_sync_use_case__mutmut_orig,
        x__create_sync_use_case__mutmut_mutants,
        args,
        kwargs,
        None,
    )


def x__create_sync_use_case__mutmut_orig():
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
    from shared.infrastructure.adapters.prometheus_telemetry import (
        PrometheusTelemetryAdapter,
    )

    # Ensure tables exist (same as FastAPI lifespan)
    Base.metadata.create_all(bind=engine)

    # Wire Adapters into Ports
    session = SessionLocal()
    repository = PostgresCompanyRepository(session=session)
    telemetry = PrometheusTelemetryAdapter()
    data_source = PlaywrightB3DataSource(telemetry=telemetry)

    use_case = SyncB3CompaniesUseCase(
        data_source=data_source,
        repository=repository,
        telemetry=telemetry,
    )
    return use_case, session


def x__create_sync_use_case__mutmut_1():
    """
    Composition Root: Manually wires the dependency graph
    outside of FastAPI's DI container.

    This is the CLI equivalent of dependencies.py, following
    the Hexagonal Architecture pattern where the Composition Root
    lives at the outermost layer (Presentation/Infrastructure).
    """
    from shared.infrastructure.database.connection import SessionLocal
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
    from shared.infrastructure.adapters.prometheus_telemetry import (
        PrometheusTelemetryAdapter,
    )

    # Ensure tables exist (same as FastAPI lifespan)
    Base.metadata.create_all(bind=None)

    # Wire Adapters into Ports
    session = SessionLocal()
    repository = PostgresCompanyRepository(session=session)
    telemetry = PrometheusTelemetryAdapter()
    data_source = PlaywrightB3DataSource(telemetry=telemetry)

    use_case = SyncB3CompaniesUseCase(
        data_source=data_source,
        repository=repository,
        telemetry=telemetry,
    )
    return use_case, session


def x__create_sync_use_case__mutmut_2():
    """
    Composition Root: Manually wires the dependency graph
    outside of FastAPI's DI container.

    This is the CLI equivalent of dependencies.py, following
    the Hexagonal Architecture pattern where the Composition Root
    lives at the outermost layer (Presentation/Infrastructure).
    """
    from shared.infrastructure.database.connection import engine
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
    from shared.infrastructure.adapters.prometheus_telemetry import (
        PrometheusTelemetryAdapter,
    )

    # Ensure tables exist (same as FastAPI lifespan)
    Base.metadata.create_all(bind=engine)

    # Wire Adapters into Ports
    session = None
    repository = PostgresCompanyRepository(session=session)
    telemetry = PrometheusTelemetryAdapter()
    data_source = PlaywrightB3DataSource(telemetry=telemetry)

    use_case = SyncB3CompaniesUseCase(
        data_source=data_source,
        repository=repository,
        telemetry=telemetry,
    )
    return use_case, session


def x__create_sync_use_case__mutmut_3():
    """
    Composition Root: Manually wires the dependency graph
    outside of FastAPI's DI container.

    This is the CLI equivalent of dependencies.py, following
    the Hexagonal Architecture pattern where the Composition Root
    lives at the outermost layer (Presentation/Infrastructure).
    """
    from shared.infrastructure.database.connection import engine, SessionLocal
    from companies.infrastructure.adapters.database.models import Base
    from companies.infrastructure.adapters.data_sources.playwright_b3_data_source import (
        PlaywrightB3DataSource,
    )
    from companies.application.use_cases.sync_b3_companies import (
        SyncB3CompaniesUseCase,
    )
    from shared.infrastructure.adapters.prometheus_telemetry import (
        PrometheusTelemetryAdapter,
    )

    # Ensure tables exist (same as FastAPI lifespan)
    Base.metadata.create_all(bind=engine)

    # Wire Adapters into Ports
    session = SessionLocal()
    repository = None
    telemetry = PrometheusTelemetryAdapter()
    data_source = PlaywrightB3DataSource(telemetry=telemetry)

    use_case = SyncB3CompaniesUseCase(
        data_source=data_source,
        repository=repository,
        telemetry=telemetry,
    )
    return use_case, session


def x__create_sync_use_case__mutmut_4():
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
    from shared.infrastructure.adapters.prometheus_telemetry import (
        PrometheusTelemetryAdapter,
    )

    # Ensure tables exist (same as FastAPI lifespan)
    Base.metadata.create_all(bind=engine)

    # Wire Adapters into Ports
    session = SessionLocal()
    repository = PostgresCompanyRepository(session=None)
    telemetry = PrometheusTelemetryAdapter()
    data_source = PlaywrightB3DataSource(telemetry=telemetry)

    use_case = SyncB3CompaniesUseCase(
        data_source=data_source,
        repository=repository,
        telemetry=telemetry,
    )
    return use_case, session


def x__create_sync_use_case__mutmut_5():
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
    telemetry = None
    data_source = PlaywrightB3DataSource(telemetry=telemetry)

    use_case = SyncB3CompaniesUseCase(
        data_source=data_source,
        repository=repository,
        telemetry=telemetry,
    )
    return use_case, session


def x__create_sync_use_case__mutmut_6():
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
    from companies.application.use_cases.sync_b3_companies import (
        SyncB3CompaniesUseCase,
    )
    from shared.infrastructure.adapters.prometheus_telemetry import (
        PrometheusTelemetryAdapter,
    )

    # Ensure tables exist (same as FastAPI lifespan)
    Base.metadata.create_all(bind=engine)

    # Wire Adapters into Ports
    session = SessionLocal()
    repository = PostgresCompanyRepository(session=session)
    telemetry = PrometheusTelemetryAdapter()
    data_source = None

    use_case = SyncB3CompaniesUseCase(
        data_source=data_source,
        repository=repository,
        telemetry=telemetry,
    )
    return use_case, session


def x__create_sync_use_case__mutmut_7():
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
    from shared.infrastructure.adapters.prometheus_telemetry import (
        PrometheusTelemetryAdapter,
    )

    # Ensure tables exist (same as FastAPI lifespan)
    Base.metadata.create_all(bind=engine)

    # Wire Adapters into Ports
    session = SessionLocal()
    repository = PostgresCompanyRepository(session=session)
    telemetry = PrometheusTelemetryAdapter()
    data_source = PlaywrightB3DataSource(telemetry=None)

    use_case = SyncB3CompaniesUseCase(
        data_source=data_source,
        repository=repository,
        telemetry=telemetry,
    )
    return use_case, session


def x__create_sync_use_case__mutmut_8():
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
    from shared.infrastructure.adapters.prometheus_telemetry import (
        PrometheusTelemetryAdapter,
    )

    # Ensure tables exist (same as FastAPI lifespan)
    Base.metadata.create_all(bind=engine)

    # Wire Adapters into Ports
    session = SessionLocal()
    repository = PostgresCompanyRepository(session=session)
    telemetry = PrometheusTelemetryAdapter()
    data_source = PlaywrightB3DataSource(telemetry=telemetry)

    use_case = None
    return use_case, session


def x__create_sync_use_case__mutmut_9():
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
    from shared.infrastructure.adapters.prometheus_telemetry import (
        PrometheusTelemetryAdapter,
    )

    # Ensure tables exist (same as FastAPI lifespan)
    Base.metadata.create_all(bind=engine)

    # Wire Adapters into Ports
    session = SessionLocal()
    repository = PostgresCompanyRepository(session=session)
    telemetry = PrometheusTelemetryAdapter()
    data_source = PlaywrightB3DataSource(telemetry=telemetry)

    use_case = SyncB3CompaniesUseCase(
        data_source=None,
        repository=repository,
        telemetry=telemetry,
    )
    return use_case, session


def x__create_sync_use_case__mutmut_10():
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
    from shared.infrastructure.adapters.prometheus_telemetry import (
        PrometheusTelemetryAdapter,
    )

    # Ensure tables exist (same as FastAPI lifespan)
    Base.metadata.create_all(bind=engine)

    # Wire Adapters into Ports
    session = SessionLocal()
    repository = PostgresCompanyRepository(session=session)
    telemetry = PrometheusTelemetryAdapter()
    data_source = PlaywrightB3DataSource(telemetry=telemetry)

    use_case = SyncB3CompaniesUseCase(
        data_source=data_source,
        repository=None,
        telemetry=telemetry,
    )
    return use_case, session


def x__create_sync_use_case__mutmut_11():
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
    from shared.infrastructure.adapters.prometheus_telemetry import (
        PrometheusTelemetryAdapter,
    )

    # Ensure tables exist (same as FastAPI lifespan)
    Base.metadata.create_all(bind=engine)

    # Wire Adapters into Ports
    session = SessionLocal()
    repository = PostgresCompanyRepository(session=session)
    telemetry = PrometheusTelemetryAdapter()
    data_source = PlaywrightB3DataSource(telemetry=telemetry)

    use_case = SyncB3CompaniesUseCase(
        data_source=data_source,
        repository=repository,
        telemetry=None,
    )
    return use_case, session


def x__create_sync_use_case__mutmut_12():
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
    from shared.infrastructure.adapters.prometheus_telemetry import (
        PrometheusTelemetryAdapter,
    )

    # Ensure tables exist (same as FastAPI lifespan)
    Base.metadata.create_all(bind=engine)

    # Wire Adapters into Ports
    session = SessionLocal()
    repository = PostgresCompanyRepository(session=session)
    telemetry = PrometheusTelemetryAdapter()
    data_source = PlaywrightB3DataSource(telemetry=telemetry)

    use_case = SyncB3CompaniesUseCase(
        repository=repository,
        telemetry=telemetry,
    )
    return use_case, session


def x__create_sync_use_case__mutmut_13():
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
    from shared.infrastructure.adapters.prometheus_telemetry import (
        PrometheusTelemetryAdapter,
    )

    # Ensure tables exist (same as FastAPI lifespan)
    Base.metadata.create_all(bind=engine)

    # Wire Adapters into Ports
    session = SessionLocal()
    repository = PostgresCompanyRepository(session=session)
    telemetry = PrometheusTelemetryAdapter()
    data_source = PlaywrightB3DataSource(telemetry=telemetry)

    use_case = SyncB3CompaniesUseCase(
        data_source=data_source,
        telemetry=telemetry,
    )
    return use_case, session


def x__create_sync_use_case__mutmut_14():
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
    from shared.infrastructure.adapters.prometheus_telemetry import (
        PrometheusTelemetryAdapter,
    )

    # Ensure tables exist (same as FastAPI lifespan)
    Base.metadata.create_all(bind=engine)

    # Wire Adapters into Ports
    session = SessionLocal()
    repository = PostgresCompanyRepository(session=session)
    telemetry = PrometheusTelemetryAdapter()
    data_source = PlaywrightB3DataSource(telemetry=telemetry)

    use_case = SyncB3CompaniesUseCase(
        data_source=data_source,
        repository=repository,
    )
    return use_case, session


x__create_sync_use_case__mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
    "x__create_sync_use_case__mutmut_1": x__create_sync_use_case__mutmut_1,
    "x__create_sync_use_case__mutmut_2": x__create_sync_use_case__mutmut_2,
    "x__create_sync_use_case__mutmut_3": x__create_sync_use_case__mutmut_3,
    "x__create_sync_use_case__mutmut_4": x__create_sync_use_case__mutmut_4,
    "x__create_sync_use_case__mutmut_5": x__create_sync_use_case__mutmut_5,
    "x__create_sync_use_case__mutmut_6": x__create_sync_use_case__mutmut_6,
    "x__create_sync_use_case__mutmut_7": x__create_sync_use_case__mutmut_7,
    "x__create_sync_use_case__mutmut_8": x__create_sync_use_case__mutmut_8,
    "x__create_sync_use_case__mutmut_9": x__create_sync_use_case__mutmut_9,
    "x__create_sync_use_case__mutmut_10": x__create_sync_use_case__mutmut_10,
    "x__create_sync_use_case__mutmut_11": x__create_sync_use_case__mutmut_11,
    "x__create_sync_use_case__mutmut_12": x__create_sync_use_case__mutmut_12,
    "x__create_sync_use_case__mutmut_13": x__create_sync_use_case__mutmut_13,
    "x__create_sync_use_case__mutmut_14": x__create_sync_use_case__mutmut_14,
}
x__create_sync_use_case__mutmut_orig.__name__ = "x__create_sync_use_case"


async def _run_sync_companies():
    args = []  # type: ignore
    kwargs = {}  # type: ignore
    return await _mutmut_trampoline(
        x__run_sync_companies__mutmut_orig,
        x__run_sync_companies__mutmut_mutants,
        args,
        kwargs,
        None,
    )


async def x__run_sync_companies__mutmut_orig():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = _create_sync_use_case()
    try:
        logger.info(
            "Worker: Starting B3 Companies Synchronization..."
        )  # pragma: no mutate
        await use_case.execute()
        logger.info(
            "Worker: Synchronization completed successfully."
        )  # pragma: no mutate
    except Exception as e:
        logger.error(
            f"Worker: Synchronization failed: {e}", exc_info=True
        )  # pragma: no mutate
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")  # pragma: no mutate

        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway, REGISTRY

        pushgateway_url = os.getenv("PUSHGATEWAY_URL", "http://metrics-ingestion:9091")

        try:
            logger.info(
                f"Empurrando métricas para o Pushgateway em {pushgateway_url}..."
            )  # pragma: no mutate
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(
                pushgateway_url, job="worker_sync_companies", registry=REGISTRY
            )
            logger.info(
                "Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion)."
            )  # pragma: no mutate
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(
                f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}"
            )  # pragma: no mutate


async def x__run_sync_companies__mutmut_1():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = None
    try:
        logger.info(
            "Worker: Starting B3 Companies Synchronization..."
        )  # pragma: no mutate
        await use_case.execute()
        logger.info(
            "Worker: Synchronization completed successfully."
        )  # pragma: no mutate
    except Exception as e:
        logger.error(
            f"Worker: Synchronization failed: {e}", exc_info=True
        )  # pragma: no mutate
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")  # pragma: no mutate

        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway, REGISTRY

        pushgateway_url = os.getenv("PUSHGATEWAY_URL", "http://metrics-ingestion:9091")

        try:
            logger.info(
                f"Empurrando métricas para o Pushgateway em {pushgateway_url}..."
            )  # pragma: no mutate
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(
                pushgateway_url, job="worker_sync_companies", registry=REGISTRY
            )
            logger.info(
                "Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion)."
            )  # pragma: no mutate
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(
                f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}"
            )  # pragma: no mutate


async def x__run_sync_companies__mutmut_2():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = _create_sync_use_case()
    try:
        logger.info(
            "Worker: Starting B3 Companies Synchronization..."
        )  # pragma: no mutate
        await use_case.execute()
        logger.info(
            "Worker: Synchronization completed successfully."
        )  # pragma: no mutate
    except Exception as e:
        logger.error(
            f"Worker: Synchronization failed: {e}", exc_info=True
        )  # pragma: no mutate
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")  # pragma: no mutate

        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway, REGISTRY

        pushgateway_url = None

        try:
            logger.info(
                f"Empurrando métricas para o Pushgateway em {pushgateway_url}..."
            )  # pragma: no mutate
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(
                pushgateway_url, job="worker_sync_companies", registry=REGISTRY
            )
            logger.info(
                "Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion)."
            )  # pragma: no mutate
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(
                f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}"
            )  # pragma: no mutate


async def x__run_sync_companies__mutmut_3():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = _create_sync_use_case()
    try:
        logger.info(
            "Worker: Starting B3 Companies Synchronization..."
        )  # pragma: no mutate
        await use_case.execute()
        logger.info(
            "Worker: Synchronization completed successfully."
        )  # pragma: no mutate
    except Exception as e:
        logger.error(
            f"Worker: Synchronization failed: {e}", exc_info=True
        )  # pragma: no mutate
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")  # pragma: no mutate

        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway, REGISTRY

        pushgateway_url = os.getenv(None, "http://metrics-ingestion:9091")

        try:
            logger.info(
                f"Empurrando métricas para o Pushgateway em {pushgateway_url}..."
            )  # pragma: no mutate
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(
                pushgateway_url, job="worker_sync_companies", registry=REGISTRY
            )
            logger.info(
                "Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion)."
            )  # pragma: no mutate
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(
                f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}"
            )  # pragma: no mutate


async def x__run_sync_companies__mutmut_4():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = _create_sync_use_case()
    try:
        logger.info(
            "Worker: Starting B3 Companies Synchronization..."
        )  # pragma: no mutate
        await use_case.execute()
        logger.info(
            "Worker: Synchronization completed successfully."
        )  # pragma: no mutate
    except Exception as e:
        logger.error(
            f"Worker: Synchronization failed: {e}", exc_info=True
        )  # pragma: no mutate
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")  # pragma: no mutate

        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway, REGISTRY

        pushgateway_url = os.getenv("PUSHGATEWAY_URL", None)

        try:
            logger.info(
                f"Empurrando métricas para o Pushgateway em {pushgateway_url}..."
            )  # pragma: no mutate
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(
                pushgateway_url, job="worker_sync_companies", registry=REGISTRY
            )
            logger.info(
                "Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion)."
            )  # pragma: no mutate
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(
                f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}"
            )  # pragma: no mutate


async def x__run_sync_companies__mutmut_5():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = _create_sync_use_case()
    try:
        logger.info(
            "Worker: Starting B3 Companies Synchronization..."
        )  # pragma: no mutate
        await use_case.execute()
        logger.info(
            "Worker: Synchronization completed successfully."
        )  # pragma: no mutate
    except Exception as e:
        logger.error(
            f"Worker: Synchronization failed: {e}", exc_info=True
        )  # pragma: no mutate
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")  # pragma: no mutate

        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway, REGISTRY

        pushgateway_url = os.getenv("http://metrics-ingestion:9091")

        try:
            logger.info(
                f"Empurrando métricas para o Pushgateway em {pushgateway_url}..."
            )  # pragma: no mutate
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(
                pushgateway_url, job="worker_sync_companies", registry=REGISTRY
            )
            logger.info(
                "Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion)."
            )  # pragma: no mutate
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(
                f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}"
            )  # pragma: no mutate


async def x__run_sync_companies__mutmut_6():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = _create_sync_use_case()
    try:
        logger.info(
            "Worker: Starting B3 Companies Synchronization..."
        )  # pragma: no mutate
        await use_case.execute()
        logger.info(
            "Worker: Synchronization completed successfully."
        )  # pragma: no mutate
    except Exception as e:
        logger.error(
            f"Worker: Synchronization failed: {e}", exc_info=True
        )  # pragma: no mutate
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")  # pragma: no mutate

        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway, REGISTRY

        pushgateway_url = os.getenv(
            "PUSHGATEWAY_URL",
        )

        try:
            logger.info(
                f"Empurrando métricas para o Pushgateway em {pushgateway_url}..."
            )  # pragma: no mutate
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(
                pushgateway_url, job="worker_sync_companies", registry=REGISTRY
            )
            logger.info(
                "Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion)."
            )  # pragma: no mutate
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(
                f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}"
            )  # pragma: no mutate


async def x__run_sync_companies__mutmut_7():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = _create_sync_use_case()
    try:
        logger.info(
            "Worker: Starting B3 Companies Synchronization..."
        )  # pragma: no mutate
        await use_case.execute()
        logger.info(
            "Worker: Synchronization completed successfully."
        )  # pragma: no mutate
    except Exception as e:
        logger.error(
            f"Worker: Synchronization failed: {e}", exc_info=True
        )  # pragma: no mutate
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")  # pragma: no mutate

        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway, REGISTRY

        pushgateway_url = os.getenv(
            "XXPUSHGATEWAY_URLXX", "http://metrics-ingestion:9091"
        )

        try:
            logger.info(
                f"Empurrando métricas para o Pushgateway em {pushgateway_url}..."
            )  # pragma: no mutate
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(
                pushgateway_url, job="worker_sync_companies", registry=REGISTRY
            )
            logger.info(
                "Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion)."
            )  # pragma: no mutate
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(
                f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}"
            )  # pragma: no mutate


async def x__run_sync_companies__mutmut_8():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = _create_sync_use_case()
    try:
        logger.info(
            "Worker: Starting B3 Companies Synchronization..."
        )  # pragma: no mutate
        await use_case.execute()
        logger.info(
            "Worker: Synchronization completed successfully."
        )  # pragma: no mutate
    except Exception as e:
        logger.error(
            f"Worker: Synchronization failed: {e}", exc_info=True
        )  # pragma: no mutate
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")  # pragma: no mutate

        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway, REGISTRY

        pushgateway_url = os.getenv("pushgateway_url", "http://metrics-ingestion:9091")

        try:
            logger.info(
                f"Empurrando métricas para o Pushgateway em {pushgateway_url}..."
            )  # pragma: no mutate
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(
                pushgateway_url, job="worker_sync_companies", registry=REGISTRY
            )
            logger.info(
                "Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion)."
            )  # pragma: no mutate
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(
                f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}"
            )  # pragma: no mutate


async def x__run_sync_companies__mutmut_9():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = _create_sync_use_case()
    try:
        logger.info(
            "Worker: Starting B3 Companies Synchronization..."
        )  # pragma: no mutate
        await use_case.execute()
        logger.info(
            "Worker: Synchronization completed successfully."
        )  # pragma: no mutate
    except Exception as e:
        logger.error(
            f"Worker: Synchronization failed: {e}", exc_info=True
        )  # pragma: no mutate
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")  # pragma: no mutate

        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway, REGISTRY

        pushgateway_url = os.getenv(
            "PUSHGATEWAY_URL", "XXhttp://metrics-ingestion:9091XX"
        )

        try:
            logger.info(
                f"Empurrando métricas para o Pushgateway em {pushgateway_url}..."
            )  # pragma: no mutate
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(
                pushgateway_url, job="worker_sync_companies", registry=REGISTRY
            )
            logger.info(
                "Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion)."
            )  # pragma: no mutate
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(
                f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}"
            )  # pragma: no mutate


async def x__run_sync_companies__mutmut_10():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = _create_sync_use_case()
    try:
        logger.info(
            "Worker: Starting B3 Companies Synchronization..."
        )  # pragma: no mutate
        await use_case.execute()
        logger.info(
            "Worker: Synchronization completed successfully."
        )  # pragma: no mutate
    except Exception as e:
        logger.error(
            f"Worker: Synchronization failed: {e}", exc_info=True
        )  # pragma: no mutate
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")  # pragma: no mutate

        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway, REGISTRY

        pushgateway_url = os.getenv("PUSHGATEWAY_URL", "HTTP://METRICS-INGESTION:9091")

        try:
            logger.info(
                f"Empurrando métricas para o Pushgateway em {pushgateway_url}..."
            )  # pragma: no mutate
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(
                pushgateway_url, job="worker_sync_companies", registry=REGISTRY
            )
            logger.info(
                "Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion)."
            )  # pragma: no mutate
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(
                f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}"
            )  # pragma: no mutate


async def x__run_sync_companies__mutmut_11():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = _create_sync_use_case()
    try:
        logger.info(
            "Worker: Starting B3 Companies Synchronization..."
        )  # pragma: no mutate
        await use_case.execute()
        logger.info(
            "Worker: Synchronization completed successfully."
        )  # pragma: no mutate
    except Exception as e:
        logger.error(
            f"Worker: Synchronization failed: {e}", exc_info=True
        )  # pragma: no mutate
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")  # pragma: no mutate

        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway, REGISTRY

        pushgateway_url = os.getenv("PUSHGATEWAY_URL", "http://metrics-ingestion:9091")

        try:
            logger.info(
                f"Empurrando métricas para o Pushgateway em {pushgateway_url}..."
            )  # pragma: no mutate
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(None, job="worker_sync_companies", registry=REGISTRY)
            logger.info(
                "Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion)."
            )  # pragma: no mutate
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(
                f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}"
            )  # pragma: no mutate


async def x__run_sync_companies__mutmut_12():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = _create_sync_use_case()
    try:
        logger.info(
            "Worker: Starting B3 Companies Synchronization..."
        )  # pragma: no mutate
        await use_case.execute()
        logger.info(
            "Worker: Synchronization completed successfully."
        )  # pragma: no mutate
    except Exception as e:
        logger.error(
            f"Worker: Synchronization failed: {e}", exc_info=True
        )  # pragma: no mutate
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")  # pragma: no mutate

        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway, REGISTRY

        pushgateway_url = os.getenv("PUSHGATEWAY_URL", "http://metrics-ingestion:9091")

        try:
            logger.info(
                f"Empurrando métricas para o Pushgateway em {pushgateway_url}..."
            )  # pragma: no mutate
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(pushgateway_url, job=None, registry=REGISTRY)
            logger.info(
                "Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion)."
            )  # pragma: no mutate
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(
                f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}"
            )  # pragma: no mutate


async def x__run_sync_companies__mutmut_13():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = _create_sync_use_case()
    try:
        logger.info(
            "Worker: Starting B3 Companies Synchronization..."
        )  # pragma: no mutate
        await use_case.execute()
        logger.info(
            "Worker: Synchronization completed successfully."
        )  # pragma: no mutate
    except Exception as e:
        logger.error(
            f"Worker: Synchronization failed: {e}", exc_info=True
        )  # pragma: no mutate
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")  # pragma: no mutate

        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway

        pushgateway_url = os.getenv("PUSHGATEWAY_URL", "http://metrics-ingestion:9091")

        try:
            logger.info(
                f"Empurrando métricas para o Pushgateway em {pushgateway_url}..."
            )  # pragma: no mutate
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(pushgateway_url, job="worker_sync_companies", registry=None)
            logger.info(
                "Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion)."
            )  # pragma: no mutate
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(
                f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}"
            )  # pragma: no mutate


async def x__run_sync_companies__mutmut_14():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = _create_sync_use_case()
    try:
        logger.info(
            "Worker: Starting B3 Companies Synchronization..."
        )  # pragma: no mutate
        await use_case.execute()
        logger.info(
            "Worker: Synchronization completed successfully."
        )  # pragma: no mutate
    except Exception as e:
        logger.error(
            f"Worker: Synchronization failed: {e}", exc_info=True
        )  # pragma: no mutate
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")  # pragma: no mutate

        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway, REGISTRY

        pushgateway_url = os.getenv("PUSHGATEWAY_URL", "http://metrics-ingestion:9091")

        try:
            logger.info(
                f"Empurrando métricas para o Pushgateway em {pushgateway_url}..."
            )  # pragma: no mutate
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(job="worker_sync_companies", registry=REGISTRY)
            logger.info(
                "Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion)."
            )  # pragma: no mutate
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(
                f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}"
            )  # pragma: no mutate


async def x__run_sync_companies__mutmut_15():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = _create_sync_use_case()
    try:
        logger.info(
            "Worker: Starting B3 Companies Synchronization..."
        )  # pragma: no mutate
        await use_case.execute()
        logger.info(
            "Worker: Synchronization completed successfully."
        )  # pragma: no mutate
    except Exception as e:
        logger.error(
            f"Worker: Synchronization failed: {e}", exc_info=True
        )  # pragma: no mutate
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")  # pragma: no mutate

        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway, REGISTRY

        pushgateway_url = os.getenv("PUSHGATEWAY_URL", "http://metrics-ingestion:9091")

        try:
            logger.info(
                f"Empurrando métricas para o Pushgateway em {pushgateway_url}..."
            )  # pragma: no mutate
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(pushgateway_url, registry=REGISTRY)
            logger.info(
                "Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion)."
            )  # pragma: no mutate
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(
                f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}"
            )  # pragma: no mutate


async def x__run_sync_companies__mutmut_16():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = _create_sync_use_case()
    try:
        logger.info(
            "Worker: Starting B3 Companies Synchronization..."
        )  # pragma: no mutate
        await use_case.execute()
        logger.info(
            "Worker: Synchronization completed successfully."
        )  # pragma: no mutate
    except Exception as e:
        logger.error(
            f"Worker: Synchronization failed: {e}", exc_info=True
        )  # pragma: no mutate
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")  # pragma: no mutate

        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway

        pushgateway_url = os.getenv("PUSHGATEWAY_URL", "http://metrics-ingestion:9091")

        try:
            logger.info(
                f"Empurrando métricas para o Pushgateway em {pushgateway_url}..."
            )  # pragma: no mutate
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(
                pushgateway_url,
                job="worker_sync_companies",
            )
            logger.info(
                "Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion)."
            )  # pragma: no mutate
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(
                f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}"
            )  # pragma: no mutate


async def x__run_sync_companies__mutmut_17():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = _create_sync_use_case()
    try:
        logger.info(
            "Worker: Starting B3 Companies Synchronization..."
        )  # pragma: no mutate
        await use_case.execute()
        logger.info(
            "Worker: Synchronization completed successfully."
        )  # pragma: no mutate
    except Exception as e:
        logger.error(
            f"Worker: Synchronization failed: {e}", exc_info=True
        )  # pragma: no mutate
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")  # pragma: no mutate

        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway, REGISTRY

        pushgateway_url = os.getenv("PUSHGATEWAY_URL", "http://metrics-ingestion:9091")

        try:
            logger.info(
                f"Empurrando métricas para o Pushgateway em {pushgateway_url}..."
            )  # pragma: no mutate
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(
                pushgateway_url, job="XXworker_sync_companiesXX", registry=REGISTRY
            )
            logger.info(
                "Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion)."
            )  # pragma: no mutate
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(
                f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}"
            )  # pragma: no mutate


async def x__run_sync_companies__mutmut_18():
    """Executes the SyncB3CompaniesUseCase with proper resource cleanup."""
    use_case, session = _create_sync_use_case()
    try:
        logger.info(
            "Worker: Starting B3 Companies Synchronization..."
        )  # pragma: no mutate
        await use_case.execute()
        logger.info(
            "Worker: Synchronization completed successfully."
        )  # pragma: no mutate
    except Exception as e:
        logger.error(
            f"Worker: Synchronization failed: {e}", exc_info=True
        )  # pragma: no mutate
        raise
    finally:
        session.close()
        logger.info("Worker: Database session closed.")  # pragma: no mutate

        # SOTA: EMPURRAR PARA O PUSHGATEWAY ANTES DO CONTÊINER MORRER
        from prometheus_client import push_to_gateway, REGISTRY

        pushgateway_url = os.getenv("PUSHGATEWAY_URL", "http://metrics-ingestion:9091")

        try:
            logger.info(
                f"Empurrando métricas para o Pushgateway em {pushgateway_url}..."
            )  # pragma: no mutate
            # 'job' é a etiqueta que agrupará essas métricas lá no Prometheus
            push_to_gateway(
                pushgateway_url, job="WORKER_SYNC_COMPANIES", registry=REGISTRY
            )
            logger.info(
                "Métricas empurradas com sucesso para o Pushgateway (metrics-ingestion)."
            )  # pragma: no mutate
        except Exception as pg_error:
            # Não queremos que uma falha na telemetria quebre o job principal, apenas logamos
            logger.error(
                f"Falha ao enviar métricas para o Pushgateway (metrics-ingestion): {pg_error}"
            )  # pragma: no mutate


x__run_sync_companies__mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
    "x__run_sync_companies__mutmut_1": x__run_sync_companies__mutmut_1,
    "x__run_sync_companies__mutmut_2": x__run_sync_companies__mutmut_2,
    "x__run_sync_companies__mutmut_3": x__run_sync_companies__mutmut_3,
    "x__run_sync_companies__mutmut_4": x__run_sync_companies__mutmut_4,
    "x__run_sync_companies__mutmut_5": x__run_sync_companies__mutmut_5,
    "x__run_sync_companies__mutmut_6": x__run_sync_companies__mutmut_6,
    "x__run_sync_companies__mutmut_7": x__run_sync_companies__mutmut_7,
    "x__run_sync_companies__mutmut_8": x__run_sync_companies__mutmut_8,
    "x__run_sync_companies__mutmut_9": x__run_sync_companies__mutmut_9,
    "x__run_sync_companies__mutmut_10": x__run_sync_companies__mutmut_10,
    "x__run_sync_companies__mutmut_11": x__run_sync_companies__mutmut_11,
    "x__run_sync_companies__mutmut_12": x__run_sync_companies__mutmut_12,
    "x__run_sync_companies__mutmut_13": x__run_sync_companies__mutmut_13,
    "x__run_sync_companies__mutmut_14": x__run_sync_companies__mutmut_14,
    "x__run_sync_companies__mutmut_15": x__run_sync_companies__mutmut_15,
    "x__run_sync_companies__mutmut_16": x__run_sync_companies__mutmut_16,
    "x__run_sync_companies__mutmut_17": x__run_sync_companies__mutmut_17,
    "x__run_sync_companies__mutmut_18": x__run_sync_companies__mutmut_18,
}
x__run_sync_companies__mutmut_orig.__name__ = "x__run_sync_companies"


async def main():
    args = []  # type: ignore
    kwargs = {}  # type: ignore
    return await _mutmut_trampoline(
        x_main__mutmut_orig, x_main__mutmut_mutants, args, kwargs, None
    )


async def x_main__mutmut_orig():
    if len(sys.argv) < 2:
        print(
            "Usage: python -m src.shared.presentation.cli [command]"
        )  # pragma: no mutate
        print("Available commands: sync-companies")  # pragma: no mutate
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        await _run_sync_companies()
    else:
        print(f"Unknown command: {cmd}")  # pragma: no mutate
        sys.exit(1)


async def x_main__mutmut_1():
    if len(sys.argv) <= 2:
        print(
            "Usage: python -m src.shared.presentation.cli [command]"
        )  # pragma: no mutate
        print("Available commands: sync-companies")  # pragma: no mutate
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        await _run_sync_companies()
    else:
        print(f"Unknown command: {cmd}")  # pragma: no mutate
        sys.exit(1)


async def x_main__mutmut_2():
    if len(sys.argv) < 3:
        print(
            "Usage: python -m src.shared.presentation.cli [command]"
        )  # pragma: no mutate
        print("Available commands: sync-companies")  # pragma: no mutate
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        await _run_sync_companies()
    else:
        print(f"Unknown command: {cmd}")  # pragma: no mutate
        sys.exit(1)


async def x_main__mutmut_3():
    if len(sys.argv) < 2:
        print(
            "Usage: python -m src.shared.presentation.cli [command]"
        )  # pragma: no mutate
        print("Available commands: sync-companies")  # pragma: no mutate
        return

    cmd = None
    if cmd == "sync-companies":
        await _run_sync_companies()
    else:
        print(f"Unknown command: {cmd}")  # pragma: no mutate
        sys.exit(1)


async def x_main__mutmut_4():
    if len(sys.argv) < 2:
        print(
            "Usage: python -m src.shared.presentation.cli [command]"
        )  # pragma: no mutate
        print("Available commands: sync-companies")  # pragma: no mutate
        return

    cmd = sys.argv[2]
    if cmd == "sync-companies":
        await _run_sync_companies()
    else:
        print(f"Unknown command: {cmd}")  # pragma: no mutate
        sys.exit(1)


async def x_main__mutmut_5():
    if len(sys.argv) < 2:
        print(
            "Usage: python -m src.shared.presentation.cli [command]"
        )  # pragma: no mutate
        print("Available commands: sync-companies")  # pragma: no mutate
        return

    cmd = sys.argv[1]
    if cmd != "sync-companies":
        await _run_sync_companies()
    else:
        print(f"Unknown command: {cmd}")  # pragma: no mutate
        sys.exit(1)


async def x_main__mutmut_6():
    if len(sys.argv) < 2:
        print(
            "Usage: python -m src.shared.presentation.cli [command]"
        )  # pragma: no mutate
        print("Available commands: sync-companies")  # pragma: no mutate
        return

    cmd = sys.argv[1]
    if cmd == "XXsync-companiesXX":
        await _run_sync_companies()
    else:
        print(f"Unknown command: {cmd}")  # pragma: no mutate
        sys.exit(1)


async def x_main__mutmut_7():
    if len(sys.argv) < 2:
        print(
            "Usage: python -m src.shared.presentation.cli [command]"
        )  # pragma: no mutate
        print("Available commands: sync-companies")  # pragma: no mutate
        return

    cmd = sys.argv[1]
    if cmd == "SYNC-COMPANIES":
        await _run_sync_companies()
    else:
        print(f"Unknown command: {cmd}")  # pragma: no mutate
        sys.exit(1)


async def x_main__mutmut_8():
    if len(sys.argv) < 2:
        print(
            "Usage: python -m src.shared.presentation.cli [command]"
        )  # pragma: no mutate
        print("Available commands: sync-companies")  # pragma: no mutate
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        await _run_sync_companies()
    else:
        print(f"Unknown command: {cmd}")  # pragma: no mutate
        sys.exit(None)


async def x_main__mutmut_9():
    if len(sys.argv) < 2:
        print(
            "Usage: python -m src.shared.presentation.cli [command]"
        )  # pragma: no mutate
        print("Available commands: sync-companies")  # pragma: no mutate
        return

    cmd = sys.argv[1]
    if cmd == "sync-companies":
        await _run_sync_companies()
    else:
        print(f"Unknown command: {cmd}")  # pragma: no mutate
        sys.exit(2)


x_main__mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
    "x_main__mutmut_1": x_main__mutmut_1,
    "x_main__mutmut_2": x_main__mutmut_2,
    "x_main__mutmut_3": x_main__mutmut_3,
    "x_main__mutmut_4": x_main__mutmut_4,
    "x_main__mutmut_5": x_main__mutmut_5,
    "x_main__mutmut_6": x_main__mutmut_6,
    "x_main__mutmut_7": x_main__mutmut_7,
    "x_main__mutmut_8": x_main__mutmut_8,
    "x_main__mutmut_9": x_main__mutmut_9,
}
x_main__mutmut_orig.__name__ = "x_main"


if __name__ == "__main__":
    asyncio.run(main())
