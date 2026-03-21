from abc import ABC, abstractmethod
from typing import List, Optional
from companies.domain.entities import Company


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
