from fastapi import Depends
from sqlalchemy.orm import Session
from shared.infrastructure.database.connection import get_db
from companies.infrastructure.adapters.database.postgres_company_repository import PostgresCompanyRepository
from companies.infrastructure.adapters.data_sources.playwright_b3_data_source import PlaywrightB3DataSource
from companies.application.use_cases.sync_b3_companies import SyncB3CompaniesUseCase

def get_company_repository(db: Session = Depends(get_db)) -> PostgresCompanyRepository:
    """Dependency Provider for CompanyRepository Port"""
    return PostgresCompanyRepository(session=db)

def get_b3_data_source() -> PlaywrightB3DataSource:
    """Dependency Provider for B3DataSource Port. Uses headless by default."""
    return PlaywrightB3DataSource(headless=True)

def get_sync_b3_companies_use_case(
    data_source: PlaywrightB3DataSource = Depends(get_b3_data_source),
    repository: PostgresCompanyRepository = Depends(get_company_repository)
) -> SyncB3CompaniesUseCase:
    """Dependency Provider for the Sync Use Case"""
    return SyncB3CompaniesUseCase(data_source=data_source, repository=repository)
