from typing import Optional, List
from pydantic import BaseModel, Field, field_validator
import re
from domain.value_objects.cnpj import CNPJ
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

class Company(BaseModel):
    # Core Identification
    ticker: str = Field(..., min_length=4, max_length=10, description="The stock ticker code, e.g., PETR4")
    cvm_code: str = Field(..., min_length=1, max_length=10, description="The CVM numeric code")
    company_name: str
    trading_name: Optional[str] = None
    cnpj: Optional[CNPJ] = None
    
    # Optional B3 Market details
    listing: Optional[str] = None
    sector: Optional[str] = None
    subsector: Optional[str] = None
    segment: Optional[str] = None
    segment_eng: Optional[str] = None
    activity: Optional[str] = None
    describle_category_bvmf: Optional[str] = None
    
    # Optional Dates
    date_listing: Optional[str] = None
    last_date: Optional[str] = None
    date_quotation: Optional[str] = None
    
    # Optional Infrastructure / Legal
    website: Optional[str] = None
    registrar: Optional[str] = None
    main_registrar: Optional[str] = None
    status: Optional[str] = None
    type: Optional[str] = None
    market_indicator: Optional[str] = None
    
    # Securities Identifiers
    ticker_codes: Optional[str] = None # JSON dumped list in legacy, but maybe we could map as list in new DDD
    isin_codes: Optional[str] = None   # Same
    type_bdr: Optional[str] = None
    has_quotation: Optional[str] = None
    has_emissions: Optional[str] = None
    has_bdr: Optional[str] = None

    @field_validator("cvm_code")
    def validate_cvm_code_is_numeric(cls, v: str) -> str:
        if not v.isdigit():
            raise ValueError("CVM code must contain only digits.")
        return v
    
    @field_validator("ticker")
    def validate_ticker_format(cls, v: str) -> str:
        if not re.match(r"^[A-Z]{4}[0-9A-Z]{0,6}$", v):
            raise ValueError("Ticker must start with 4 letters followed by numbers/letters")
        return v
