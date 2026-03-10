from abc import ABC, abstractmethod
from typing import List, Optional
from domain.entities.company import Company

class CompanyRepository(ABC):
    """
    Port for company data persistence.
    """

    @abstractmethod
    def save(self, company: Company) -> None:
        pass

    @abstractmethod
    def save_batch(self, companies: List[Company]) -> None:
        pass

    @abstractmethod
    def get_by_ticker(self, ticker: str) -> Optional[Company]:
        pass

    @abstractmethod
    def get_all(self) -> List[Company]:
        pass
