from typing import Optional, Any
from shared.domain.errors import DomainError


class CompanyDomainError(DomainError):
    """Base class for errors in the Companies Bounded Context."""
    pass


class CompanySyncError(CompanyDomainError):
    """Base class for errors during company synchronization."""
    def __init__(self, message: str, code: str = "COMPANY_SYNC_ERROR", details: Optional[dict[str, Any]] = None):
        super().__init__(message=message, code=code, details=details)


class CompanyValidationError(CompanySyncError):
    """Raised when a Company entity invariant is violated."""
    def __init__(self, message: str, details: Optional[dict[str, Any]] = None):
        super().__init__(
            message=message,
            code="COMPANY_VALIDATION_ERROR",
            details=details
        )


class B3RateLimitExceededError(CompanySyncError):
    """Raised when B3 returns HTTP 429 - Too Many Requests."""
    def __init__(self, message: str = "B3 Rate limit exceeded. Throttling active.", details: Optional[dict[str, Any]] = None):
        super().__init__(
            message=message,
            code="B3_RATE_LIMIT_EXCEEDED",
            details=details
        )


class B3NetworkTimeoutError(CompanySyncError):
    """Raised when a request to B3 times out."""
    def __init__(self, target_url: str):
        super().__init__(
            message=f"B3 Network timeout for {target_url}",
            code="B3_NETWORK_TIMEOUT",
            details={"url": target_url}
        )


class CompanyDataValidationError(CompanySyncError):
    """
    Raised when raw data from B3 fails validation/sanitization
    before even becoming a Domain Entity. Useful for tracking Data Quality.
    """
    def __init__(self, message: str, field: str, ticker: Optional[str] = None):
        super().__init__(
            message=message,
            code="COMPANY_DATA_VALIDATION_ERROR",
            details={"field": field, "ticker": ticker}
        )
