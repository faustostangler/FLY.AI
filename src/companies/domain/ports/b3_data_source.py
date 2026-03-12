from abc import ABC, abstractmethod
from typing import List, Dict, Any


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
