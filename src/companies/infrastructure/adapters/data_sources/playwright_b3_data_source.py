from typing import List, Dict, Any, Optional
import json
import base64
from playwright.async_api import async_playwright, Page, BrowserContext
from companies.domain.ports.b3_data_source import B3DataSource
from shared.infrastructure.config import settings
from shared.infrastructure.monitoring.metrics import metrics

class PlaywrightB3DataSource(B3DataSource):
    def __init__(self, headless: Optional[bool] = None):
        self.headless = headless if headless is not None else settings.app.headless
        self.homepage_url = settings.b3.homepage_url
        self.initial_companies_api = settings.b3.initial_companies_api
        
        # Session Management
        self._playwright = None
        self._browser = None
        self._context = None

    async def __aenter__(self):
        """Starts a persistent browser session for multiple requests."""
        if not self._playwright:
            self._playwright = await async_playwright().start()
            self._browser = await self._playwright.chromium.launch(headless=self.headless)
            self._context = await self._browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            # Aciona a home uma única vez para limpar WAF/Cookies
            page = await self._context.new_page()
            await page.goto(self.homepage_url, wait_until="networkidle")
            await page.close()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Closes the persistent session."""
        if self._browser:
            await self._browser.close()
        if self._playwright:
            await self._playwright.stop()
        self._browser = None
        self._playwright = None
        self._context = None

    def _create_token(self, payload: dict) -> str:
        """Helper to create the base64 token required by B3 endpoints."""
        json_str = json.dumps(payload)
        return base64.b64encode(json_str.encode('utf-8')).decode('utf-8')

    async def _get_context(self):
        """Internal helper to reuse or create a context."""
        if self._context:
            return self._context, False # (context, is_temporary)
        
        # Se não estiver em um contexto gerenciado, criamos um temporário (legado/suporte unitário)
        p = await async_playwright().start()
        b = await p.chromium.launch(headless=self.headless)
        c = await b.new_context(
             user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        return c, True

    async def fetch_initial_companies(self) -> List[Dict[str, Any]]:
        all_companies = []
        context, is_temp = await self._get_context()
        
        try:
            if is_temp:
                page = await context.new_page()
                await page.goto(self.homepage_url, wait_until="networkidle")
                await page.close()

            page_num = -1 # -1 to get all at once
            total_pages = -1 # -1 to get all at once

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
                    metrics.b3_rate_limit_hits.inc()
                    raise Exception(f"Rate limited by B3 (429) on initial fetch. Payload: {payload}")
                
                if not response.ok:
                    raise Exception(f"Failed to fetch initial companies page {page_num}: {response.status}")

                body = await response.body()
                payload_size = len(body)
                metrics.network_transmit_bytes_total.labels(direction="inbound", context="b3_initial").inc(payload_size)

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
                metrics.b3_rate_limit_hits.inc()
                raise Exception(f"Rate limited by B3 (429) on details fetch for {cvm_code}.")

            if not response.ok:
                raise Exception(f"Failed to fetch details for {cvm_code}: {response.status}")
            
            body = await response.body()
            payload_size = len(body)
            metrics.network_transmit_bytes_total.labels(direction="inbound", context="b3_detail").inc(payload_size)
            
            return json.loads(body)
        finally:
            if is_temp:
                await context.browser.close()

    async def fetch_company_financials(self, cvm_code: str) -> Dict[str, Any]:
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
