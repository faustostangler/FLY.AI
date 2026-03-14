from typing import Optional

class DomainError(Exception):
    """Base class for all domain exceptions"""
    pass

class CompanySyncError(DomainError):
    """Base class for errors during company synchronization."""
    pass

class CompanyValidationError(CompanySyncError):
    """Raised when a Company entity invariant is violated."""
    pass

class B3RateLimitExceededError(CompanySyncError):
    """Raised when B3 returns HTTP 429 - Too Many Requests."""
    pass

class B3NetworkTimeoutError(CompanySyncError):
    """Raised when a request to B3 times out."""
    pass

class CompanyDataValidationError(CompanySyncError):
    """
    Raised when raw data from B3 fails validation/sanitization 
    before even becoming a Domain Entity. Useful for tracking Data Quality.
    """
    def __init__(self, message: str, field: str, ticker: Optional[str] = None):
        super().__init__(message)
        self.field = field
        self.ticker = ticker
