from abc import ABC, abstractmethod
from typing import List, Dict, Any
from shared.domain.utils.result import Result


class B3DataSource(ABC):
    """
    Port (abstract contract) for B3 data retrieval operations.
    """

    @abstractmethod
    async def fetch_initial_companies(self) -> Result[List[Dict[str, Any]], Exception]:
        """
        Fetch the initial paginated list of all companies from B3.
        """
        pass

    @abstractmethod
    async def fetch_company_details(self, cvm_code: str) -> Result[Dict[str, Any], Exception]:
        """
        Fetch detailed information for a specific company using its CVM code.
        """
        pass

    @abstractmethod
    async def fetch_company_financials(self, cvm_code: str) -> Result[Dict[str, Any], Exception]:
        """
        Fetch financial info and shareholders for a specific company using its CVM code.
        """
        pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        pass
