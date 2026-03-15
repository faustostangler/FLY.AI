from typing import Generic, TypeVar, Optional
from dataclasses import dataclass

T = TypeVar("T")
E = TypeVar("E", bound=Exception)


@dataclass(frozen=True)
class Result(Generic[T, E]):
    """
    SOTA Result Monad for deterministic flow control.
    Encapsulates success (value) or failure (error) without using None as a sentinel.
    """

    value: Optional[T] = None
    error: Optional[E] = None

    @classmethod
    def ok(cls, value: T) -> "Result[T, E]":
        """Creates a success result."""
        return cls(value=value, error=None)

    @classmethod
    def fail(cls, error: E) -> "Result[T, E]":
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
