import json
from typing import Dict, Any
from companies.domain.entities.company import Company
from companies.domain.value_objects.cnpj import CNPJ
from companies.infrastructure.adapters.database.models import CompanyModel


class CompanyDataMapper:
    """
    Data Mapper SOTA: Isola completamente a conversão bidirecional entre
    Entidades de Domínio (Python puro) e Modelos de Infraestrutura (SQLAlchemy).
    """

    @staticmethod
    def to_model(entity: Company) -> CompanyModel:
        """Converts a Domain Entity to a SQLAlchemy Model."""
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
            ticker_codes=json.dumps(entity.ticker_codes),
            isin_codes=json.dumps(entity.isin_codes),
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr,
        )

    @staticmethod
    def to_entity(model: CompanyModel) -> Company:
        """Converts a SQLAlchemy Model to a Domain Entity."""
        try:
            ticker_codes = json.loads(model.ticker_codes) if model.ticker_codes else []
        except (json.JSONDecodeError, TypeError):
            ticker_codes = []

        try:
            isin_codes = json.loads(model.isin_codes) if model.isin_codes else []
        except (json.JSONDecodeError, TypeError):
            isin_codes = []

        return Company(
            ticker=model.ticker,
            cvm_code=model.cvm_code,
            company_name=model.company_name,
            trading_name=model.trading_name,
            cnpj=CNPJ(model.cnpj) if model.cnpj else None,
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
            ticker_codes=ticker_codes,
            isin_codes=isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr,
        )

    @staticmethod
    def to_persistence_dict(entity: Company) -> Dict[str, Any]:
        """
        Gera um dicionário puro para persistência, eliminando metadados do ORM.
        """
        model = CompanyDataMapper.to_model(entity)
        # Extrai apenas as colunas declaradas no SQLAlchemy (ignorando ID e auditoria)
        exclude = ["id", "created_at", "updated_at", "ingested_at"]
        return {
            c.name: getattr(model, c.name)
            for c in CompanyModel.__table__.columns
            if c.name not in exclude
        }
