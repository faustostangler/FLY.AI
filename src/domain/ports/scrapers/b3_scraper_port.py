from abc import ABC, abstractmethod
from typing import List, Dict, Any

class B3ScraperPort(ABC):
    """
    Port for the B3 scraping operations.
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
