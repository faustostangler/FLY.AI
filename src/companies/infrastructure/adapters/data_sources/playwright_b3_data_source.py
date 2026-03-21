from typing import List, Dict, Any, Optional
import json
import base64
from playwright.async_api import async_playwright
from companies.domain.ports.b3_data_source import B3DataSource
from companies.domain.exceptions import B3RateLimitExceededError, B3NetworkTimeoutError
from shared.infrastructure.config import settings
from shared.domain.ports.telemetry_port import TelemetryPort
from shared.domain.utils.result import Result


class PlaywrightB3DataSource(B3DataSource):
    """B3 Data Source implemented using Playwright with Result Monad."""

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
        if not self._playwright:
            self._playwright = await async_playwright().start()
            self._browser = await self._playwright.chromium.launch(
                headless=self.headless
            )
            self._context = await self._browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            page = await self._context.new_page()
            await page.goto(self.homepage_url, wait_until="networkidle")
            await page.close()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self._browser:
            await self._browser.close()
        if self._playwright:
            await self._playwright.stop()
        self._browser = None
        self._playwright = None
        self._context = None

    def _create_token(self, payload: dict) -> str:
        json_str = json.dumps(payload)
        return base64.b64encode(json_str.encode("utf-8")).decode("utf-8")

    async def _get_context(self):
        if self._context:
            return self._context, False
        p = await async_playwright().start()
        b = await p.chromium.launch(headless=self.headless)
        c = await b.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        return c, True

    async def fetch_initial_companies(self) -> Result[List[Dict[str, Any]], Exception]:
        all_companies = []
        context, is_temp = await self._get_context()

        try:
            if is_temp:
                page = await context.new_page()
                await page.goto(self.homepage_url, wait_until="networkidle")
                await page.close()

            page_num = -1
            total_pages = -1

            while page_num <= total_pages:
                payload = {"language": "pt-br", "pageNumber": page_num, "pageSize": 20}
                token = self._create_token(payload)
                endpoint = f"{self.initial_companies_api}{token}"

                response = await context.request.get(
                    endpoint,
                    headers={
                        "Referer": settings.b3.referer_url,
                        "X-DtReferer": self.homepage_url,
                    },
                )

                if response.status == 429:
                    self._telemetry.increment_b3_rate_limit_hits()
                    return Result.fail(B3RateLimitExceededError(f"Rate limited (429) at page {page_num}"))

                if not response.ok:
                    return Result.fail(Exception(f"Failed to fetch initial companies page {page_num}: {response.status}"))

                body = await response.body()
                self._telemetry.increment_network_transmit_bytes(
                    direction="inbound", context="b3_initial", payload_size=len(body)
                )

                data = json.loads(body)
                if page_num == -1: # B3 initial page often returns total
                     page_num = 1
                     total_pages = data.get("page", {}).get("totalPages", 1)
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
            
            return Result.ok(all_companies)
        except Exception as e:
            return Result.fail(e)
        finally:
            if is_temp:
                await context.browser.close()

    async def fetch_company_details(self, cvm_code: str) -> Result[Dict[str, Any], Exception]:
        endpoint_base = settings.b3.detail_api
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        context, is_temp = await self._get_context()

        try:
            response = await context.request.get(
                f"{endpoint_base}{token}",
                headers={
                    "Referer": settings.b3.referer_url,
                    "X-DtReferer": self.homepage_url,
                },
            )

            if response.status == 429:
                self._telemetry.increment_b3_rate_limit_hits()
                return Result.fail(B3RateLimitExceededError(f"Rate limited by B3 (429) for {cvm_code}."))

            if not response.ok:
                return Result.fail(Exception(f"Failed to fetch details for {cvm_code}: {response.status}"))

            body = await response.body()
            self._telemetry.increment_network_transmit_bytes(
                direction="inbound", context="b3_detail", payload_size=len(body)
            )

            return Result.ok(json.loads(body))
        except Exception as e:
            return Result.fail(e)
        finally:
            if is_temp:
                await context.browser.close()

    async def fetch_company_financials(self, cvm_code: str) -> Result[Dict[str, Any], Exception]:
        endpoint_base = settings.b3.financial_api
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        context, is_temp = await self._get_context()

        try:
            response = await context.request.get(
                f"{endpoint_base}{token}",
                headers={
                    "Referer": settings.b3.referer_url,
                    "X-DtReferer": self.homepage_url,
                },
            )
            if not response.ok:
                return Result.fail(Exception(f"Failed to fetch financials for {cvm_code}"))
            return Result.ok(await response.json())
        except Exception as e:
            return Result.fail(e)
        finally:
            if is_temp:
                await context.browser.close()
