from dataclasses import dataclass
from typing import Optional, Any

@dataclass(frozen=True)
class DomainError:
    """
    Base class for all domain errors.
    Isolated from Python's Exception hierarchy to ensure pure domain modeling.
    """
    message: str
    code: str
    details: Optional[dict[str, Any]] = None

    def __str__(self) -> str:
        return f"[{self.code}] {self.message}"
