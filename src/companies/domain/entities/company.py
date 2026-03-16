from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List
import re

from companies.domain.value_objects.cnpj import CNPJ
from companies.domain.exceptions import CompanyValidationError


@dataclass(kw_only=True)
class Company:
    """Rich Domain Entity representing a publicly traded Issuer.

    This is the Aggregate Root for the 'Issuers' bounded context. It
    encapsulates all business rules and state transitions related to
    companies listed on the B3 exchange, ensuring the model is always
    in a valid state.

    Attributes:
        ticker (str): The primary trading symbol for the company.
        cvm_code (str): Unique identification code assigned by the CVM.
        company_name (str): Legal corporate name.
        trading_name (str): The name used in market interactions.
        cnpj (CNPJ): Validated Brazilian tax identification number.
        listing (str): The listing market (e.g., 'BOVESPA').
        sector (str): The broad economic sector.
        subsector (str): A more granular classification of business activity.
        segment (str): The specific listing segment for corporate governance.
        status (str): Operational state (e.g., 'ATIVO', 'INATIVO').
        ticker_codes (List[str]): All trading symbols associated with this issuer.
        isin_codes (List[str]): International Securities Identification Numbers.
    """

    # Canonical identification used to correlate data across sources.
    ticker: str
    cvm_code: str
    company_name: str
    trading_name: Optional[str] = None
    cnpj: Optional[CNPJ] = None

    # B3-specific market metadata used for fundamental analysis.
    listing: Optional[str] = None
    sector: Optional[str] = None
    subsector: Optional[str] = None
    segment: Optional[str] = None
    segment_eng: Optional[str] = None
    activity: Optional[str] = None
    describle_category_bvmf: Optional[str] = None

    # Lifecycle timestamps.
    date_listing: Optional[datetime] = None
    last_date: Optional[datetime] = None
    date_quotation: Optional[datetime] = None

    # Administrative and legal metadata.
    website: Optional[str] = None
    registrar: Optional[str] = None
    main_registrar: Optional[str] = None
    status: Optional[str] = None
    company_type: Optional[str] = None
    market_indicator: Optional[str] = None

    # Financial instrument identifiers.
    ticker_codes: List[str] = field(default_factory=list)
    isin_codes: List[str] = field(default_factory=list)
    type_bdr: Optional[str] = None
    has_quotation: Optional[bool] = None
    has_emissions: Optional[bool] = None
    has_bdr: Optional[bool] = None

    def __post_init__(self):
        """Enforces Domain Invariants upon creation.

        Following the 'Always-Valid' entity pattern prevents the
        instantiation of companies with corrupt or logically impossible
        identification codes.
        """
        self._validate_cvm_code()
        self._validate_ticker()

    def _validate_cvm_code(self):
        """Ensures the CVM code conforms to the regulatory numeric format."""
        if not self.cvm_code.isdigit():
            raise CompanyValidationError(
                f"CVM code must contain only digits, got '{self.cvm_code}'."
            )

    def _validate_ticker(self):
        """Enforces the standard B3 symbol formatting rules."""
        # Symbols must be alphanumeric and follow length constraints
        # to avoid ingestion of garbage data from scrapper noise.
        if not re.match(r"^[A-Z0-9]{2,12}$", self.ticker):
            raise CompanyValidationError(
                f"Ticker '{self.ticker}' must be 2-12 alphanumeric characters."
            )

    # --- Domain Behavior (State Transitions) ---

    def mark_as_delisted(self, last_quotation_date: datetime):
        """Transitions the entity to an inactive state after delisting from the exchange.

        Delisting is a significant business event that affects data
        availability for trading algorithms.

        Args:
            last_quotation_date (datetime): The final captured market activity timestamp.
        """
        self.status = "INATIVO"
        self.last_date = last_quotation_date
        self.has_quotation = False

    def add_security_codes(self, isin: str, ticker: str):
        """Registers unique market identifiers associated with this issuer.

        Companies often have multiple tickers (ON, PN, UNT) and ISINs.
        This method ensures duplicates are handled gracefully.

        Args:
            isin (str): The unique ISIN to be added.
            ticker (str): The trading symbol to be associated.
        """
        if isin and isin not in self.isin_codes:
            self.isin_codes.append(isin)
        if ticker and ticker not in self.ticker_codes:
            self.ticker_codes.append(ticker)
