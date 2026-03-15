from abc import ABC, abstractmethod
from typing import List, Optional
from companies.domain.entities.company import Company
from typing import Annotated
from typing import Callable

MutantDict = Annotated[dict[str, Callable], "Mutant"]  # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg=None):  # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os  # type: ignore

    mutant_under_test = os.environ["MUTANT_UNDER_TEST"]  # type: ignore
    if mutant_under_test == "fail":  # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException  # type: ignore

        raise MutmutProgrammaticFailException("Failed programmatically")  # type: ignore
    elif mutant_under_test == "stats":  # type: ignore
        from mutmut.__main__ import record_trampoline_hit  # type: ignore

        record_trampoline_hit(orig.__module__ + "." + orig.__name__)  # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs)  # type: ignore
        return result  # type: ignore
    prefix = orig.__module__ + "." + orig.__name__ + "__mutmut_"  # type: ignore
    if not mutant_under_test.startswith(prefix):  # type: ignore
        result = orig(*call_args, **call_kwargs)  # type: ignore
        return result  # type: ignore
    mutant_name = mutant_under_test.rpartition(".")[-1]  # type: ignore
    if self_arg is not None:  # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)  # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)  # type: ignore
    return result  # type: ignore


class CompanyRepository(ABC):
    """Port for Issuer persistence operations.

    In Hexagonal Architecture, this interface acts as a Port. It allows
    the Domain to express its persistence requirements without being coupled
    to a specific database technology (PostgreSQL, MongoDB, etc.).
    """

    @abstractmethod
    def save(self, company: Company) -> None:
        """Persists a single Company entity.

        Used for individual updates or real-time state transitions
        where immediate consistency is required.
        """
        pass

    @abstractmethod
    def save_batch(self, companies: List[Company]) -> None:
        """Persists multiple Company entities in a single atomic transaction.

        Batch operations significantly reduce database round-trips
        and connection overhead during the heavy B3 synchronization cycles.
        """
        pass

    @abstractmethod
    def get_by_ticker(self, ticker: str) -> Optional[Company]:
        """Retrieves a company using its primary market identifier.

        Returns:
            Optional[Company]: The domain entity if found, else None.
        """
        pass

    @abstractmethod
    def get_all(self) -> List[Company]:
        """Returns the complete list of issuers currently in the domain.

        Used for full-cache refreshes or analytical exports.
        """
        pass
