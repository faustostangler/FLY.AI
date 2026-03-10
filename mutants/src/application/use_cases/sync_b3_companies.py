import asyncio
import logging
from typing import Dict, Any, List
from pydantic import ValidationError

from domain.entities.company import Company
from domain.ports.scrapers.b3_scraper_port import B3ScraperPort
from domain.ports.repositories.company_repository import CompanyRepository

logger = logging.getLogger(__name__)
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

class SyncB3CompaniesUseCase:
    """
    Application Use Case to synchronize the list of companies from B3
    into the database using the scraper and repository ports.
    """
    def __init__(self, scraper: B3ScraperPort, repository: CompanyRepository):
        args = [scraper, repository]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁSyncB3CompaniesUseCaseǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁSyncB3CompaniesUseCaseǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁSyncB3CompaniesUseCaseǁ__init____mutmut_orig(self, scraper: B3ScraperPort, repository: CompanyRepository):
        self._scraper = scraper
        self._repository = repository
        
    def xǁSyncB3CompaniesUseCaseǁ__init____mutmut_1(self, scraper: B3ScraperPort, repository: CompanyRepository):
        self._scraper = None
        self._repository = repository
        
    def xǁSyncB3CompaniesUseCaseǁ__init____mutmut_2(self, scraper: B3ScraperPort, repository: CompanyRepository):
        self._scraper = scraper
        self._repository = None
        
    
    xǁSyncB3CompaniesUseCaseǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁSyncB3CompaniesUseCaseǁ__init____mutmut_1': xǁSyncB3CompaniesUseCaseǁ__init____mutmut_1, 
        'xǁSyncB3CompaniesUseCaseǁ__init____mutmut_2': xǁSyncB3CompaniesUseCaseǁ__init____mutmut_2
    }
    xǁSyncB3CompaniesUseCaseǁ__init____mutmut_orig.__name__ = 'xǁSyncB3CompaniesUseCaseǁ__init__'
    def _map_b3_payload_to_entity(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        args = [basic_info, detailed_info]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_orig'), object.__getattribute__(self, 'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_mutants'), args, kwargs, self)
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_orig(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_1(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=None,
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_2(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=None,
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_3(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=None,
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_4(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=None,
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_5(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=None,
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_6(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=None,
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_7(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=None,
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_8(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=None,
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_9(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=None,
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_10(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=None,
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_11(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=None,
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_12(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=None,
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_13(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=None,
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_14(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=None,
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_15(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=None,
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_16(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=None,
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_17(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=None,
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_18(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=None,
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_19(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=None,
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_20(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=None,
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_21(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=None,
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_22(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=None,
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_23(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=None,
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_24(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=None,
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_25(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=None
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_26(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_27(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_28(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_29(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_30(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_31(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_32(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_33(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_34(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_35(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_36(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_37(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_38(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_39(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_40(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_41(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_42(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_43(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_44(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_45(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_46(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_47(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_48(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_49(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_50(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_51(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get(None),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_52(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("XXissuingCompanyXX"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_53(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingcompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_54(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("ISSUINGCOMPANY"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_55(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(None),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_56(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get(None)),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_57(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("XXcodeCVMXX")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_58(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codecvm")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_59(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("CODECVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_60(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get(None),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_61(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("XXcompanyNameXX"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_62(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyname"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_63(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("COMPANYNAME"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_64(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get(None),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_65(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("XXtradingNameXX"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_66(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingname"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_67(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("TRADINGNAME"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_68(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get(None),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_69(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("XXcnpjXX"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_70(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("CNPJ"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_71(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get(None),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_72(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("XXmarketXX"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_73(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("MARKET"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_74(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get(None),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_75(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("XXsectorXX"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_76(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("SECTOR"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_77(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get(None),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_78(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("XXsubsectorXX"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_79(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("SUBSECTOR"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_80(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get(None),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_81(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("XXsegmentXX"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_82(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("SEGMENT"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_83(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get(None),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_84(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("XXsegmentEngXX"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_85(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmenteng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_86(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("SEGMENTENG"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_87(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get(None),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_88(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("XXactivityXX"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_89(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("ACTIVITY"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_90(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get(None),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_91(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("XXdescrible_category_bvmfXX"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_92(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("DESCRIBLE_CATEGORY_BVMF"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_93(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get(None),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_94(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("XXdateListingXX"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_95(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("datelisting"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_96(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("DATELISTING"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_97(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get(None),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_98(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("XXlast_dateXX"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_99(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("LAST_DATE"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_100(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get(None),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_101(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("XXdate_quotationXX"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_102(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("DATE_QUOTATION"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_103(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get(None),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_104(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("XXwebsiteXX"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_105(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("WEBSITE"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_106(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get(None),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_107(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("XXregistrarXX"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_108(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("REGISTRAR"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_109(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get(None),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_110(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("XXmain_registrarXX"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_111(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("MAIN_REGISTRAR"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_112(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get(None),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_113(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("XXstatusXX"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_114(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("STATUS"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_115(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get(None),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_116(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("XXtypeXX"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_117(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("TYPE"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_118(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get(None),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_119(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("XXmarketIndicatorXX"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_120(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketindicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_121(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("MARKETINDICATOR"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_122(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get(None),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_123(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("XXtypeBDRXX"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_124(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typebdr"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_125(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("TYPEBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_126(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(None),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_127(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get(None, "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_128(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", None)),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_129(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_130(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", )),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_131(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("XXhas_quotationXX", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_132(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("HAS_QUOTATION", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_133(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "XXXX")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_134(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(None),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_135(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get(None, "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_136(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", None)),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_137(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_138(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", )),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_139(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("XXhas_emissionsXX", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_140(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("HAS_EMISSIONS", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_141(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "XXXX")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_142(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(None)
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_143(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get(None, ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_144(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", None))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_145(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get(""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_146(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_147(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("XXhas_bdrXX", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_148(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("HAS_BDR", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_149(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", "XXXX"))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingCompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_150(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(None)
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_151(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get(None)}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_152(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('XXissuingCompanyXX')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_153(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('issuingcompany')}: {e}")
            raise e
    def xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_154(self, basic_info: Dict[str, Any], detailed_info: Dict[str, Any]) -> Company:
        """
        Maps raw JSON from B3 into the Company domain entity.
        Includes fallbacks and conversions matching the Domain rules.
        """
        try:
            return Company(
                ticker=basic_info.get("issuingCompany"),
                cvm_code=str(basic_info.get("codeCVM")),
                company_name=basic_info.get("companyName"),
                trading_name=detailed_info.get("tradingName"),
                cnpj=detailed_info.get("cnpj"),
                listing=detailed_info.get("market"),
                sector=detailed_info.get("sector"),
                subsector=detailed_info.get("subsector"),
                segment=detailed_info.get("segment"),
                segment_eng=detailed_info.get("segmentEng"),
                activity=detailed_info.get("activity"),
                describle_category_bvmf=detailed_info.get("describle_category_bvmf"),
                date_listing=detailed_info.get("dateListing"),
                last_date=detailed_info.get("last_date"),
                date_quotation=detailed_info.get("date_quotation"),
                website=detailed_info.get("website"),
                registrar=detailed_info.get("registrar"),
                main_registrar=detailed_info.get("main_registrar"),
                status=detailed_info.get("status"),
                type=detailed_info.get("type"),
                market_indicator=detailed_info.get("marketIndicator"),
                type_bdr=detailed_info.get("typeBDR"),
                has_quotation=str(detailed_info.get("has_quotation", "")),
                has_emissions=str(detailed_info.get("has_emissions", "")),
                has_bdr=str(detailed_info.get("has_bdr", ""))
                # Note: ticker_codes and isin_codes might require complex mapping 
                # from `otherCodes` array if needed later.
            )
        except ValidationError as e:
            logger.error(f"Validation error for {basic_info.get('ISSUINGCOMPANY')}: {e}")
            raise e
    
    xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_1': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_1, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_2': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_2, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_3': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_3, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_4': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_4, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_5': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_5, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_6': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_6, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_7': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_7, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_8': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_8, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_9': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_9, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_10': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_10, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_11': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_11, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_12': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_12, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_13': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_13, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_14': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_14, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_15': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_15, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_16': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_16, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_17': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_17, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_18': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_18, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_19': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_19, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_20': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_20, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_21': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_21, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_22': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_22, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_23': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_23, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_24': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_24, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_25': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_25, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_26': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_26, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_27': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_27, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_28': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_28, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_29': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_29, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_30': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_30, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_31': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_31, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_32': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_32, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_33': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_33, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_34': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_34, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_35': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_35, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_36': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_36, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_37': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_37, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_38': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_38, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_39': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_39, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_40': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_40, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_41': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_41, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_42': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_42, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_43': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_43, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_44': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_44, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_45': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_45, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_46': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_46, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_47': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_47, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_48': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_48, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_49': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_49, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_50': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_50, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_51': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_51, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_52': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_52, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_53': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_53, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_54': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_54, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_55': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_55, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_56': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_56, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_57': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_57, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_58': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_58, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_59': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_59, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_60': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_60, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_61': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_61, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_62': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_62, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_63': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_63, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_64': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_64, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_65': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_65, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_66': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_66, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_67': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_67, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_68': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_68, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_69': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_69, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_70': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_70, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_71': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_71, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_72': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_72, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_73': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_73, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_74': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_74, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_75': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_75, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_76': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_76, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_77': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_77, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_78': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_78, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_79': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_79, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_80': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_80, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_81': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_81, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_82': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_82, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_83': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_83, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_84': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_84, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_85': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_85, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_86': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_86, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_87': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_87, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_88': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_88, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_89': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_89, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_90': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_90, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_91': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_91, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_92': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_92, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_93': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_93, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_94': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_94, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_95': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_95, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_96': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_96, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_97': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_97, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_98': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_98, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_99': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_99, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_100': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_100, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_101': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_101, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_102': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_102, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_103': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_103, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_104': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_104, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_105': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_105, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_106': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_106, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_107': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_107, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_108': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_108, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_109': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_109, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_110': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_110, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_111': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_111, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_112': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_112, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_113': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_113, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_114': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_114, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_115': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_115, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_116': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_116, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_117': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_117, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_118': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_118, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_119': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_119, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_120': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_120, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_121': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_121, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_122': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_122, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_123': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_123, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_124': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_124, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_125': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_125, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_126': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_126, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_127': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_127, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_128': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_128, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_129': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_129, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_130': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_130, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_131': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_131, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_132': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_132, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_133': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_133, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_134': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_134, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_135': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_135, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_136': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_136, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_137': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_137, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_138': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_138, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_139': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_139, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_140': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_140, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_141': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_141, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_142': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_142, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_143': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_143, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_144': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_144, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_145': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_145, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_146': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_146, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_147': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_147, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_148': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_148, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_149': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_149, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_150': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_150, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_151': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_151, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_152': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_152, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_153': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_153, 
        'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_154': xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_154
    }
    xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity__mutmut_orig.__name__ = 'xǁSyncB3CompaniesUseCaseǁ_map_b3_payload_to_entity'

    async def execute(self) -> None:
        args = []# type: ignore
        kwargs = {}# type: ignore
        return await _mutmut_trampoline(object.__getattribute__(self, 'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_orig'), object.__getattribute__(self, 'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_mutants'), args, kwargs, self)

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_orig(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_1(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info(None)
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_2(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("XXStarting B3 Companies SynchronizationXX")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_3(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("starting b3 companies synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_4(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("STARTING B3 COMPANIES SYNCHRONIZATION")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_5(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = None
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_6(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = None
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_7(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(None):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_8(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = None
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_9(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get(None)
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_10(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("XXissuingCompanyXX")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_11(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingcompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_12(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("ISSUINGCOMPANY")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_13(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = None
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_14(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(None)
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_15(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get(None))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_16(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("XXcodeCVMXX"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_17(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codecvm"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_18(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("CODECVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_19(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker and not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_20(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_21(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_22(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(None)
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_23(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                break
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_24(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(None)
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_25(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index - 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_26(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 2}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_27(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = None
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_28(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(None)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_29(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = None
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_30(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(None, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_31(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, None)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_32(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_33(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, )
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_34(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(None)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_35(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(None)
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_36(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(None)
            self._repository.save_batch(entities_to_save)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_37(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(None)
        
        logger.info("Synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_38(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info(None)

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_39(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("XXSynchronization completed successfully.XX")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_40(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("synchronization completed successfully.")

    async def xǁSyncB3CompaniesUseCaseǁexecute__mutmut_41(self) -> None:
        """
        Main execution flow:
        1. Fetch all companies listed.
        2. Fetch details for each company.
        3. Map to Domain Entities.
        4. Save to Repository in batches.
        """
        logger.info("Starting B3 Companies Synchronization")
        
        # 1. Fetch the raw initial list
        initial_companies = await self._scraper.fetch_initial_companies()
        
        entities_to_save: List[Company] = []
        
        for index, raw_company in enumerate(initial_companies):
            ticker = raw_company.get("issuingCompany")
            cvm_code = str(raw_company.get("codeCVM"))
            
            if not ticker or not cvm_code.isdigit():
                logger.warning(f"Skipping invalid entry: {ticker} (CVM: {cvm_code})")
                continue
                
            logger.info(f"Processing {index + 1}/{len(initial_companies)}: {ticker}")
            
            try:
                # 2. Detail fetch
                details = await self._scraper.fetch_company_details(cvm_code)
                
                # 3. Domain Mapping 
                # Merging dictionaries strategy isn't needed here if we pass both
                company_entity = self._map_b3_payload_to_entity(raw_company, details)
                entities_to_save.append(company_entity)
            except Exception as e:
                logger.error(f"Failed to process {ticker}: {e}")
                
        # 4. Persistence
        if entities_to_save:
            logger.info(f"Saving {len(entities_to_save)} companies to the repository.")
            self._repository.save_batch(entities_to_save)
        
        logger.info("SYNCHRONIZATION COMPLETED SUCCESSFULLY.")
    
    xǁSyncB3CompaniesUseCaseǁexecute__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_1': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_1, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_2': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_2, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_3': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_3, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_4': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_4, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_5': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_5, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_6': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_6, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_7': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_7, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_8': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_8, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_9': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_9, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_10': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_10, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_11': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_11, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_12': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_12, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_13': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_13, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_14': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_14, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_15': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_15, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_16': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_16, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_17': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_17, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_18': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_18, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_19': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_19, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_20': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_20, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_21': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_21, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_22': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_22, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_23': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_23, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_24': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_24, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_25': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_25, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_26': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_26, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_27': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_27, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_28': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_28, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_29': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_29, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_30': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_30, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_31': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_31, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_32': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_32, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_33': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_33, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_34': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_34, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_35': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_35, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_36': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_36, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_37': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_37, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_38': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_38, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_39': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_39, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_40': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_40, 
        'xǁSyncB3CompaniesUseCaseǁexecute__mutmut_41': xǁSyncB3CompaniesUseCaseǁexecute__mutmut_41
    }
    xǁSyncB3CompaniesUseCaseǁexecute__mutmut_orig.__name__ = 'xǁSyncB3CompaniesUseCaseǁexecute'
