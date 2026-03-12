from typing import Optional, List
from pydantic import BaseModel, Field, field_validator
import re
from companies.domain.value_objects.cnpj import CNPJ
from shared.infrastructure.utils.text import TextCleaner

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

    @field_validator(
        "company_name", "trading_name", "sector", "subsector", 
        "segment", "activity", "listing", "status", "type",
        mode="before"
    )
    @classmethod
    def clean_text_fields(cls, v: Optional[str]) -> Optional[str]:
        """Automatically cleans text fields during entity creation."""
        return TextCleaner.clean(v)

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
