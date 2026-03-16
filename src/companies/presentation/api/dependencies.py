from fastapi import Depends
from sqlalchemy.orm import Session
from shared.infrastructure.database.connection import get_db
from companies.infrastructure.adapters.database.postgres_company_repository import (
    PostgresCompanyRepository,
)
from companies.infrastructure.adapters.data_sources.playwright_b3_data_source import (
    PlaywrightB3DataSource,
)
from companies.application.use_cases.sync_b3_companies import SyncB3CompaniesUseCase
from shared.domain.ports.telemetry_port import TelemetryPort
from shared.infrastructure.adapters.prometheus_telemetry import (
    PrometheusTelemetryAdapter,
)
from shared.domain.ports.job_queue_port import JobQueuePort
from shared.infrastructure.adapters.arq_job_queue import ArqJobQueueAdapter
from companies.application.use_cases.trigger_b3_sync import TriggerB3SyncUseCase

def get_telemetry_port() -> TelemetryPort:
    """Dependency Provider for TelemetryPort"""
    return PrometheusTelemetryAdapter()


def get_company_repository(db: Session = Depends(get_db)) -> PostgresCompanyRepository:
    """Dependency Provider for CompanyRepository Port"""
    return PostgresCompanyRepository(session=db)


def get_b3_data_source(
    telemetry: TelemetryPort = Depends(get_telemetry_port),
) -> PlaywrightB3DataSource:
    """Dependency Provider for B3DataSource Port. Default headless mode from settings."""
    return PlaywrightB3DataSource(telemetry=telemetry)


def get_sync_b3_companies_use_case(
    data_source: PlaywrightB3DataSource = Depends(get_b3_data_source),
    repository: PostgresCompanyRepository = Depends(get_company_repository),
    telemetry: TelemetryPort = Depends(get_telemetry_port),
) -> SyncB3CompaniesUseCase:
    """Dependency Provider for the Sync Use Case"""
    return SyncB3CompaniesUseCase(
        data_source=data_source, repository=repository, telemetry=telemetry
    )


def get_job_queue_port() -> JobQueuePort:
    """Dependency Provider for the primary Job Queue Port."""
    return ArqJobQueueAdapter()


def get_trigger_b3_sync_use_case(
    job_queue: JobQueuePort = Depends(get_job_queue_port),
    telemetry: TelemetryPort = Depends(get_telemetry_port),
) -> TriggerB3SyncUseCase:
    """Dependency Provider for triggering B3 background syncs."""
    return TriggerB3SyncUseCase(job_queue=job_queue, telemetry=telemetry)
