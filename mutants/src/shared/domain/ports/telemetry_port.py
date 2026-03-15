from abc import ABC, abstractmethod
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

class TelemetryPort(ABC):
    @abstractmethod
    def increment_active_sync_tasks(self) -> None:
        pass

    @abstractmethod
    def decrement_active_sync_tasks(self) -> None:
        pass

    @abstractmethod
    def increment_companies_synced(self, count: int, status: str) -> None:
        pass

    @abstractmethod
    def set_companies_by_sector(self, sector: str, count: int) -> None:
        pass

    @abstractmethod
    def set_companies_by_segment(self, segment: str, count: int) -> None:
        pass

    @abstractmethod
    def observe_sync_duration(self, context: str, duration: float) -> None:
        pass

    @abstractmethod
    def increment_date_parsing_failures(self, field: str, source: str) -> None:
        pass

    @abstractmethod
    def increment_b3_rate_limit_hits(self) -> None:
        pass

    @abstractmethod
    def increment_network_transmit_bytes(self, direction: str, context: str, payload_size: int) -> None:
        pass

    @abstractmethod
    def increment_data_validation_error(self, entity: str, field: str, reason: str) -> None:
        pass

    @abstractmethod
    def increment_generic_sync_error(self, type: str) -> None:
        pass
