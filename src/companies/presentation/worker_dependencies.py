from sqlalchemy.ext.asyncio import AsyncSession
from shared.infrastructure.database.connection import AsyncSessionLocal
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

def get_telemetry_port() -> TelemetryPort:
    """Dependency Provider for TelemetryPort"""
    return PrometheusTelemetryAdapter()

def get_company_repository(db: AsyncSession) -> PostgresCompanyRepository:
    """Dependency Provider for CompanyRepository Port"""
    return PostgresCompanyRepository(session=db)

def get_b3_data_source(
    telemetry: TelemetryPort,
) -> PlaywrightB3DataSource:
    """Dependency Provider for B3DataSource Port. Heavyweight dependencies reside here."""
    return PlaywrightB3DataSource(telemetry=telemetry)

def get_sync_b3_companies_use_case(
    db_session: AsyncSession
) -> SyncB3CompaniesUseCase:
    """Dependency Provider for the heavy Sync Use Case (Worker Only)."""
    telemetry = get_telemetry_port()
    repository = get_company_repository(db_session)
    data_source = get_b3_data_source(telemetry)
    
    return SyncB3CompaniesUseCase(
        data_source=data_source, 
        repository=repository, 
        telemetry=telemetry
    )
