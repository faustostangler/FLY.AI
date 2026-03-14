from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert

from companies.domain.entities.company import Company
from companies.domain.ports.company_repository import CompanyRepository
from companies.infrastructure.adapters.database.models import CompanyModel
from companies.infrastructure.adapters.database.mapper import CompanyDataMapper

class PostgresCompanyRepository(CompanyRepository):
    """
    SOTA Implementation: 100% focused on I/O and optimized SQL queries.
    Uses Data Mapper to isolate domain/infrastructure translation.
    """
    def __init__(self, session: Session):
        self._session = session

    def save(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        data = CompanyDataMapper.to_persistence_dict(company)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def save_batch(self, companies: List[Company]) -> None:
        """
        Saves or updates companies in batch using PostgreSQL native UPSERT.
        Optimized via Data Mapper for clean persistence dictionaries.
        """
        if not companies:
            return
            
        data_list = [CompanyDataMapper.to_persistence_dict(company) for company in companies]
        
        # Standard PostgreSQL UPSERT logic
        stmt = insert(CompanyModel).values(data_list)
        
        # Define what to update on conflict
        update_cols = {
            c.name: stmt.excluded[c.name] 
            for c in CompanyModel.__table__.columns 
            if c.name not in ['id', 'ticker']
        }
        
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_=update_cols
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def get_by_ticker(self, ticker: str) -> Optional[Company]:
        """Fetches a company by ticker and maps it to a Domain Entity."""
        model = self._session.query(CompanyModel).filter(CompanyModel.ticker == ticker).first()
        return CompanyDataMapper.to_entity(model) if model else None

    def get_all(self) -> List[Company]:
        """Fetches all companies and maps them to Domain Entities."""
        models = self._session.query(CompanyModel).all()
        return [CompanyDataMapper.to_entity(m) for m in models]
