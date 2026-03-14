from typing import List, Dict, Any, Optional
import json
import base64
from playwright.async_api import async_playwright, Page, BrowserContext
from companies.domain.ports.b3_data_source import B3DataSource
from companies.domain.exceptions import B3RateLimitExceededError
from shared.infrastructure.config import settings
from shared.domain.ports.telemetry_port import TelemetryPort

class PlaywrightB3DataSource(B3DataSource):
    """B3 Data Source implemented using Playwright.

    B3's modern listing APIs often require session cookies and 
    browser-like behavior (WAF) to prevent simple HTTP clients from scraping. 
    By using Playwright, we simulate a legitimate user session, ensuring 
    higher reliability for the synchronization process.
    """
    def __init__(self, telemetry: TelemetryPort, headless: Optional[bool] = None):
        self._telemetry = telemetry
        self.headless = headless if headless is not None else settings.app.headless
        self.homepage_url = settings.b3.homepage_url
        self.initial_companies_api = settings.b3.initial_companies_api
        
        # State management for the persistent browser session.
        self._playwright = None
        self._browser = None
        self._context = None

    async def __aenter__(self):
        """Initializes a shared browser context for efficient multi-fetching.

        Launching a browser for every request is prohibitively expensive. 
        Using a context manager allows the Use Case to batch-process issuers 
        using a single, high-performance execution environment.
        """
        if not self._playwright:
            self._playwright = await async_playwright().start()
            self._browser = await self._playwright.chromium.launch(headless=self.headless)
            self._context = await self._browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            # Hit the homepage once to establish session cookies and clear basic WAF gates.
            page = await self._context.new_page()
            await page.goto(self.homepage_url, wait_until="networkidle")
            await page.close()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Ensures complete cleanup of browser processes to prevent memory leaks."""
        if self._browser:
            await self._browser.close()
        if self._playwright:
            await self._playwright.stop()
        self._browser = None
        self._playwright = None
        self._context = None

    def _create_token(self, payload: dict) -> str:
        """Generates the Base64-encoded token required by B3 API endpoints.

        B3 uses a transparent Base64 JSON payload as a URL parameter 
        rather than standard query strings or POST bodies.
        """
        json_str = json.dumps(payload)
        return base64.b64encode(json_str.encode('utf-8')).decode('utf-8')

    async def _get_context(self):
        """Secures an active browser context for API interaction.

        Supports both managed sessions (via __aenter__) and one-off 
        calls (used primarily in legacy tests or simple CLI tools).
        """
        if self._context:
            return self._context, False # (context, is_temporary_marker)
        
        # Fallback for unmanaged sessions: create a temporary browser instance.
        p = await async_playwright().start()
        b = await p.chromium.launch(headless=self.headless)
        c = await b.new_context(
             user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        return c, True

    async def fetch_initial_companies(self) -> List[Dict[str, Any]]:
        """Retrieves the full list of companies currently listed on B3.

        Returns:
            List[Dict[str, Any]]: Raw records from the discovery endpoint.

        Raises:
            B3RateLimitExceededError: If the 429 quota is reached.
        """
        all_companies = []
        context, is_temp = await self._get_context()
        
        try:
            if is_temp:
                page = await context.new_page()
                await page.goto(self.homepage_url, wait_until="networkidle")
                await page.close()

            # B3 uses specific pagination logic where -1 often triggers 'all' or 'first page'.
            page_num = -1 
            total_pages = -1

            while page_num <= total_pages:
                payload = {"language": "pt-br", "pageNumber": page_num, "pageSize": 20}
                token = self._create_token(payload)
                endpoint = f"{self.initial_companies_api}{token}"

                response = await context.request.get(
                    endpoint,
                    headers={
                        "Referer": "https://sistemaswebb3-listados.b3.com.br/",
                        "X-DtReferer": self.homepage_url
                    }
                )
                
                if response.status == 429:
                    self._telemetry.increment_b3_rate_limit_hits()
                    raise B3RateLimitExceededError(
                        f"Rate limited by B3 (429) on initial fetch. Payload: {payload}"
                    )
                
                if not response.ok:
                    raise Exception(
                        f"Failed to fetch initial companies page {page_num}: {response.status}"
                    )

                body = await response.body()
                self._telemetry.increment_network_transmit_bytes(
                    direction="inbound", context="b3_initial", payload_size=len(body)
                )

                data = json.loads(body)
                if page_num == 1:
                    total_pages = data.get("page", {}).get("totalPages", 1)

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def fetch_company_details(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches granular metadata for a specific issuer by its CVM code.

        This endpoint provides deeper attributes like industry classification 
        and CNPJ that are missing from the initial summary list.
        """
        endpoint_base = settings.b3.detail_api
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        context, is_temp = await self._get_context()

        try:
            response = await context.request.get(
                f"{endpoint_base}{token}",
                headers={
                    "Referer": "https://sistemaswebb3-listados.b3.com.br/",
                    "X-DtReferer": self.homepage_url
                }
            )
            
            if response.status == 429:
                self._telemetry.increment_b3_rate_limit_hits()
                raise B3RateLimitExceededError(
                    f"Rate limited by B3 (429) on details fetch for {cvm_code}."
                )

            if not response.ok:
                raise Exception(
                    f"Failed to fetch details for {cvm_code}: {response.status}"
                )
            
            body = await response.body()
            self._telemetry.increment_network_transmit_bytes(
                direction="inbound", context="b3_detail", payload_size=len(body)
            )
            
            return json.loads(body)
        finally:
            if is_temp:
                await context.browser.close()

    async def fetch_company_financials(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches the latest financial indicators for an issuer.

        Enables data quality checks on the financial health of the issuer 
        during the domain synchronization cycle.
        """
        endpoint_base = settings.b3.financial_api
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        context, is_temp = await self._get_context()

        try:
            response = await context.request.get(
                f"{endpoint_base}{token}",
                headers={
                    "Referer": "https://sistemaswebb3-listados.b3.com.br/",
                    "X-DtReferer": self.homepage_url
                }
            )
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
            return await response.json()
        finally:
            if is_temp:
                await context.browser.close()
