from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert

from companies.domain.entities.company import Company
from companies.domain.ports.company_repository import CompanyRepository
from companies.infrastructure.adapters.database.models import CompanyModel
from companies.infrastructure.adapters.database.mapper import CompanyDataMapper

class PostgresCompanyRepository(CompanyRepository):
    """PostgreSQL implementation of the CompanyRepository port.

    This adapter provides high-performance persistence using native 
    PostgreSQL features (UPSERT) while keeping the Domain decoupled from 
    relational schemas through the use of Data Mappers.

    Attributes:
        session (Session): An active SQLAlchemy session for transaction management.
    """
    def __init__(self, session: Session):
        self._session = session

    def save(self, company: Company) -> None:
        """Persists or updates an issuer using an atomic UPSERT operation.

        Relying on native 'ON CONFLICT' clauses ensures atomicity and 
        prevents race conditions during concurrent updates of the same ticker.

        Args:
            company (Company): The domain entity to be persisted.
        """
        data = CompanyDataMapper.to_persistence_dict(company)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def save_batch(self, companies: List[Company]) -> None:
        """Executes a bulk UPSERT for a collection of issuers.

        During full-market synchronizations, individual inserts are 
        prohibitively slow. Native batch UPSERTs reduce I/O wait times 
        by orders of magnitude.

        Args:
            companies (List[Company]): A sequence of domain entities.
        """
        if not companies:
            return
            
        # Transform domain entities into flat dictionaries compatible with the ORM.
        data_list = [CompanyDataMapper.to_persistence_dict(company) for company in companies]
        
        # Standard PostgreSQL UPSERT logic (ON CONFLICT DO UPDATE).
        stmt = insert(CompanyModel).values(data_list)
        
        # Calculate update columns dynamically from the model definition.
        # This automatically handles schema changes without requiring 
        # manual updates to the repository logic.
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
        """Retrieves an issuer by its primary symbol.

        Args:
            ticker (str): The ticker symbol to search for.

        Returns:
            Optional[Company]: A reconstructed domain entity or None.
        """
        model = self._session.query(CompanyModel).filter(CompanyModel.ticker == ticker).first()
        return CompanyDataMapper.to_entity(model) if model else None

    def get_all(self) -> List[Company]:
        """Loads all issuer records from the database.

        Used primarily for populating caches or during full-system audits.

        Returns:
            List[Company]: A list of hydrated domain entities.
        """
        models = self._session.query(CompanyModel).all()
        return [CompanyDataMapper.to_entity(m) for m in models]
