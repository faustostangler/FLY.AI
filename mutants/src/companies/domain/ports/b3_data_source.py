from abc import ABC, abstractmethod
from typing import List, Dict, Any
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


class B3DataSource(ABC):
    """
    Port (abstract contract) for B3 data retrieval operations.
    Defines the interface that any infrastructure adapter must implement
    to provide company data from B3.
    """

    @abstractmethod
    async def fetch_initial_companies(self) -> List[Dict[str, Any]]:
        """
        Fetch the initial paginated list of all companies from B3.
        Returns the raw dictionaries that will be parsed by the Use Cases.
        """
        pass

    @abstractmethod
    async def fetch_company_details(self, cvm_code: str) -> Dict[str, Any]:
        """
        Fetch detailed information for a specific company using its CVM code.
        """
        pass

    @abstractmethod
    async def fetch_company_financials(self, cvm_code: str) -> Dict[str, Any]:
        """
        Fetch financial info and shareholders for a specific company using its CVM code.
        """
        pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass
