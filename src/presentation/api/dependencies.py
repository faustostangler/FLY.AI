from fastapi import Depends
from sqlalchemy.orm import Session
from infrastructure.database.connection import get_db
from infrastructure.adapters.database.postgres_company_repository import PostgresCompanyRepository
from infrastructure.adapters.scrapers.playwright_b3_scraper import PlaywrightB3Scraper
from application.use_cases.sync_b3_companies import SyncB3CompaniesUseCase

def get_company_repository(db: Session = Depends(get_db)) -> PostgresCompanyRepository:
    """Dependency Provider for CompanyRepository Port"""
    return PostgresCompanyRepository(session=db)

def get_b3_scraper() -> PlaywrightB3Scraper:
    """Dependency Provider for B3Scraper Port. Uses headless by default."""
    return PlaywrightB3Scraper(headless=True)

def get_sync_b3_companies_use_case(
    scraper: PlaywrightB3Scraper = Depends(get_b3_scraper),
    repository: PostgresCompanyRepository = Depends(get_company_repository)
) -> SyncB3CompaniesUseCase:
    """Dependency Provider for the Sync Use Case"""
    return SyncB3CompaniesUseCase(scraper=scraper, repository=repository)
