from typing import Optional
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
        args = [message, field, ticker]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁCompanyDataValidationErrorǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁCompanyDataValidationErrorǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁCompanyDataValidationErrorǁ__init____mutmut_orig(self, message: str, field: str, ticker: Optional[str] = None):
        super().__init__(message)
        self.field = field
        self.ticker = ticker
    def xǁCompanyDataValidationErrorǁ__init____mutmut_1(self, message: str, field: str, ticker: Optional[str] = None):
        super().__init__(None)
        self.field = field
        self.ticker = ticker
    def xǁCompanyDataValidationErrorǁ__init____mutmut_2(self, message: str, field: str, ticker: Optional[str] = None):
        super().__init__(message)
        self.field = None
        self.ticker = ticker
    def xǁCompanyDataValidationErrorǁ__init____mutmut_3(self, message: str, field: str, ticker: Optional[str] = None):
        super().__init__(message)
        self.field = field
        self.ticker = None
    
    xǁCompanyDataValidationErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁCompanyDataValidationErrorǁ__init____mutmut_1': xǁCompanyDataValidationErrorǁ__init____mutmut_1, 
        'xǁCompanyDataValidationErrorǁ__init____mutmut_2': xǁCompanyDataValidationErrorǁ__init____mutmut_2, 
        'xǁCompanyDataValidationErrorǁ__init____mutmut_3': xǁCompanyDataValidationErrorǁ__init____mutmut_3
    }
    xǁCompanyDataValidationErrorǁ__init____mutmut_orig.__name__ = 'xǁCompanyDataValidationErrorǁ__init__'
