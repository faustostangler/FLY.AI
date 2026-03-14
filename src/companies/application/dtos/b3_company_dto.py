from typing import Optional, List, Any
from datetime import datetime
from pydantic import BaseModel, Field, field_validator, ConfigDict
from shared.infrastructure.utils.text import TextCleaner
from companies.domain.entities.company import Company
from companies.domain.value_objects.cnpj import CNPJ

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
