class DomainError(Exception):
    """Base class for all domain exceptions"""
    pass

class CompanyValidationError(DomainError):
    """Raised when a Company entity invariant is violated"""
    pass
