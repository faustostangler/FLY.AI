from typing import List, Optional
from sqlalchemy.orm import Session
from companies.domain.entities.company import Company
from companies.domain.ports.company_repository import CompanyRepository
from companies.infrastructure.adapters.database.models import CompanyModel

class PostgresCompanyRepository(CompanyRepository):
    """
    SQLAlchemy-based concrete implementation of CompanyRepository.
    Designed for PostgreSQL interactions.
    """
    def __init__(self, session: Session):
        self._session = session
        
    def _to_model(self, entity: Company) -> CompanyModel:
        """Map Domain Entity to SQLAlchemy Model"""
        return CompanyModel(
            ticker=entity.ticker,
            cvm_code=entity.cvm_code,
            company_name=entity.company_name,
            trading_name=entity.trading_name,
            cnpj=entity.cnpj.root if entity.cnpj else None,
            listing=entity.listing,
            sector=entity.sector,
            subsector=entity.subsector,
            segment=entity.segment,
            segment_eng=entity.segment_eng,
            activity=entity.activity,
            describle_category_bvmf=entity.describle_category_bvmf,
            date_listing=entity.date_listing,
            last_date=entity.last_date,
            date_quotation=entity.date_quotation,
            website=entity.website,
            registrar=entity.registrar,
            main_registrar=entity.main_registrar,
            status=entity.status,
            type=entity.type,
            market_indicator=entity.market_indicator,
            ticker_codes=entity.ticker_codes,
            isin_codes=entity.isin_codes,
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )

    def _to_entity(self, model: CompanyModel) -> Company:
        """Map SQLAlchemy Model back to Domain Entity"""
        return Company(
            ticker=model.ticker,
            cvm_code=model.cvm_code,
            company_name=model.company_name,
            trading_name=model.trading_name,
            cnpj=model.cnpj,
            listing=model.listing,
            sector=model.sector,
            subsector=model.subsector,
            segment=model.segment,
            segment_eng=model.segment_eng,
            activity=model.activity,
            describle_category_bvmf=model.describle_category_bvmf,
            date_listing=model.date_listing,
            last_date=model.last_date,
            date_quotation=model.date_quotation,
            website=model.website,
            registrar=model.registrar,
            main_registrar=model.main_registrar,
            status=model.status,
            type=model.type,
            market_indicator=model.market_indicator,
            ticker_codes=model.ticker_codes,
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def save(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', None)
        data.pop('id', None)
        
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
        This prevents 'Duplicate Key' errors and improves performance.
        """
        if not companies:
            return
            
        from sqlalchemy.dialects.postgresql import insert
        
        # Prepare data for bulk insert
        data_list = []
        for company in companies:
            data = self._to_model(company).__dict__
            data.pop('_sa_instance_state', None)
            data.pop('id', None)
            data_list.append(data)
            
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
        model = self._session.query(CompanyModel).filter(CompanyModel.ticker == ticker).first()
        if model:
            return self._to_entity(model)
        return None

    def get_all(self) -> List[Company]:
        models = self._session.query(CompanyModel).all()
        return [self._to_entity(m) for m in models]
