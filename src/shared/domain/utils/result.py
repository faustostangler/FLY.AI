from typing import Generic, TypeVar, Optional, Any, Union
from dataclasses import dataclass

T = TypeVar("T")
# E is now unbound, allowing for DomainError dataclasses or any other type
E = TypeVar("E")


class UnwrapError(Exception):
    """Raised when trying to unwrap a failure Result."""
    def __init__(self, error: Any):
        self.error = error
        super().__init__(f"Attempted to unwrap a failure Result: {error}")


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
        """
        Returns the value if success, otherwise raises an UnwrapError.
        Use sparingly in tests or top-level crash-handlers.
        """
        if self.is_failure:
            if isinstance(self.error, Exception):
                raise self.error
            raise UnwrapError(self.error)
        return self.value  # type: ignore
