from typing import List, Optional
from sqlalchemy.orm import Session
from domain.entities.company import Company
from domain.ports.repositories.company_repository import CompanyRepository
from infrastructure.database.models import CompanyModel

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
            cnpj=entity.cnpj,
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
        model = self._to_model(company)
        # Using merge instead of add to gracefully handle upserts if primary key or unique exists
        self._session.merge(model)
        self._session.commit()

    def save_batch(self, companies: List[Company]) -> None:
        models = [self._to_model(c) for c in companies]
        # In SQLAlchemy 2.0, bulk save is handled best with add_all and commit
        self._session.add_all(models) 
        self._session.commit()

    def get_by_ticker(self, ticker: str) -> Optional[Company]:
        model = self._session.query(CompanyModel).filter(CompanyModel.ticker == ticker).first()
        if model:
            return self._to_entity(model)
        return None

    def get_all(self) -> List[Company]:
        models = self._session.query(CompanyModel).all()
        return [self._to_entity(m) for m in models]
