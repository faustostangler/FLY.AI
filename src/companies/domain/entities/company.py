from typing import Optional, List, Any
from datetime import datetime
from pydantic import BaseModel, Field, field_validator, ConfigDict
import re
from companies.domain.value_objects.cnpj import CNPJ
from shared.infrastructure.utils.text import TextCleaner
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
    date_listing: Optional[datetime] = None
    last_date: Optional[datetime] = None
    date_quotation: Optional[datetime] = None
    
    # Optional Infrastructure / Legal
    website: Optional[str] = None
    registrar: Optional[str] = None
    main_registrar: Optional[str] = None
    status: Optional[str] = None
    type: Optional[str] = None
    market_indicator: Optional[str] = None
    
    # Securities Identifiers
    ticker_codes: List[str] = Field(default_factory=list, description="List of all ticker codes associated with the company")
    isin_codes: List[str] = Field(default_factory=list, description="List of all ISIN codes associated with the company")
    type_bdr: Optional[str] = None
    has_quotation: Optional[bool] = None
    has_emissions: Optional[bool] = None
    has_bdr: Optional[bool] = None

    @field_validator(
        "ticker", "company_name", "trading_name", "sector", "subsector", 
        "segment", "segment_eng", "activity", "listing", "status", "type",
        "registrar", "main_registrar", "describle_category_bvmf",
        mode="before"
    )
    @classmethod
    def clean_text_fields(cls, v: Optional[str]) -> Optional[str]:
        """Automatically cleans text fields during entity creation."""
        return TextCleaner.clean(v)
    
    @field_validator("ticker_codes", "isin_codes", mode="before")
    @classmethod
    def validate_security_codes(cls, v: Any) -> List[str]:
        """Ensures security codes are handled as lists, even if passed as JSON strings."""
        if isinstance(v, str):
            try:
                import json
                data = json.loads(v)
                if isinstance(data, list):
                    return [str(item) for item in data]
            except (json.JSONDecodeError, TypeError):
                pass
        if isinstance(v, list):
            return [str(item) for item in v]
        return []

    @field_validator("cvm_code")
    def validate_cvm_code_is_numeric(cls, v: str) -> str:
        if not v.isdigit():
            raise ValueError("CVM code must contain only digits.")
        return v
    
    @field_validator("ticker")
    def validate_ticker_format(cls, v: str) -> str:
        """
        SOTA Ticker Validation: 
        Accepts any alphanumeric string between 2 and 12 chars to be extremely safe 
        with B3's evolving ticker formats (including indices, BDRs, etc).
        """
        if not re.match(r"^[A-Z0-9]{2,12}$", v):
            raise ValueError(f"Ticker '{v}' must be 2-12 alphanumeric characters (SOTA Rule)")
        return v

    @field_validator("has_quotation", "has_emissions", "has_bdr", mode="before")
    @classmethod
    def validate_bool_fields(cls, v: Any) -> Optional[bool]:
        """Resiliently converts strings/numbers to boolean for B3 compatibility."""
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
