from typing import List, Optional
import json
from sqlalchemy.orm import Session
from companies.domain.entities.company import Company
from companies.domain.ports.company_repository import CompanyRepository
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

class PostgresCompanyRepository(CompanyRepository):
    """
    SQLAlchemy-based concrete implementation of CompanyRepository.
    Designed for PostgreSQL interactions.
    """
    def __init__(self, session: Session):
        args = [session]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPostgresCompanyRepositoryǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁPostgresCompanyRepositoryǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁPostgresCompanyRepositoryǁ__init____mutmut_orig(self, session: Session):
        self._session = session
        
    def xǁPostgresCompanyRepositoryǁ__init____mutmut_1(self, session: Session):
        self._session = None
        
    
    xǁPostgresCompanyRepositoryǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPostgresCompanyRepositoryǁ__init____mutmut_1': xǁPostgresCompanyRepositoryǁ__init____mutmut_1
    }
    xǁPostgresCompanyRepositoryǁ__init____mutmut_orig.__name__ = 'xǁPostgresCompanyRepositoryǁ__init__'
    def _to_model(self, entity: Company) -> CompanyModel:
        args = [entity]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_orig'), object.__getattribute__(self, 'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_mutants'), args, kwargs, self)
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_orig(self, entity: Company) -> CompanyModel:
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_1(self, entity: Company) -> CompanyModel:
        """Map Domain Entity to SQLAlchemy Model"""
        return CompanyModel(
            ticker=None,
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_2(self, entity: Company) -> CompanyModel:
        """Map Domain Entity to SQLAlchemy Model"""
        return CompanyModel(
            ticker=entity.ticker,
            cvm_code=None,
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_3(self, entity: Company) -> CompanyModel:
        """Map Domain Entity to SQLAlchemy Model"""
        return CompanyModel(
            ticker=entity.ticker,
            cvm_code=entity.cvm_code,
            company_name=None,
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_4(self, entity: Company) -> CompanyModel:
        """Map Domain Entity to SQLAlchemy Model"""
        return CompanyModel(
            ticker=entity.ticker,
            cvm_code=entity.cvm_code,
            company_name=entity.company_name,
            trading_name=None,
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_5(self, entity: Company) -> CompanyModel:
        """Map Domain Entity to SQLAlchemy Model"""
        return CompanyModel(
            ticker=entity.ticker,
            cvm_code=entity.cvm_code,
            company_name=entity.company_name,
            trading_name=entity.trading_name,
            cnpj=None,
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_6(self, entity: Company) -> CompanyModel:
        """Map Domain Entity to SQLAlchemy Model"""
        return CompanyModel(
            ticker=entity.ticker,
            cvm_code=entity.cvm_code,
            company_name=entity.company_name,
            trading_name=entity.trading_name,
            cnpj=entity.cnpj.root if entity.cnpj else None,
            listing=None,
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_7(self, entity: Company) -> CompanyModel:
        """Map Domain Entity to SQLAlchemy Model"""
        return CompanyModel(
            ticker=entity.ticker,
            cvm_code=entity.cvm_code,
            company_name=entity.company_name,
            trading_name=entity.trading_name,
            cnpj=entity.cnpj.root if entity.cnpj else None,
            listing=entity.listing,
            sector=None,
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_8(self, entity: Company) -> CompanyModel:
        """Map Domain Entity to SQLAlchemy Model"""
        return CompanyModel(
            ticker=entity.ticker,
            cvm_code=entity.cvm_code,
            company_name=entity.company_name,
            trading_name=entity.trading_name,
            cnpj=entity.cnpj.root if entity.cnpj else None,
            listing=entity.listing,
            sector=entity.sector,
            subsector=None,
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_9(self, entity: Company) -> CompanyModel:
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
            segment=None,
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_10(self, entity: Company) -> CompanyModel:
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
            segment_eng=None,
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_11(self, entity: Company) -> CompanyModel:
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
            activity=None,
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_12(self, entity: Company) -> CompanyModel:
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
            describle_category_bvmf=None,
            date_listing=entity.date_listing,
            last_date=entity.last_date,
            date_quotation=entity.date_quotation,
            website=entity.website,
            registrar=entity.registrar,
            main_registrar=entity.main_registrar,
            status=entity.status,
            type=entity.type,
            market_indicator=entity.market_indicator,
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_13(self, entity: Company) -> CompanyModel:
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
            date_listing=None,
            last_date=entity.last_date,
            date_quotation=entity.date_quotation,
            website=entity.website,
            registrar=entity.registrar,
            main_registrar=entity.main_registrar,
            status=entity.status,
            type=entity.type,
            market_indicator=entity.market_indicator,
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_14(self, entity: Company) -> CompanyModel:
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
            last_date=None,
            date_quotation=entity.date_quotation,
            website=entity.website,
            registrar=entity.registrar,
            main_registrar=entity.main_registrar,
            status=entity.status,
            type=entity.type,
            market_indicator=entity.market_indicator,
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_15(self, entity: Company) -> CompanyModel:
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
            date_quotation=None,
            website=entity.website,
            registrar=entity.registrar,
            main_registrar=entity.main_registrar,
            status=entity.status,
            type=entity.type,
            market_indicator=entity.market_indicator,
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_16(self, entity: Company) -> CompanyModel:
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
            website=None,
            registrar=entity.registrar,
            main_registrar=entity.main_registrar,
            status=entity.status,
            type=entity.type,
            market_indicator=entity.market_indicator,
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_17(self, entity: Company) -> CompanyModel:
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
            registrar=None,
            main_registrar=entity.main_registrar,
            status=entity.status,
            type=entity.type,
            market_indicator=entity.market_indicator,
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_18(self, entity: Company) -> CompanyModel:
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
            main_registrar=None,
            status=entity.status,
            type=entity.type,
            market_indicator=entity.market_indicator,
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_19(self, entity: Company) -> CompanyModel:
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
            status=None,
            type=entity.type,
            market_indicator=entity.market_indicator,
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_20(self, entity: Company) -> CompanyModel:
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
            type=None,
            market_indicator=entity.market_indicator,
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_21(self, entity: Company) -> CompanyModel:
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
            market_indicator=None,
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_22(self, entity: Company) -> CompanyModel:
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
            ticker_codes=None,
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_23(self, entity: Company) -> CompanyModel:
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=None,
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_24(self, entity: Company) -> CompanyModel:
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=None,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_25(self, entity: Company) -> CompanyModel:
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=None,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_26(self, entity: Company) -> CompanyModel:
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=None,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_27(self, entity: Company) -> CompanyModel:
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=None
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_28(self, entity: Company) -> CompanyModel:
        """Map Domain Entity to SQLAlchemy Model"""
        return CompanyModel(
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_29(self, entity: Company) -> CompanyModel:
        """Map Domain Entity to SQLAlchemy Model"""
        return CompanyModel(
            ticker=entity.ticker,
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_30(self, entity: Company) -> CompanyModel:
        """Map Domain Entity to SQLAlchemy Model"""
        return CompanyModel(
            ticker=entity.ticker,
            cvm_code=entity.cvm_code,
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_31(self, entity: Company) -> CompanyModel:
        """Map Domain Entity to SQLAlchemy Model"""
        return CompanyModel(
            ticker=entity.ticker,
            cvm_code=entity.cvm_code,
            company_name=entity.company_name,
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_32(self, entity: Company) -> CompanyModel:
        """Map Domain Entity to SQLAlchemy Model"""
        return CompanyModel(
            ticker=entity.ticker,
            cvm_code=entity.cvm_code,
            company_name=entity.company_name,
            trading_name=entity.trading_name,
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_33(self, entity: Company) -> CompanyModel:
        """Map Domain Entity to SQLAlchemy Model"""
        return CompanyModel(
            ticker=entity.ticker,
            cvm_code=entity.cvm_code,
            company_name=entity.company_name,
            trading_name=entity.trading_name,
            cnpj=entity.cnpj.root if entity.cnpj else None,
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_34(self, entity: Company) -> CompanyModel:
        """Map Domain Entity to SQLAlchemy Model"""
        return CompanyModel(
            ticker=entity.ticker,
            cvm_code=entity.cvm_code,
            company_name=entity.company_name,
            trading_name=entity.trading_name,
            cnpj=entity.cnpj.root if entity.cnpj else None,
            listing=entity.listing,
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_35(self, entity: Company) -> CompanyModel:
        """Map Domain Entity to SQLAlchemy Model"""
        return CompanyModel(
            ticker=entity.ticker,
            cvm_code=entity.cvm_code,
            company_name=entity.company_name,
            trading_name=entity.trading_name,
            cnpj=entity.cnpj.root if entity.cnpj else None,
            listing=entity.listing,
            sector=entity.sector,
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_36(self, entity: Company) -> CompanyModel:
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_37(self, entity: Company) -> CompanyModel:
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_38(self, entity: Company) -> CompanyModel:
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_39(self, entity: Company) -> CompanyModel:
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
            date_listing=entity.date_listing,
            last_date=entity.last_date,
            date_quotation=entity.date_quotation,
            website=entity.website,
            registrar=entity.registrar,
            main_registrar=entity.main_registrar,
            status=entity.status,
            type=entity.type,
            market_indicator=entity.market_indicator,
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_40(self, entity: Company) -> CompanyModel:
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
            last_date=entity.last_date,
            date_quotation=entity.date_quotation,
            website=entity.website,
            registrar=entity.registrar,
            main_registrar=entity.main_registrar,
            status=entity.status,
            type=entity.type,
            market_indicator=entity.market_indicator,
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_41(self, entity: Company) -> CompanyModel:
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
            date_quotation=entity.date_quotation,
            website=entity.website,
            registrar=entity.registrar,
            main_registrar=entity.main_registrar,
            status=entity.status,
            type=entity.type,
            market_indicator=entity.market_indicator,
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_42(self, entity: Company) -> CompanyModel:
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
            website=entity.website,
            registrar=entity.registrar,
            main_registrar=entity.main_registrar,
            status=entity.status,
            type=entity.type,
            market_indicator=entity.market_indicator,
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_43(self, entity: Company) -> CompanyModel:
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
            registrar=entity.registrar,
            main_registrar=entity.main_registrar,
            status=entity.status,
            type=entity.type,
            market_indicator=entity.market_indicator,
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_44(self, entity: Company) -> CompanyModel:
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
            main_registrar=entity.main_registrar,
            status=entity.status,
            type=entity.type,
            market_indicator=entity.market_indicator,
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_45(self, entity: Company) -> CompanyModel:
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
            status=entity.status,
            type=entity.type,
            market_indicator=entity.market_indicator,
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_46(self, entity: Company) -> CompanyModel:
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
            type=entity.type,
            market_indicator=entity.market_indicator,
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_47(self, entity: Company) -> CompanyModel:
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
            market_indicator=entity.market_indicator,
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_48(self, entity: Company) -> CompanyModel:
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_49(self, entity: Company) -> CompanyModel:
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
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_50(self, entity: Company) -> CompanyModel:
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_51(self, entity: Company) -> CompanyModel:
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_52(self, entity: Company) -> CompanyModel:
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_53(self, entity: Company) -> CompanyModel:
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_54(self, entity: Company) -> CompanyModel:
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_55(self, entity: Company) -> CompanyModel:
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
            ticker_codes=json.dumps(None) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_56(self, entity: Company) -> CompanyModel:
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "XX[]XX",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_57(self, entity: Company) -> CompanyModel:
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(None) if entity.isin_codes else "[]",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    def xǁPostgresCompanyRepositoryǁ_to_model__mutmut_58(self, entity: Company) -> CompanyModel:
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
            ticker_codes=json.dumps(entity.ticker_codes) if entity.ticker_codes else "[]",
            isin_codes=json.dumps(entity.isin_codes) if entity.isin_codes else "XX[]XX",
            type_bdr=entity.type_bdr,
            has_quotation=entity.has_quotation,
            has_emissions=entity.has_emissions,
            has_bdr=entity.has_bdr
        )
    
    xǁPostgresCompanyRepositoryǁ_to_model__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_1': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_1, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_2': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_2, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_3': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_3, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_4': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_4, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_5': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_5, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_6': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_6, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_7': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_7, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_8': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_8, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_9': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_9, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_10': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_10, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_11': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_11, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_12': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_12, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_13': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_13, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_14': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_14, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_15': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_15, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_16': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_16, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_17': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_17, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_18': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_18, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_19': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_19, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_20': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_20, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_21': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_21, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_22': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_22, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_23': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_23, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_24': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_24, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_25': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_25, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_26': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_26, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_27': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_27, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_28': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_28, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_29': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_29, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_30': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_30, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_31': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_31, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_32': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_32, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_33': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_33, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_34': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_34, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_35': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_35, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_36': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_36, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_37': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_37, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_38': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_38, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_39': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_39, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_40': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_40, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_41': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_41, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_42': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_42, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_43': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_43, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_44': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_44, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_45': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_45, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_46': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_46, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_47': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_47, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_48': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_48, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_49': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_49, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_50': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_50, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_51': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_51, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_52': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_52, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_53': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_53, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_54': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_54, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_55': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_55, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_56': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_56, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_57': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_57, 
        'xǁPostgresCompanyRepositoryǁ_to_model__mutmut_58': xǁPostgresCompanyRepositoryǁ_to_model__mutmut_58
    }
    xǁPostgresCompanyRepositoryǁ_to_model__mutmut_orig.__name__ = 'xǁPostgresCompanyRepositoryǁ_to_model'

    def _to_entity(self, model: CompanyModel) -> Company:
        args = [model]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_orig'), object.__getattribute__(self, 'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_mutants'), args, kwargs, self)

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_orig(self, model: CompanyModel) -> Company:
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_1(self, model: CompanyModel) -> Company:
        """Map SQLAlchemy Model back to Domain Entity"""
        return Company(
            ticker=None,
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_2(self, model: CompanyModel) -> Company:
        """Map SQLAlchemy Model back to Domain Entity"""
        return Company(
            ticker=model.ticker,
            cvm_code=None,
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_3(self, model: CompanyModel) -> Company:
        """Map SQLAlchemy Model back to Domain Entity"""
        return Company(
            ticker=model.ticker,
            cvm_code=model.cvm_code,
            company_name=None,
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_4(self, model: CompanyModel) -> Company:
        """Map SQLAlchemy Model back to Domain Entity"""
        return Company(
            ticker=model.ticker,
            cvm_code=model.cvm_code,
            company_name=model.company_name,
            trading_name=None,
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_5(self, model: CompanyModel) -> Company:
        """Map SQLAlchemy Model back to Domain Entity"""
        return Company(
            ticker=model.ticker,
            cvm_code=model.cvm_code,
            company_name=model.company_name,
            trading_name=model.trading_name,
            cnpj=None,
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_6(self, model: CompanyModel) -> Company:
        """Map SQLAlchemy Model back to Domain Entity"""
        return Company(
            ticker=model.ticker,
            cvm_code=model.cvm_code,
            company_name=model.company_name,
            trading_name=model.trading_name,
            cnpj=model.cnpj,
            listing=None,
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_7(self, model: CompanyModel) -> Company:
        """Map SQLAlchemy Model back to Domain Entity"""
        return Company(
            ticker=model.ticker,
            cvm_code=model.cvm_code,
            company_name=model.company_name,
            trading_name=model.trading_name,
            cnpj=model.cnpj,
            listing=model.listing,
            sector=None,
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_8(self, model: CompanyModel) -> Company:
        """Map SQLAlchemy Model back to Domain Entity"""
        return Company(
            ticker=model.ticker,
            cvm_code=model.cvm_code,
            company_name=model.company_name,
            trading_name=model.trading_name,
            cnpj=model.cnpj,
            listing=model.listing,
            sector=model.sector,
            subsector=None,
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_9(self, model: CompanyModel) -> Company:
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
            segment=None,
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_10(self, model: CompanyModel) -> Company:
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
            segment_eng=None,
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_11(self, model: CompanyModel) -> Company:
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
            activity=None,
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_12(self, model: CompanyModel) -> Company:
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
            describle_category_bvmf=None,
            date_listing=model.date_listing,
            last_date=model.last_date,
            date_quotation=model.date_quotation,
            website=model.website,
            registrar=model.registrar,
            main_registrar=model.main_registrar,
            status=model.status,
            type=model.type,
            market_indicator=model.market_indicator,
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_13(self, model: CompanyModel) -> Company:
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
            date_listing=None,
            last_date=model.last_date,
            date_quotation=model.date_quotation,
            website=model.website,
            registrar=model.registrar,
            main_registrar=model.main_registrar,
            status=model.status,
            type=model.type,
            market_indicator=model.market_indicator,
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_14(self, model: CompanyModel) -> Company:
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
            last_date=None,
            date_quotation=model.date_quotation,
            website=model.website,
            registrar=model.registrar,
            main_registrar=model.main_registrar,
            status=model.status,
            type=model.type,
            market_indicator=model.market_indicator,
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_15(self, model: CompanyModel) -> Company:
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
            date_quotation=None,
            website=model.website,
            registrar=model.registrar,
            main_registrar=model.main_registrar,
            status=model.status,
            type=model.type,
            market_indicator=model.market_indicator,
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_16(self, model: CompanyModel) -> Company:
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
            website=None,
            registrar=model.registrar,
            main_registrar=model.main_registrar,
            status=model.status,
            type=model.type,
            market_indicator=model.market_indicator,
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_17(self, model: CompanyModel) -> Company:
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
            registrar=None,
            main_registrar=model.main_registrar,
            status=model.status,
            type=model.type,
            market_indicator=model.market_indicator,
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_18(self, model: CompanyModel) -> Company:
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
            main_registrar=None,
            status=model.status,
            type=model.type,
            market_indicator=model.market_indicator,
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_19(self, model: CompanyModel) -> Company:
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
            status=None,
            type=model.type,
            market_indicator=model.market_indicator,
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_20(self, model: CompanyModel) -> Company:
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
            type=None,
            market_indicator=model.market_indicator,
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_21(self, model: CompanyModel) -> Company:
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
            market_indicator=None,
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_22(self, model: CompanyModel) -> Company:
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
            ticker_codes=None, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_23(self, model: CompanyModel) -> Company:
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=None,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_24(self, model: CompanyModel) -> Company:
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=None,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_25(self, model: CompanyModel) -> Company:
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=None,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_26(self, model: CompanyModel) -> Company:
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=None,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_27(self, model: CompanyModel) -> Company:
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=None
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_28(self, model: CompanyModel) -> Company:
        """Map SQLAlchemy Model back to Domain Entity"""
        return Company(
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_29(self, model: CompanyModel) -> Company:
        """Map SQLAlchemy Model back to Domain Entity"""
        return Company(
            ticker=model.ticker,
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_30(self, model: CompanyModel) -> Company:
        """Map SQLAlchemy Model back to Domain Entity"""
        return Company(
            ticker=model.ticker,
            cvm_code=model.cvm_code,
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_31(self, model: CompanyModel) -> Company:
        """Map SQLAlchemy Model back to Domain Entity"""
        return Company(
            ticker=model.ticker,
            cvm_code=model.cvm_code,
            company_name=model.company_name,
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_32(self, model: CompanyModel) -> Company:
        """Map SQLAlchemy Model back to Domain Entity"""
        return Company(
            ticker=model.ticker,
            cvm_code=model.cvm_code,
            company_name=model.company_name,
            trading_name=model.trading_name,
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_33(self, model: CompanyModel) -> Company:
        """Map SQLAlchemy Model back to Domain Entity"""
        return Company(
            ticker=model.ticker,
            cvm_code=model.cvm_code,
            company_name=model.company_name,
            trading_name=model.trading_name,
            cnpj=model.cnpj,
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_34(self, model: CompanyModel) -> Company:
        """Map SQLAlchemy Model back to Domain Entity"""
        return Company(
            ticker=model.ticker,
            cvm_code=model.cvm_code,
            company_name=model.company_name,
            trading_name=model.trading_name,
            cnpj=model.cnpj,
            listing=model.listing,
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_35(self, model: CompanyModel) -> Company:
        """Map SQLAlchemy Model back to Domain Entity"""
        return Company(
            ticker=model.ticker,
            cvm_code=model.cvm_code,
            company_name=model.company_name,
            trading_name=model.trading_name,
            cnpj=model.cnpj,
            listing=model.listing,
            sector=model.sector,
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_36(self, model: CompanyModel) -> Company:
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_37(self, model: CompanyModel) -> Company:
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_38(self, model: CompanyModel) -> Company:
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_39(self, model: CompanyModel) -> Company:
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
            date_listing=model.date_listing,
            last_date=model.last_date,
            date_quotation=model.date_quotation,
            website=model.website,
            registrar=model.registrar,
            main_registrar=model.main_registrar,
            status=model.status,
            type=model.type,
            market_indicator=model.market_indicator,
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_40(self, model: CompanyModel) -> Company:
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
            last_date=model.last_date,
            date_quotation=model.date_quotation,
            website=model.website,
            registrar=model.registrar,
            main_registrar=model.main_registrar,
            status=model.status,
            type=model.type,
            market_indicator=model.market_indicator,
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_41(self, model: CompanyModel) -> Company:
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
            date_quotation=model.date_quotation,
            website=model.website,
            registrar=model.registrar,
            main_registrar=model.main_registrar,
            status=model.status,
            type=model.type,
            market_indicator=model.market_indicator,
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_42(self, model: CompanyModel) -> Company:
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
            website=model.website,
            registrar=model.registrar,
            main_registrar=model.main_registrar,
            status=model.status,
            type=model.type,
            market_indicator=model.market_indicator,
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_43(self, model: CompanyModel) -> Company:
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
            registrar=model.registrar,
            main_registrar=model.main_registrar,
            status=model.status,
            type=model.type,
            market_indicator=model.market_indicator,
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_44(self, model: CompanyModel) -> Company:
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
            main_registrar=model.main_registrar,
            status=model.status,
            type=model.type,
            market_indicator=model.market_indicator,
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_45(self, model: CompanyModel) -> Company:
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
            status=model.status,
            type=model.type,
            market_indicator=model.market_indicator,
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_46(self, model: CompanyModel) -> Company:
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
            type=model.type,
            market_indicator=model.market_indicator,
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_47(self, model: CompanyModel) -> Company:
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
            market_indicator=model.market_indicator,
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_48(self, model: CompanyModel) -> Company:
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_49(self, model: CompanyModel) -> Company:
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
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_50(self, model: CompanyModel) -> Company:
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_51(self, model: CompanyModel) -> Company:
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_52(self, model: CompanyModel) -> Company:
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_emissions=model.has_emissions,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_53(self, model: CompanyModel) -> Company:
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_bdr=model.has_bdr
        )

    def xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_54(self, model: CompanyModel) -> Company:
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
            ticker_codes=model.ticker_codes, # Entity validator handles JSON string to List conversion
            isin_codes=model.isin_codes,
            type_bdr=model.type_bdr,
            has_quotation=model.has_quotation,
            has_emissions=model.has_emissions,
            )
    
    xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_1': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_1, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_2': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_2, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_3': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_3, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_4': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_4, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_5': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_5, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_6': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_6, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_7': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_7, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_8': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_8, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_9': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_9, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_10': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_10, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_11': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_11, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_12': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_12, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_13': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_13, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_14': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_14, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_15': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_15, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_16': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_16, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_17': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_17, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_18': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_18, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_19': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_19, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_20': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_20, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_21': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_21, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_22': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_22, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_23': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_23, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_24': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_24, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_25': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_25, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_26': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_26, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_27': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_27, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_28': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_28, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_29': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_29, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_30': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_30, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_31': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_31, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_32': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_32, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_33': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_33, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_34': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_34, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_35': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_35, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_36': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_36, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_37': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_37, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_38': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_38, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_39': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_39, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_40': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_40, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_41': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_41, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_42': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_42, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_43': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_43, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_44': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_44, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_45': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_45, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_46': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_46, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_47': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_47, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_48': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_48, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_49': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_49, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_50': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_50, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_51': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_51, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_52': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_52, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_53': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_53, 
        'xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_54': xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_54
    }
    xǁPostgresCompanyRepositoryǁ_to_entity__mutmut_orig.__name__ = 'xǁPostgresCompanyRepositoryǁ_to_entity'

    def save(self, company: Company) -> None:
        args = [company]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPostgresCompanyRepositoryǁsave__mutmut_orig'), object.__getattribute__(self, 'xǁPostgresCompanyRepositoryǁsave__mutmut_mutants'), args, kwargs, self)

    def xǁPostgresCompanyRepositoryǁsave__mutmut_orig(self, company: Company) -> None:
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

    def xǁPostgresCompanyRepositoryǁsave__mutmut_1(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = None
        data.pop('_sa_instance_state', None)
        data.pop('id', None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_2(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(None).__dict__
        data.pop('_sa_instance_state', None)
        data.pop('id', None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_3(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop(None, None)
        data.pop('id', None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_4(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop(None)
        data.pop('id', None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_5(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', )
        data.pop('id', None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_6(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('XX_sa_instance_stateXX', None)
        data.pop('id', None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_7(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_SA_INSTANCE_STATE', None)
        data.pop('id', None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_8(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', None)
        data.pop(None, None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_9(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', None)
        data.pop(None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_10(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', None)
        data.pop('id', )
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_11(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', None)
        data.pop('XXidXX', None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_12(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', None)
        data.pop('ID', None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_13(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', None)
        data.pop('id', None)
        
        stmt = None
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_14(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', None)
        data.pop('id', None)
        
        stmt = insert(CompanyModel).values(None)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_15(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', None)
        data.pop('id', None)
        
        stmt = insert(None).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_16(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', None)
        data.pop('id', None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = None
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_17(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', None)
        data.pop('id', None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=None,
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_18(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', None)
        data.pop('id', None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_=None
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_19(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', None)
        data.pop('id', None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_20(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', None)
        data.pop('id', None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_21(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', None)
        data.pop('id', None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['XXtickerXX'],
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_22(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', None)
        data.pop('id', None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['TICKER'],
            set_={k: v for k, v in data.items() if k != 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_23(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', None)
        data.pop('id', None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k == 'ticker'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_24(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', None)
        data.pop('id', None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k != 'XXtickerXX'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_25(self, company: Company) -> None:
        """Saves or updates a single company using UPSERT."""
        from sqlalchemy.dialects.postgresql import insert
        
        data = self._to_model(company).__dict__
        data.pop('_sa_instance_state', None)
        data.pop('id', None)
        
        stmt = insert(CompanyModel).values(data)
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_={k: v for k, v in data.items() if k != 'TICKER'}
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave__mutmut_26(self, company: Company) -> None:
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
        
        self._session.execute(None)
        self._session.commit()
    
    xǁPostgresCompanyRepositoryǁsave__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPostgresCompanyRepositoryǁsave__mutmut_1': xǁPostgresCompanyRepositoryǁsave__mutmut_1, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_2': xǁPostgresCompanyRepositoryǁsave__mutmut_2, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_3': xǁPostgresCompanyRepositoryǁsave__mutmut_3, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_4': xǁPostgresCompanyRepositoryǁsave__mutmut_4, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_5': xǁPostgresCompanyRepositoryǁsave__mutmut_5, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_6': xǁPostgresCompanyRepositoryǁsave__mutmut_6, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_7': xǁPostgresCompanyRepositoryǁsave__mutmut_7, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_8': xǁPostgresCompanyRepositoryǁsave__mutmut_8, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_9': xǁPostgresCompanyRepositoryǁsave__mutmut_9, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_10': xǁPostgresCompanyRepositoryǁsave__mutmut_10, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_11': xǁPostgresCompanyRepositoryǁsave__mutmut_11, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_12': xǁPostgresCompanyRepositoryǁsave__mutmut_12, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_13': xǁPostgresCompanyRepositoryǁsave__mutmut_13, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_14': xǁPostgresCompanyRepositoryǁsave__mutmut_14, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_15': xǁPostgresCompanyRepositoryǁsave__mutmut_15, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_16': xǁPostgresCompanyRepositoryǁsave__mutmut_16, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_17': xǁPostgresCompanyRepositoryǁsave__mutmut_17, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_18': xǁPostgresCompanyRepositoryǁsave__mutmut_18, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_19': xǁPostgresCompanyRepositoryǁsave__mutmut_19, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_20': xǁPostgresCompanyRepositoryǁsave__mutmut_20, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_21': xǁPostgresCompanyRepositoryǁsave__mutmut_21, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_22': xǁPostgresCompanyRepositoryǁsave__mutmut_22, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_23': xǁPostgresCompanyRepositoryǁsave__mutmut_23, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_24': xǁPostgresCompanyRepositoryǁsave__mutmut_24, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_25': xǁPostgresCompanyRepositoryǁsave__mutmut_25, 
        'xǁPostgresCompanyRepositoryǁsave__mutmut_26': xǁPostgresCompanyRepositoryǁsave__mutmut_26
    }
    xǁPostgresCompanyRepositoryǁsave__mutmut_orig.__name__ = 'xǁPostgresCompanyRepositoryǁsave'

    def save_batch(self, companies: List[Company]) -> None:
        args = [companies]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_orig'), object.__getattribute__(self, 'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_mutants'), args, kwargs, self)

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_orig(self, companies: List[Company]) -> None:
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

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_1(self, companies: List[Company]) -> None:
        """
        Saves or updates companies in batch using PostgreSQL native UPSERT.
        This prevents 'Duplicate Key' errors and improves performance.
        """
        if companies:
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

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_2(self, companies: List[Company]) -> None:
        """
        Saves or updates companies in batch using PostgreSQL native UPSERT.
        This prevents 'Duplicate Key' errors and improves performance.
        """
        if not companies:
            return
            
        from sqlalchemy.dialects.postgresql import insert
        
        # Prepare data for bulk insert
        data_list = None
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

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_3(self, companies: List[Company]) -> None:
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
            data = None
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

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_4(self, companies: List[Company]) -> None:
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
            data = self._to_model(None).__dict__
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

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_5(self, companies: List[Company]) -> None:
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
            data.pop(None, None)
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

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_6(self, companies: List[Company]) -> None:
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
            data.pop(None)
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

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_7(self, companies: List[Company]) -> None:
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
            data.pop('_sa_instance_state', )
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

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_8(self, companies: List[Company]) -> None:
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
            data.pop('XX_sa_instance_stateXX', None)
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

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_9(self, companies: List[Company]) -> None:
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
            data.pop('_SA_INSTANCE_STATE', None)
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

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_10(self, companies: List[Company]) -> None:
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
            data.pop(None, None)
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

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_11(self, companies: List[Company]) -> None:
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
            data.pop(None)
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

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_12(self, companies: List[Company]) -> None:
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
            data.pop('id', )
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

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_13(self, companies: List[Company]) -> None:
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
            data.pop('XXidXX', None)
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

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_14(self, companies: List[Company]) -> None:
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
            data.pop('ID', None)
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

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_15(self, companies: List[Company]) -> None:
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
            data_list.append(None)
            
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

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_16(self, companies: List[Company]) -> None:
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
        stmt = None
        
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

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_17(self, companies: List[Company]) -> None:
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
        stmt = insert(CompanyModel).values(None)
        
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

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_18(self, companies: List[Company]) -> None:
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
        stmt = insert(None).values(data_list)
        
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

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_19(self, companies: List[Company]) -> None:
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
        update_cols = None
        
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_=update_cols
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_20(self, companies: List[Company]) -> None:
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
            if c.name in ['id', 'ticker']
        }
        
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_=update_cols
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_21(self, companies: List[Company]) -> None:
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
            if c.name not in ['XXidXX', 'ticker']
        }
        
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_=update_cols
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_22(self, companies: List[Company]) -> None:
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
            if c.name not in ['ID', 'ticker']
        }
        
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_=update_cols
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_23(self, companies: List[Company]) -> None:
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
            if c.name not in ['id', 'XXtickerXX']
        }
        
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_=update_cols
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_24(self, companies: List[Company]) -> None:
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
            if c.name not in ['id', 'TICKER']
        }
        
        stmt = stmt.on_conflict_do_update(
            index_elements=['ticker'],
            set_=update_cols
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_25(self, companies: List[Company]) -> None:
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
        
        stmt = None
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_26(self, companies: List[Company]) -> None:
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
            index_elements=None,
            set_=update_cols
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_27(self, companies: List[Company]) -> None:
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
            set_=None
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_28(self, companies: List[Company]) -> None:
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
            set_=update_cols
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_29(self, companies: List[Company]) -> None:
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
            )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_30(self, companies: List[Company]) -> None:
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
            index_elements=['XXtickerXX'],
            set_=update_cols
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_31(self, companies: List[Company]) -> None:
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
            index_elements=['TICKER'],
            set_=update_cols
        )
        
        self._session.execute(stmt)
        self._session.commit()

    def xǁPostgresCompanyRepositoryǁsave_batch__mutmut_32(self, companies: List[Company]) -> None:
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
        
        self._session.execute(None)
        self._session.commit()
    
    xǁPostgresCompanyRepositoryǁsave_batch__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_1': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_1, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_2': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_2, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_3': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_3, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_4': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_4, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_5': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_5, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_6': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_6, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_7': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_7, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_8': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_8, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_9': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_9, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_10': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_10, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_11': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_11, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_12': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_12, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_13': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_13, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_14': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_14, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_15': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_15, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_16': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_16, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_17': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_17, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_18': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_18, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_19': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_19, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_20': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_20, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_21': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_21, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_22': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_22, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_23': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_23, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_24': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_24, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_25': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_25, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_26': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_26, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_27': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_27, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_28': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_28, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_29': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_29, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_30': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_30, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_31': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_31, 
        'xǁPostgresCompanyRepositoryǁsave_batch__mutmut_32': xǁPostgresCompanyRepositoryǁsave_batch__mutmut_32
    }
    xǁPostgresCompanyRepositoryǁsave_batch__mutmut_orig.__name__ = 'xǁPostgresCompanyRepositoryǁsave_batch'

    def get_by_ticker(self, ticker: str) -> Optional[Company]:
        args = [ticker]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_orig'), object.__getattribute__(self, 'xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_mutants'), args, kwargs, self)

    def xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_orig(self, ticker: str) -> Optional[Company]:
        model = self._session.query(CompanyModel).filter(CompanyModel.ticker == ticker).first()
        if model:
            return self._to_entity(model)
        return None

    def xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_1(self, ticker: str) -> Optional[Company]:
        model = None
        if model:
            return self._to_entity(model)
        return None

    def xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_2(self, ticker: str) -> Optional[Company]:
        model = self._session.query(CompanyModel).filter(None).first()
        if model:
            return self._to_entity(model)
        return None

    def xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_3(self, ticker: str) -> Optional[Company]:
        model = self._session.query(None).filter(CompanyModel.ticker == ticker).first()
        if model:
            return self._to_entity(model)
        return None

    def xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_4(self, ticker: str) -> Optional[Company]:
        model = self._session.query(CompanyModel).filter(CompanyModel.ticker != ticker).first()
        if model:
            return self._to_entity(model)
        return None

    def xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_5(self, ticker: str) -> Optional[Company]:
        model = self._session.query(CompanyModel).filter(CompanyModel.ticker == ticker).first()
        if model:
            return self._to_entity(None)
        return None
    
    xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_1': xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_1, 
        'xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_2': xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_2, 
        'xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_3': xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_3, 
        'xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_4': xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_4, 
        'xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_5': xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_5
    }
    xǁPostgresCompanyRepositoryǁget_by_ticker__mutmut_orig.__name__ = 'xǁPostgresCompanyRepositoryǁget_by_ticker'

    def get_all(self) -> List[Company]:
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPostgresCompanyRepositoryǁget_all__mutmut_orig'), object.__getattribute__(self, 'xǁPostgresCompanyRepositoryǁget_all__mutmut_mutants'), args, kwargs, self)

    def xǁPostgresCompanyRepositoryǁget_all__mutmut_orig(self) -> List[Company]:
        models = self._session.query(CompanyModel).all()
        return [self._to_entity(m) for m in models]

    def xǁPostgresCompanyRepositoryǁget_all__mutmut_1(self) -> List[Company]:
        models = None
        return [self._to_entity(m) for m in models]

    def xǁPostgresCompanyRepositoryǁget_all__mutmut_2(self) -> List[Company]:
        models = self._session.query(None).all()
        return [self._to_entity(m) for m in models]

    def xǁPostgresCompanyRepositoryǁget_all__mutmut_3(self) -> List[Company]:
        models = self._session.query(CompanyModel).all()
        return [self._to_entity(None) for m in models]
    
    xǁPostgresCompanyRepositoryǁget_all__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPostgresCompanyRepositoryǁget_all__mutmut_1': xǁPostgresCompanyRepositoryǁget_all__mutmut_1, 
        'xǁPostgresCompanyRepositoryǁget_all__mutmut_2': xǁPostgresCompanyRepositoryǁget_all__mutmut_2, 
        'xǁPostgresCompanyRepositoryǁget_all__mutmut_3': xǁPostgresCompanyRepositoryǁget_all__mutmut_3
    }
    xǁPostgresCompanyRepositoryǁget_all__mutmut_orig.__name__ = 'xǁPostgresCompanyRepositoryǁget_all'
