import json
from typing import Dict, Any
from companies.domain.entities.company import Company
from companies.domain.value_objects.cnpj import CNPJ
from companies.infrastructure.adapters.database.models import CompanyModel
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore

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
            has_bdr=entity.has_bdr
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
            has_bdr=model.has_bdr
        )

    @staticmethod
    def to_persistence_dict(entity: Company) -> Dict[str, Any]:
        """
        Gera um dicionário puro para persistência, eliminando metadados do ORM.
        """
        model = CompanyDataMapper.to_model(entity)
        # Extrai apenas as colunas declaradas no SQLAlchemy (ignorando ID auto-incremental)
        return {
            c.name: getattr(model, c.name) 
            for c in CompanyModel.__table__.columns 
            if c.name != 'id'
        }
