from typing import Generic, TypeVar, Optional, Any, Union
from dataclasses import dataclass

T = TypeVar("T")
E = TypeVar("E", bound=Exception)
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

@dataclass(frozen=True)
class Result(Generic[T, E]):
    """
    SOTA Result Monad for deterministic flow control.
    Encapsulates success (value) or failure (error) without using None as a sentinel.
    """
    value: Optional[T] = None
    error: Optional[E] = None

    @classmethod
    def ok(cls, value: T) -> 'Result[T, E]':
        """Creates a success result."""
        return cls(value=value, error=None)

    @classmethod
    def fail(cls, error: E) -> 'Result[T, E]':
        """Creates a failure result."""
        return cls(value=None, error=error)

    @property
    def is_success(self) -> bool:
        """Returns True if the result is a success."""
        return self.error is None

    @property
    def is_failure(self) -> bool:
        """Returns True if the result is a failure."""
        return self.error is not None

    def unwrap(self) -> T:
        """Returns the value if success, otherwise raises the error."""
        if self.is_failure:
            raise self.error  # type: ignore
        return self.value  # type: ignore
