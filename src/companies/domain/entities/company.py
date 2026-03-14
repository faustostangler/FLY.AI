from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
import re

from companies.domain.value_objects.cnpj import CNPJ
from companies.domain.exceptions import CompanyValidationError

@dataclass(kw_only=True)
class Company:
    """
    Rich Domain Entity representing a Company.
    Pure Python dataclass, independent of frameworks.
    """
    # Core Identification
    ticker: str
    cvm_code: str
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
    ticker_codes: List[str] = field(default_factory=list)
    isin_codes: List[str] = field(default_factory=list)
    type_bdr: Optional[str] = None
    has_quotation: Optional[bool] = None
    has_emissions: Optional[bool] = None
    has_bdr: Optional[bool] = None

    def __post_init__(self):
        """Domain Invariants Validation (Always-Valid Entity)"""
        self._validate_cvm_code()
        self._validate_ticker()

    def _validate_cvm_code(self):
        if not self.cvm_code.isdigit():
            raise CompanyValidationError(f"CVM code must contain only digits, got '{self.cvm_code}'.")

    def _validate_ticker(self):
        # SOTA Rule: 2-12 alphanumeric characters
        if not re.match(r"^[A-Z0-9]{2,12}$", self.ticker):
            raise CompanyValidationError(f"Ticker '{self.ticker}' must be 2-12 alphanumeric characters.")

    # --- Domain Behavior (Rich Model) ---
    
    def mark_as_delisted(self, last_quotation_date: datetime):
        """Changes company status to reflect delisting."""
        self.status = "INATIVO"
        self.last_date = last_quotation_date
        self.has_quotation = False

    def add_security_codes(self, isin: str, ticker: str):
        """Encapsulates the logic of adding security codes to the company."""
        if isin and isin not in self.isin_codes:
            self.isin_codes.append(isin)
        if ticker and ticker not in self.ticker_codes:
            self.ticker_codes.append(ticker)
