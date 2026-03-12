from typing import List, Dict, Any
from playwright.async_api import async_playwright, Page, BrowserContext
from src.companies.domain.ports.b3_data_source import B3DataSource
import json
import base64


class PlaywrightB3DataSource(B3DataSource):
    def __init__(self, headless: bool = True):
        self.headless = headless
        self.homepage_url = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/?language=pt-br"
        self.initial_companies_api = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetInitialCompanies/"

    def _create_token(self, payload: dict) -> str:
        """Helper to create the base64 token required by B3 endpoints."""
        json_str = json.dumps(payload)
        return base64.b64encode(json_str.encode('utf-8')).decode('utf-8')

    async def fetch_initial_companies(self) -> List[Dict[str, Any]]:
        """
        Navigates to the B3 page to get cookies/WAF clearance, then hits the backend API
        to fetch the paginated list of all companies.
        """
        all_companies = []

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            page = await context.new_page()

            # Step 1: Hit the frontend to acquire necessary cookies / tokens
            await page.goto(self.homepage_url, wait_until="networkidle")

            # Step 2: Query the API directly using the context's request feature
            page_num = 1
            total_pages = 1

            while page_num <= total_pages:
                payload = {"language": "pt-br", "pageNumber": page_num, "pageSize": 120}
                token = self._create_token(payload)
                endpoint = f"{self.initial_companies_api}{token}"

                response = await context.request.get(endpoint)
                if not response.ok:
                    raise Exception(f"Failed to fetch page {page_num}: {response.status}")

                data = await response.json()

                if page_num == 1:
                    total_pages = data.get("page", {}).get("totalPages", 1)

                companies = data.get("results", [])
                all_companies.extend(companies)

                page_num += 1

            await browser.close()

        return all_companies

    async def fetch_company_details(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            page = await context.new_page()

            # Get session
            await page.goto(self.homepage_url, wait_until="networkidle")

            # API Request
            response = await context.request.get(f"{endpoint_base}{token}")
            if not response.ok:
                raise Exception(f"Failed to fetch details for {cvm_code}: {response.status}")

            data = await response.json()
            await browser.close()
            return data

    async def fetch_company_financials(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            page = await context.new_page()

            await page.goto(self.homepage_url, wait_until="networkidle")

            response = await context.request.get(f"{endpoint_base}{token}")
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")

            data = await response.json()
            await browser.close()
            return data
