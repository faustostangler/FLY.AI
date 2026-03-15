from typing import Optional, List, Any
from datetime import datetime
from pydantic import BaseModel, Field, field_validator, ConfigDict
from shared.infrastructure.utils.text import TextCleaner
from companies.domain.entities.company import Company
from companies.domain.value_objects.cnpj import CNPJ
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

class B3CompanyPayloadDTO(BaseModel):
    """
    Anti-Corruption Layer DTO.
    Handles sanitization and validation of raw data from B3 
    before it enters the Domain layer.
    """
    model_config = ConfigDict(extra='ignore')

    ticker: str
    cvm_code: str
    company_name: str
    trading_name: Optional[str] = None
    cnpj: Optional[str] = None
    
    # B3 Market details
    listing: Optional[str] = None
    sector: Optional[str] = None
    subsector: Optional[str] = None
    segment: Optional[str] = None
    segment_eng: Optional[str] = None
    activity: Optional[str] = None
    describle_category_bvmf: Optional[str] = None
    
    # Dates (Already parsed by Use Case in current logic, but could be here)
    date_listing: Optional[datetime] = None
    last_date: Optional[datetime] = None
    date_quotation: Optional[datetime] = None
    
    # Infrastructure / Legal
    website: Optional[str] = None
    registrar: Optional[str] = None
    main_registrar: Optional[str] = None
    status: Optional[str] = None
    type: Optional[str] = None
    market_indicator: Optional[str] = None
    
    # Securities Identifiers
    ticker_codes: List[str] = Field(default_factory=list)
    isin_codes: List[str] = Field(default_factory=list)
    type_bdr: Optional[str] = None
    has_quotation: Optional[bool] = None
    has_emissions: Optional[bool] = None
    has_bdr: Optional[bool] = None

    @field_validator(
        "ticker", "company_name", "trading_name", "sector", "subsector", 
        "segment", "segment_eng", "activity", "listing", "status", "type",
        "registrar", "main_registrar", "describle_category_bvmf", "website",
        mode="before"
    )
    @classmethod
    def clean_strings(cls, v: Any) -> Any:
        if isinstance(v, str):
            return TextCleaner.clean(v)
        return v

    @field_validator("has_quotation", "has_emissions", "has_bdr", mode="before")
    @classmethod
    def resilient_bool(cls, v: Any) -> Optional[bool]:
        """Convert strings/numbers to boolean for B3 compatibility."""
        if v is None:
            return None
        if isinstance(v, bool):
            return v
        if isinstance(v, str):
            v_lower = v.lower().strip()
            if v_lower in ("true", "1", "yes", "s", "y", "ativo"):
                return True
            if v_lower in ("false", "0", "no", "n", "inativo"):
                return False
        if isinstance(v, (int, float)):
            return bool(v)
        return None

    def to_domain(self) -> Company:
        args = []# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁB3CompanyPayloadDTOǁto_domain__mutmut_orig'), object.__getattribute__(self, 'xǁB3CompanyPayloadDTOǁto_domain__mutmut_mutants'), args, kwargs, self)

    def xǁB3CompanyPayloadDTOǁto_domain__mutmut_orig(self) -> Company:
        """Translates the sanitized DTO into a pure Domain Entity."""
        data = self.model_dump()
        
        # Instantiate Value Objects
        cnpj_val = data.pop('cnpj', None)
        if cnpj_val:
            # Note: CNPJ validator will run during instantiation if it's a RootModel
            data['cnpj'] = CNPJ(cnpj_val)
        else:
            data['cnpj'] = None
            
        return Company(**data)

    def xǁB3CompanyPayloadDTOǁto_domain__mutmut_1(self) -> Company:
        """Translates the sanitized DTO into a pure Domain Entity."""
        data = None
        
        # Instantiate Value Objects
        cnpj_val = data.pop('cnpj', None)
        if cnpj_val:
            # Note: CNPJ validator will run during instantiation if it's a RootModel
            data['cnpj'] = CNPJ(cnpj_val)
        else:
            data['cnpj'] = None
            
        return Company(**data)

    def xǁB3CompanyPayloadDTOǁto_domain__mutmut_2(self) -> Company:
        """Translates the sanitized DTO into a pure Domain Entity."""
        data = self.model_dump()
        
        # Instantiate Value Objects
        cnpj_val = None
        if cnpj_val:
            # Note: CNPJ validator will run during instantiation if it's a RootModel
            data['cnpj'] = CNPJ(cnpj_val)
        else:
            data['cnpj'] = None
            
        return Company(**data)

    def xǁB3CompanyPayloadDTOǁto_domain__mutmut_3(self) -> Company:
        """Translates the sanitized DTO into a pure Domain Entity."""
        data = self.model_dump()
        
        # Instantiate Value Objects
        cnpj_val = data.pop(None, None)
        if cnpj_val:
            # Note: CNPJ validator will run during instantiation if it's a RootModel
            data['cnpj'] = CNPJ(cnpj_val)
        else:
            data['cnpj'] = None
            
        return Company(**data)

    def xǁB3CompanyPayloadDTOǁto_domain__mutmut_4(self) -> Company:
        """Translates the sanitized DTO into a pure Domain Entity."""
        data = self.model_dump()
        
        # Instantiate Value Objects
        cnpj_val = data.pop(None)
        if cnpj_val:
            # Note: CNPJ validator will run during instantiation if it's a RootModel
            data['cnpj'] = CNPJ(cnpj_val)
        else:
            data['cnpj'] = None
            
        return Company(**data)

    def xǁB3CompanyPayloadDTOǁto_domain__mutmut_5(self) -> Company:
        """Translates the sanitized DTO into a pure Domain Entity."""
        data = self.model_dump()
        
        # Instantiate Value Objects
        cnpj_val = data.pop('cnpj', )
        if cnpj_val:
            # Note: CNPJ validator will run during instantiation if it's a RootModel
            data['cnpj'] = CNPJ(cnpj_val)
        else:
            data['cnpj'] = None
            
        return Company(**data)

    def xǁB3CompanyPayloadDTOǁto_domain__mutmut_6(self) -> Company:
        """Translates the sanitized DTO into a pure Domain Entity."""
        data = self.model_dump()
        
        # Instantiate Value Objects
        cnpj_val = data.pop('XXcnpjXX', None)
        if cnpj_val:
            # Note: CNPJ validator will run during instantiation if it's a RootModel
            data['cnpj'] = CNPJ(cnpj_val)
        else:
            data['cnpj'] = None
            
        return Company(**data)

    def xǁB3CompanyPayloadDTOǁto_domain__mutmut_7(self) -> Company:
        """Translates the sanitized DTO into a pure Domain Entity."""
        data = self.model_dump()
        
        # Instantiate Value Objects
        cnpj_val = data.pop('CNPJ', None)
        if cnpj_val:
            # Note: CNPJ validator will run during instantiation if it's a RootModel
            data['cnpj'] = CNPJ(cnpj_val)
        else:
            data['cnpj'] = None
            
        return Company(**data)

    def xǁB3CompanyPayloadDTOǁto_domain__mutmut_8(self) -> Company:
        """Translates the sanitized DTO into a pure Domain Entity."""
        data = self.model_dump()
        
        # Instantiate Value Objects
        cnpj_val = data.pop('cnpj', None)
        if cnpj_val:
            # Note: CNPJ validator will run during instantiation if it's a RootModel
            data['cnpj'] = None
        else:
            data['cnpj'] = None
            
        return Company(**data)

    def xǁB3CompanyPayloadDTOǁto_domain__mutmut_9(self) -> Company:
        """Translates the sanitized DTO into a pure Domain Entity."""
        data = self.model_dump()
        
        # Instantiate Value Objects
        cnpj_val = data.pop('cnpj', None)
        if cnpj_val:
            # Note: CNPJ validator will run during instantiation if it's a RootModel
            data['XXcnpjXX'] = CNPJ(cnpj_val)
        else:
            data['cnpj'] = None
            
        return Company(**data)

    def xǁB3CompanyPayloadDTOǁto_domain__mutmut_10(self) -> Company:
        """Translates the sanitized DTO into a pure Domain Entity."""
        data = self.model_dump()
        
        # Instantiate Value Objects
        cnpj_val = data.pop('cnpj', None)
        if cnpj_val:
            # Note: CNPJ validator will run during instantiation if it's a RootModel
            data['CNPJ'] = CNPJ(cnpj_val)
        else:
            data['cnpj'] = None
            
        return Company(**data)

    def xǁB3CompanyPayloadDTOǁto_domain__mutmut_11(self) -> Company:
        """Translates the sanitized DTO into a pure Domain Entity."""
        data = self.model_dump()
        
        # Instantiate Value Objects
        cnpj_val = data.pop('cnpj', None)
        if cnpj_val:
            # Note: CNPJ validator will run during instantiation if it's a RootModel
            data['cnpj'] = CNPJ(None)
        else:
            data['cnpj'] = None
            
        return Company(**data)

    def xǁB3CompanyPayloadDTOǁto_domain__mutmut_12(self) -> Company:
        """Translates the sanitized DTO into a pure Domain Entity."""
        data = self.model_dump()
        
        # Instantiate Value Objects
        cnpj_val = data.pop('cnpj', None)
        if cnpj_val:
            # Note: CNPJ validator will run during instantiation if it's a RootModel
            data['cnpj'] = CNPJ(cnpj_val)
        else:
            data['cnpj'] = ""
            
        return Company(**data)

    def xǁB3CompanyPayloadDTOǁto_domain__mutmut_13(self) -> Company:
        """Translates the sanitized DTO into a pure Domain Entity."""
        data = self.model_dump()
        
        # Instantiate Value Objects
        cnpj_val = data.pop('cnpj', None)
        if cnpj_val:
            # Note: CNPJ validator will run during instantiation if it's a RootModel
            data['cnpj'] = CNPJ(cnpj_val)
        else:
            data['XXcnpjXX'] = None
            
        return Company(**data)

    def xǁB3CompanyPayloadDTOǁto_domain__mutmut_14(self) -> Company:
        """Translates the sanitized DTO into a pure Domain Entity."""
        data = self.model_dump()
        
        # Instantiate Value Objects
        cnpj_val = data.pop('cnpj', None)
        if cnpj_val:
            # Note: CNPJ validator will run during instantiation if it's a RootModel
            data['cnpj'] = CNPJ(cnpj_val)
        else:
            data['CNPJ'] = None
            
        return Company(**data)
    
    xǁB3CompanyPayloadDTOǁto_domain__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁB3CompanyPayloadDTOǁto_domain__mutmut_1': xǁB3CompanyPayloadDTOǁto_domain__mutmut_1, 
        'xǁB3CompanyPayloadDTOǁto_domain__mutmut_2': xǁB3CompanyPayloadDTOǁto_domain__mutmut_2, 
        'xǁB3CompanyPayloadDTOǁto_domain__mutmut_3': xǁB3CompanyPayloadDTOǁto_domain__mutmut_3, 
        'xǁB3CompanyPayloadDTOǁto_domain__mutmut_4': xǁB3CompanyPayloadDTOǁto_domain__mutmut_4, 
        'xǁB3CompanyPayloadDTOǁto_domain__mutmut_5': xǁB3CompanyPayloadDTOǁto_domain__mutmut_5, 
        'xǁB3CompanyPayloadDTOǁto_domain__mutmut_6': xǁB3CompanyPayloadDTOǁto_domain__mutmut_6, 
        'xǁB3CompanyPayloadDTOǁto_domain__mutmut_7': xǁB3CompanyPayloadDTOǁto_domain__mutmut_7, 
        'xǁB3CompanyPayloadDTOǁto_domain__mutmut_8': xǁB3CompanyPayloadDTOǁto_domain__mutmut_8, 
        'xǁB3CompanyPayloadDTOǁto_domain__mutmut_9': xǁB3CompanyPayloadDTOǁto_domain__mutmut_9, 
        'xǁB3CompanyPayloadDTOǁto_domain__mutmut_10': xǁB3CompanyPayloadDTOǁto_domain__mutmut_10, 
        'xǁB3CompanyPayloadDTOǁto_domain__mutmut_11': xǁB3CompanyPayloadDTOǁto_domain__mutmut_11, 
        'xǁB3CompanyPayloadDTOǁto_domain__mutmut_12': xǁB3CompanyPayloadDTOǁto_domain__mutmut_12, 
        'xǁB3CompanyPayloadDTOǁto_domain__mutmut_13': xǁB3CompanyPayloadDTOǁto_domain__mutmut_13, 
        'xǁB3CompanyPayloadDTOǁto_domain__mutmut_14': xǁB3CompanyPayloadDTOǁto_domain__mutmut_14
    }
    xǁB3CompanyPayloadDTOǁto_domain__mutmut_orig.__name__ = 'xǁB3CompanyPayloadDTOǁto_domain'
