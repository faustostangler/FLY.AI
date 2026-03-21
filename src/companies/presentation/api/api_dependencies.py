from fastapi import Depends
from sqlalchemy.orm import Session

from shared.infrastructure.database.connection import get_db
from companies.infrastructure.adapters.database.postgres_company_repository import (
    PostgresCompanyRepository,
)
from shared.domain.ports.telemetry_port import TelemetryPort
from shared.infrastructure.adapters.prometheus_telemetry import (
    PrometheusTelemetryAdapter,
)
from shared.domain.ports.job_queue_port import JobQueuePort
from shared.infrastructure.adapters.arq_job_queue import ArqJobQueueAdapter
from companies.application.use_cases.trigger_b3_sync import TriggerB3SyncUseCase

def get_telemetry_port() -> TelemetryPort:
    """Dependency Provider for TelemetryPort. Lightweight."""
    return PrometheusTelemetryAdapter()

def get_job_queue_port() -> JobQueuePort:
    """Dependency Provider for the primary Job Queue Port. Lightweight."""
    return ArqJobQueueAdapter()

def get_company_repository(db: Session = Depends(get_db)) -> PostgresCompanyRepository:
    """Dependency Provider for CompanyRepository Port."""
    return PostgresCompanyRepository(session=db)

def get_trigger_b3_sync_use_case(
    job_queue: JobQueuePort = Depends(get_job_queue_port),
    telemetry: TelemetryPort = Depends(get_telemetry_port),
) -> TriggerB3SyncUseCase:
    """Dependency Provider for triggering B3 background syncs. 
    API-safe as it doesn't pull in heavy binaries like Playwright.
    """
    return TriggerB3SyncUseCase(job_queue=job_queue, telemetry=telemetry)
