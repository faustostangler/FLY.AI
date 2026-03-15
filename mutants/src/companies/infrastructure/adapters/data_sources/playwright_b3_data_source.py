from typing import List, Dict, Any, Optional
import json
import base64
from playwright.async_api import async_playwright, Page, BrowserContext
from companies.domain.ports.b3_data_source import B3DataSource
from companies.domain.exceptions import B3RateLimitExceededError
from shared.infrastructure.config import settings
from shared.domain.ports.telemetry_port import TelemetryPort
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore

class PlaywrightB3DataSource(B3DataSource):
    """B3 Data Source implemented using Playwright.

    B3's modern listing APIs often require session cookies and 
    browser-like behavior (WAF) to prevent simple HTTP clients from scraping. 
    By using Playwright, we simulate a legitimate user session, ensuring 
    higher reliability for the synchronization process.
    """
    def __init__(self, telemetry: TelemetryPort, headless: Optional[bool] = None):
        args = [telemetry, headless]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPlaywrightB3DataSourceǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁPlaywrightB3DataSourceǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁPlaywrightB3DataSourceǁ__init____mutmut_orig(self, telemetry: TelemetryPort, headless: Optional[bool] = None):
        self._telemetry = telemetry
        self.headless = headless if headless is not None else settings.app.headless
        self.homepage_url = settings.b3.homepage_url
        self.initial_companies_api = settings.b3.initial_companies_api
        
        # State management for the persistent browser session.
        self._playwright = None
        self._browser = None
        self._context = None
    def xǁPlaywrightB3DataSourceǁ__init____mutmut_1(self, telemetry: TelemetryPort, headless: Optional[bool] = None):
        self._telemetry = None
        self.headless = headless if headless is not None else settings.app.headless
        self.homepage_url = settings.b3.homepage_url
        self.initial_companies_api = settings.b3.initial_companies_api
        
        # State management for the persistent browser session.
        self._playwright = None
        self._browser = None
        self._context = None
    def xǁPlaywrightB3DataSourceǁ__init____mutmut_2(self, telemetry: TelemetryPort, headless: Optional[bool] = None):
        self._telemetry = telemetry
        self.headless = None
        self.homepage_url = settings.b3.homepage_url
        self.initial_companies_api = settings.b3.initial_companies_api
        
        # State management for the persistent browser session.
        self._playwright = None
        self._browser = None
        self._context = None
    def xǁPlaywrightB3DataSourceǁ__init____mutmut_3(self, telemetry: TelemetryPort, headless: Optional[bool] = None):
        self._telemetry = telemetry
        self.headless = headless if headless is None else settings.app.headless
        self.homepage_url = settings.b3.homepage_url
        self.initial_companies_api = settings.b3.initial_companies_api
        
        # State management for the persistent browser session.
        self._playwright = None
        self._browser = None
        self._context = None
    def xǁPlaywrightB3DataSourceǁ__init____mutmut_4(self, telemetry: TelemetryPort, headless: Optional[bool] = None):
        self._telemetry = telemetry
        self.headless = headless if headless is not None else settings.app.headless
        self.homepage_url = None
        self.initial_companies_api = settings.b3.initial_companies_api
        
        # State management for the persistent browser session.
        self._playwright = None
        self._browser = None
        self._context = None
    def xǁPlaywrightB3DataSourceǁ__init____mutmut_5(self, telemetry: TelemetryPort, headless: Optional[bool] = None):
        self._telemetry = telemetry
        self.headless = headless if headless is not None else settings.app.headless
        self.homepage_url = settings.b3.homepage_url
        self.initial_companies_api = None
        
        # State management for the persistent browser session.
        self._playwright = None
        self._browser = None
        self._context = None
    def xǁPlaywrightB3DataSourceǁ__init____mutmut_6(self, telemetry: TelemetryPort, headless: Optional[bool] = None):
        self._telemetry = telemetry
        self.headless = headless if headless is not None else settings.app.headless
        self.homepage_url = settings.b3.homepage_url
        self.initial_companies_api = settings.b3.initial_companies_api
        
        # State management for the persistent browser session.
        self._playwright = ""
        self._browser = None
        self._context = None
    def xǁPlaywrightB3DataSourceǁ__init____mutmut_7(self, telemetry: TelemetryPort, headless: Optional[bool] = None):
        self._telemetry = telemetry
        self.headless = headless if headless is not None else settings.app.headless
        self.homepage_url = settings.b3.homepage_url
        self.initial_companies_api = settings.b3.initial_companies_api
        
        # State management for the persistent browser session.
        self._playwright = None
        self._browser = ""
        self._context = None
    def xǁPlaywrightB3DataSourceǁ__init____mutmut_8(self, telemetry: TelemetryPort, headless: Optional[bool] = None):
        self._telemetry = telemetry
        self.headless = headless if headless is not None else settings.app.headless
        self.homepage_url = settings.b3.homepage_url
        self.initial_companies_api = settings.b3.initial_companies_api
        
        # State management for the persistent browser session.
        self._playwright = None
        self._browser = None
        self._context = ""
    
    xǁPlaywrightB3DataSourceǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPlaywrightB3DataSourceǁ__init____mutmut_1': xǁPlaywrightB3DataSourceǁ__init____mutmut_1, 
        'xǁPlaywrightB3DataSourceǁ__init____mutmut_2': xǁPlaywrightB3DataSourceǁ__init____mutmut_2, 
        'xǁPlaywrightB3DataSourceǁ__init____mutmut_3': xǁPlaywrightB3DataSourceǁ__init____mutmut_3, 
        'xǁPlaywrightB3DataSourceǁ__init____mutmut_4': xǁPlaywrightB3DataSourceǁ__init____mutmut_4, 
        'xǁPlaywrightB3DataSourceǁ__init____mutmut_5': xǁPlaywrightB3DataSourceǁ__init____mutmut_5, 
        'xǁPlaywrightB3DataSourceǁ__init____mutmut_6': xǁPlaywrightB3DataSourceǁ__init____mutmut_6, 
        'xǁPlaywrightB3DataSourceǁ__init____mutmut_7': xǁPlaywrightB3DataSourceǁ__init____mutmut_7, 
        'xǁPlaywrightB3DataSourceǁ__init____mutmut_8': xǁPlaywrightB3DataSourceǁ__init____mutmut_8
    }
    xǁPlaywrightB3DataSourceǁ__init____mutmut_orig.__name__ = 'xǁPlaywrightB3DataSourceǁ__init__'

    async def __aenter__(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return await _mutmut_trampoline(object.__getattribute__(self, 'xǁPlaywrightB3DataSourceǁ__aenter____mutmut_orig'), object.__getattribute__(self, 'xǁPlaywrightB3DataSourceǁ__aenter____mutmut_mutants'), args, kwargs, self)

    async def xǁPlaywrightB3DataSourceǁ__aenter____mutmut_orig(self):
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

    async def xǁPlaywrightB3DataSourceǁ__aenter____mutmut_1(self):
        """Initializes a shared browser context for efficient multi-fetching.

        Launching a browser for every request is prohibitively expensive. 
        Using a context manager allows the Use Case to batch-process issuers 
        using a single, high-performance execution environment.
        """
        if self._playwright:
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

    async def xǁPlaywrightB3DataSourceǁ__aenter____mutmut_2(self):
        """Initializes a shared browser context for efficient multi-fetching.

        Launching a browser for every request is prohibitively expensive. 
        Using a context manager allows the Use Case to batch-process issuers 
        using a single, high-performance execution environment.
        """
        if not self._playwright:
            self._playwright = None
            self._browser = await self._playwright.chromium.launch(headless=self.headless)
            self._context = await self._browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            # Hit the homepage once to establish session cookies and clear basic WAF gates.
            page = await self._context.new_page()
            await page.goto(self.homepage_url, wait_until="networkidle")
            await page.close()
        return self

    async def xǁPlaywrightB3DataSourceǁ__aenter____mutmut_3(self):
        """Initializes a shared browser context for efficient multi-fetching.

        Launching a browser for every request is prohibitively expensive. 
        Using a context manager allows the Use Case to batch-process issuers 
        using a single, high-performance execution environment.
        """
        if not self._playwright:
            self._playwright = await async_playwright().start()
            self._browser = None
            self._context = await self._browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            # Hit the homepage once to establish session cookies and clear basic WAF gates.
            page = await self._context.new_page()
            await page.goto(self.homepage_url, wait_until="networkidle")
            await page.close()
        return self

    async def xǁPlaywrightB3DataSourceǁ__aenter____mutmut_4(self):
        """Initializes a shared browser context for efficient multi-fetching.

        Launching a browser for every request is prohibitively expensive. 
        Using a context manager allows the Use Case to batch-process issuers 
        using a single, high-performance execution environment.
        """
        if not self._playwright:
            self._playwright = await async_playwright().start()
            self._browser = await self._playwright.chromium.launch(headless=None)
            self._context = await self._browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
            # Hit the homepage once to establish session cookies and clear basic WAF gates.
            page = await self._context.new_page()
            await page.goto(self.homepage_url, wait_until="networkidle")
            await page.close()
        return self

    async def xǁPlaywrightB3DataSourceǁ__aenter____mutmut_5(self):
        """Initializes a shared browser context for efficient multi-fetching.

        Launching a browser for every request is prohibitively expensive. 
        Using a context manager allows the Use Case to batch-process issuers 
        using a single, high-performance execution environment.
        """
        if not self._playwright:
            self._playwright = await async_playwright().start()
            self._browser = await self._playwright.chromium.launch(headless=self.headless)
            self._context = None
            # Hit the homepage once to establish session cookies and clear basic WAF gates.
            page = await self._context.new_page()
            await page.goto(self.homepage_url, wait_until="networkidle")
            await page.close()
        return self

    async def xǁPlaywrightB3DataSourceǁ__aenter____mutmut_6(self):
        """Initializes a shared browser context for efficient multi-fetching.

        Launching a browser for every request is prohibitively expensive. 
        Using a context manager allows the Use Case to batch-process issuers 
        using a single, high-performance execution environment.
        """
        if not self._playwright:
            self._playwright = await async_playwright().start()
            self._browser = await self._playwright.chromium.launch(headless=self.headless)
            self._context = await self._browser.new_context(
                user_agent=None
            )
            # Hit the homepage once to establish session cookies and clear basic WAF gates.
            page = await self._context.new_page()
            await page.goto(self.homepage_url, wait_until="networkidle")
            await page.close()
        return self

    async def xǁPlaywrightB3DataSourceǁ__aenter____mutmut_7(self):
        """Initializes a shared browser context for efficient multi-fetching.

        Launching a browser for every request is prohibitively expensive. 
        Using a context manager allows the Use Case to batch-process issuers 
        using a single, high-performance execution environment.
        """
        if not self._playwright:
            self._playwright = await async_playwright().start()
            self._browser = await self._playwright.chromium.launch(headless=self.headless)
            self._context = await self._browser.new_context(
                user_agent="XXMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36XX"
            )
            # Hit the homepage once to establish session cookies and clear basic WAF gates.
            page = await self._context.new_page()
            await page.goto(self.homepage_url, wait_until="networkidle")
            await page.close()
        return self

    async def xǁPlaywrightB3DataSourceǁ__aenter____mutmut_8(self):
        """Initializes a shared browser context for efficient multi-fetching.

        Launching a browser for every request is prohibitively expensive. 
        Using a context manager allows the Use Case to batch-process issuers 
        using a single, high-performance execution environment.
        """
        if not self._playwright:
            self._playwright = await async_playwright().start()
            self._browser = await self._playwright.chromium.launch(headless=self.headless)
            self._context = await self._browser.new_context(
                user_agent="mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/120.0.0.0 safari/537.36"
            )
            # Hit the homepage once to establish session cookies and clear basic WAF gates.
            page = await self._context.new_page()
            await page.goto(self.homepage_url, wait_until="networkidle")
            await page.close()
        return self

    async def xǁPlaywrightB3DataSourceǁ__aenter____mutmut_9(self):
        """Initializes a shared browser context for efficient multi-fetching.

        Launching a browser for every request is prohibitively expensive. 
        Using a context manager allows the Use Case to batch-process issuers 
        using a single, high-performance execution environment.
        """
        if not self._playwright:
            self._playwright = await async_playwright().start()
            self._browser = await self._playwright.chromium.launch(headless=self.headless)
            self._context = await self._browser.new_context(
                user_agent="MOZILLA/5.0 (WINDOWS NT 10.0; WIN64; X64) APPLEWEBKIT/537.36 (KHTML, LIKE GECKO) CHROME/120.0.0.0 SAFARI/537.36"
            )
            # Hit the homepage once to establish session cookies and clear basic WAF gates.
            page = await self._context.new_page()
            await page.goto(self.homepage_url, wait_until="networkidle")
            await page.close()
        return self

    async def xǁPlaywrightB3DataSourceǁ__aenter____mutmut_10(self):
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
            page = None
            await page.goto(self.homepage_url, wait_until="networkidle")
            await page.close()
        return self

    async def xǁPlaywrightB3DataSourceǁ__aenter____mutmut_11(self):
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
            await page.goto(None, wait_until="networkidle")
            await page.close()
        return self

    async def xǁPlaywrightB3DataSourceǁ__aenter____mutmut_12(self):
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
            await page.goto(self.homepage_url, wait_until=None)
            await page.close()
        return self

    async def xǁPlaywrightB3DataSourceǁ__aenter____mutmut_13(self):
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
            await page.goto(wait_until="networkidle")
            await page.close()
        return self

    async def xǁPlaywrightB3DataSourceǁ__aenter____mutmut_14(self):
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
            await page.goto(self.homepage_url, )
            await page.close()
        return self

    async def xǁPlaywrightB3DataSourceǁ__aenter____mutmut_15(self):
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
            await page.goto(self.homepage_url, wait_until="XXnetworkidleXX")
            await page.close()
        return self

    async def xǁPlaywrightB3DataSourceǁ__aenter____mutmut_16(self):
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
            await page.goto(self.homepage_url, wait_until="NETWORKIDLE")
            await page.close()
        return self
    
    xǁPlaywrightB3DataSourceǁ__aenter____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPlaywrightB3DataSourceǁ__aenter____mutmut_1': xǁPlaywrightB3DataSourceǁ__aenter____mutmut_1, 
        'xǁPlaywrightB3DataSourceǁ__aenter____mutmut_2': xǁPlaywrightB3DataSourceǁ__aenter____mutmut_2, 
        'xǁPlaywrightB3DataSourceǁ__aenter____mutmut_3': xǁPlaywrightB3DataSourceǁ__aenter____mutmut_3, 
        'xǁPlaywrightB3DataSourceǁ__aenter____mutmut_4': xǁPlaywrightB3DataSourceǁ__aenter____mutmut_4, 
        'xǁPlaywrightB3DataSourceǁ__aenter____mutmut_5': xǁPlaywrightB3DataSourceǁ__aenter____mutmut_5, 
        'xǁPlaywrightB3DataSourceǁ__aenter____mutmut_6': xǁPlaywrightB3DataSourceǁ__aenter____mutmut_6, 
        'xǁPlaywrightB3DataSourceǁ__aenter____mutmut_7': xǁPlaywrightB3DataSourceǁ__aenter____mutmut_7, 
        'xǁPlaywrightB3DataSourceǁ__aenter____mutmut_8': xǁPlaywrightB3DataSourceǁ__aenter____mutmut_8, 
        'xǁPlaywrightB3DataSourceǁ__aenter____mutmut_9': xǁPlaywrightB3DataSourceǁ__aenter____mutmut_9, 
        'xǁPlaywrightB3DataSourceǁ__aenter____mutmut_10': xǁPlaywrightB3DataSourceǁ__aenter____mutmut_10, 
        'xǁPlaywrightB3DataSourceǁ__aenter____mutmut_11': xǁPlaywrightB3DataSourceǁ__aenter____mutmut_11, 
        'xǁPlaywrightB3DataSourceǁ__aenter____mutmut_12': xǁPlaywrightB3DataSourceǁ__aenter____mutmut_12, 
        'xǁPlaywrightB3DataSourceǁ__aenter____mutmut_13': xǁPlaywrightB3DataSourceǁ__aenter____mutmut_13, 
        'xǁPlaywrightB3DataSourceǁ__aenter____mutmut_14': xǁPlaywrightB3DataSourceǁ__aenter____mutmut_14, 
        'xǁPlaywrightB3DataSourceǁ__aenter____mutmut_15': xǁPlaywrightB3DataSourceǁ__aenter____mutmut_15, 
        'xǁPlaywrightB3DataSourceǁ__aenter____mutmut_16': xǁPlaywrightB3DataSourceǁ__aenter____mutmut_16
    }
    xǁPlaywrightB3DataSourceǁ__aenter____mutmut_orig.__name__ = 'xǁPlaywrightB3DataSourceǁ__aenter__'

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        args = [exc_type, exc_val, exc_tb]# type: ignore
        kwargs = {}# type: ignore
        return await _mutmut_trampoline(object.__getattribute__(self, 'xǁPlaywrightB3DataSourceǁ__aexit____mutmut_orig'), object.__getattribute__(self, 'xǁPlaywrightB3DataSourceǁ__aexit____mutmut_mutants'), args, kwargs, self)

    async def xǁPlaywrightB3DataSourceǁ__aexit____mutmut_orig(self, exc_type, exc_val, exc_tb):
        """Ensures complete cleanup of browser processes to prevent memory leaks."""
        if self._browser:
            await self._browser.close()
        if self._playwright:
            await self._playwright.stop()
        self._browser = None
        self._playwright = None
        self._context = None

    async def xǁPlaywrightB3DataSourceǁ__aexit____mutmut_1(self, exc_type, exc_val, exc_tb):
        """Ensures complete cleanup of browser processes to prevent memory leaks."""
        if self._browser:
            await self._browser.close()
        if self._playwright:
            await self._playwright.stop()
        self._browser = ""
        self._playwright = None
        self._context = None

    async def xǁPlaywrightB3DataSourceǁ__aexit____mutmut_2(self, exc_type, exc_val, exc_tb):
        """Ensures complete cleanup of browser processes to prevent memory leaks."""
        if self._browser:
            await self._browser.close()
        if self._playwright:
            await self._playwright.stop()
        self._browser = None
        self._playwright = ""
        self._context = None

    async def xǁPlaywrightB3DataSourceǁ__aexit____mutmut_3(self, exc_type, exc_val, exc_tb):
        """Ensures complete cleanup of browser processes to prevent memory leaks."""
        if self._browser:
            await self._browser.close()
        if self._playwright:
            await self._playwright.stop()
        self._browser = None
        self._playwright = None
        self._context = ""
    
    xǁPlaywrightB3DataSourceǁ__aexit____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPlaywrightB3DataSourceǁ__aexit____mutmut_1': xǁPlaywrightB3DataSourceǁ__aexit____mutmut_1, 
        'xǁPlaywrightB3DataSourceǁ__aexit____mutmut_2': xǁPlaywrightB3DataSourceǁ__aexit____mutmut_2, 
        'xǁPlaywrightB3DataSourceǁ__aexit____mutmut_3': xǁPlaywrightB3DataSourceǁ__aexit____mutmut_3
    }
    xǁPlaywrightB3DataSourceǁ__aexit____mutmut_orig.__name__ = 'xǁPlaywrightB3DataSourceǁ__aexit__'

    def _create_token(self, payload: dict) -> str:
        args = [payload]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPlaywrightB3DataSourceǁ_create_token__mutmut_orig'), object.__getattribute__(self, 'xǁPlaywrightB3DataSourceǁ_create_token__mutmut_mutants'), args, kwargs, self)

    def xǁPlaywrightB3DataSourceǁ_create_token__mutmut_orig(self, payload: dict) -> str:
        """Generates the Base64-encoded token required by B3 API endpoints.

        B3 uses a transparent Base64 JSON payload as a URL parameter 
        rather than standard query strings or POST bodies.
        """
        json_str = json.dumps(payload)
        return base64.b64encode(json_str.encode('utf-8')).decode('utf-8')

    def xǁPlaywrightB3DataSourceǁ_create_token__mutmut_1(self, payload: dict) -> str:
        """Generates the Base64-encoded token required by B3 API endpoints.

        B3 uses a transparent Base64 JSON payload as a URL parameter 
        rather than standard query strings or POST bodies.
        """
        json_str = None
        return base64.b64encode(json_str.encode('utf-8')).decode('utf-8')

    def xǁPlaywrightB3DataSourceǁ_create_token__mutmut_2(self, payload: dict) -> str:
        """Generates the Base64-encoded token required by B3 API endpoints.

        B3 uses a transparent Base64 JSON payload as a URL parameter 
        rather than standard query strings or POST bodies.
        """
        json_str = json.dumps(None)
        return base64.b64encode(json_str.encode('utf-8')).decode('utf-8')

    def xǁPlaywrightB3DataSourceǁ_create_token__mutmut_3(self, payload: dict) -> str:
        """Generates the Base64-encoded token required by B3 API endpoints.

        B3 uses a transparent Base64 JSON payload as a URL parameter 
        rather than standard query strings or POST bodies.
        """
        json_str = json.dumps(payload)
        return base64.b64encode(json_str.encode('utf-8')).decode(None)

    def xǁPlaywrightB3DataSourceǁ_create_token__mutmut_4(self, payload: dict) -> str:
        """Generates the Base64-encoded token required by B3 API endpoints.

        B3 uses a transparent Base64 JSON payload as a URL parameter 
        rather than standard query strings or POST bodies.
        """
        json_str = json.dumps(payload)
        return base64.b64encode(None).decode('utf-8')

    def xǁPlaywrightB3DataSourceǁ_create_token__mutmut_5(self, payload: dict) -> str:
        """Generates the Base64-encoded token required by B3 API endpoints.

        B3 uses a transparent Base64 JSON payload as a URL parameter 
        rather than standard query strings or POST bodies.
        """
        json_str = json.dumps(payload)
        return base64.b64encode(json_str.encode(None)).decode('utf-8')

    def xǁPlaywrightB3DataSourceǁ_create_token__mutmut_6(self, payload: dict) -> str:
        """Generates the Base64-encoded token required by B3 API endpoints.

        B3 uses a transparent Base64 JSON payload as a URL parameter 
        rather than standard query strings or POST bodies.
        """
        json_str = json.dumps(payload)
        return base64.b64encode(json_str.encode('XXutf-8XX')).decode('utf-8')

    def xǁPlaywrightB3DataSourceǁ_create_token__mutmut_7(self, payload: dict) -> str:
        """Generates the Base64-encoded token required by B3 API endpoints.

        B3 uses a transparent Base64 JSON payload as a URL parameter 
        rather than standard query strings or POST bodies.
        """
        json_str = json.dumps(payload)
        return base64.b64encode(json_str.encode('UTF-8')).decode('utf-8')

    def xǁPlaywrightB3DataSourceǁ_create_token__mutmut_8(self, payload: dict) -> str:
        """Generates the Base64-encoded token required by B3 API endpoints.

        B3 uses a transparent Base64 JSON payload as a URL parameter 
        rather than standard query strings or POST bodies.
        """
        json_str = json.dumps(payload)
        return base64.b64encode(json_str.encode('utf-8')).decode('XXutf-8XX')

    def xǁPlaywrightB3DataSourceǁ_create_token__mutmut_9(self, payload: dict) -> str:
        """Generates the Base64-encoded token required by B3 API endpoints.

        B3 uses a transparent Base64 JSON payload as a URL parameter 
        rather than standard query strings or POST bodies.
        """
        json_str = json.dumps(payload)
        return base64.b64encode(json_str.encode('utf-8')).decode('UTF-8')
    
    xǁPlaywrightB3DataSourceǁ_create_token__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPlaywrightB3DataSourceǁ_create_token__mutmut_1': xǁPlaywrightB3DataSourceǁ_create_token__mutmut_1, 
        'xǁPlaywrightB3DataSourceǁ_create_token__mutmut_2': xǁPlaywrightB3DataSourceǁ_create_token__mutmut_2, 
        'xǁPlaywrightB3DataSourceǁ_create_token__mutmut_3': xǁPlaywrightB3DataSourceǁ_create_token__mutmut_3, 
        'xǁPlaywrightB3DataSourceǁ_create_token__mutmut_4': xǁPlaywrightB3DataSourceǁ_create_token__mutmut_4, 
        'xǁPlaywrightB3DataSourceǁ_create_token__mutmut_5': xǁPlaywrightB3DataSourceǁ_create_token__mutmut_5, 
        'xǁPlaywrightB3DataSourceǁ_create_token__mutmut_6': xǁPlaywrightB3DataSourceǁ_create_token__mutmut_6, 
        'xǁPlaywrightB3DataSourceǁ_create_token__mutmut_7': xǁPlaywrightB3DataSourceǁ_create_token__mutmut_7, 
        'xǁPlaywrightB3DataSourceǁ_create_token__mutmut_8': xǁPlaywrightB3DataSourceǁ_create_token__mutmut_8, 
        'xǁPlaywrightB3DataSourceǁ_create_token__mutmut_9': xǁPlaywrightB3DataSourceǁ_create_token__mutmut_9
    }
    xǁPlaywrightB3DataSourceǁ_create_token__mutmut_orig.__name__ = 'xǁPlaywrightB3DataSourceǁ_create_token'

    async def _get_context(self):
        args = []# type: ignore
        kwargs = {}# type: ignore
        return await _mutmut_trampoline(object.__getattribute__(self, 'xǁPlaywrightB3DataSourceǁ_get_context__mutmut_orig'), object.__getattribute__(self, 'xǁPlaywrightB3DataSourceǁ_get_context__mutmut_mutants'), args, kwargs, self)

    async def xǁPlaywrightB3DataSourceǁ_get_context__mutmut_orig(self):
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

    async def xǁPlaywrightB3DataSourceǁ_get_context__mutmut_1(self):
        """Secures an active browser context for API interaction.

        Supports both managed sessions (via __aenter__) and one-off 
        calls (used primarily in legacy tests or simple CLI tools).
        """
        if self._context:
            return self._context, True # (context, is_temporary_marker)
        
        # Fallback for unmanaged sessions: create a temporary browser instance.
        p = await async_playwright().start()
        b = await p.chromium.launch(headless=self.headless)
        c = await b.new_context(
             user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        return c, True

    async def xǁPlaywrightB3DataSourceǁ_get_context__mutmut_2(self):
        """Secures an active browser context for API interaction.

        Supports both managed sessions (via __aenter__) and one-off 
        calls (used primarily in legacy tests or simple CLI tools).
        """
        if self._context:
            return self._context, False # (context, is_temporary_marker)
        
        # Fallback for unmanaged sessions: create a temporary browser instance.
        p = None
        b = await p.chromium.launch(headless=self.headless)
        c = await b.new_context(
             user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        return c, True

    async def xǁPlaywrightB3DataSourceǁ_get_context__mutmut_3(self):
        """Secures an active browser context for API interaction.

        Supports both managed sessions (via __aenter__) and one-off 
        calls (used primarily in legacy tests or simple CLI tools).
        """
        if self._context:
            return self._context, False # (context, is_temporary_marker)
        
        # Fallback for unmanaged sessions: create a temporary browser instance.
        p = await async_playwright().start()
        b = None
        c = await b.new_context(
             user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        return c, True

    async def xǁPlaywrightB3DataSourceǁ_get_context__mutmut_4(self):
        """Secures an active browser context for API interaction.

        Supports both managed sessions (via __aenter__) and one-off 
        calls (used primarily in legacy tests or simple CLI tools).
        """
        if self._context:
            return self._context, False # (context, is_temporary_marker)
        
        # Fallback for unmanaged sessions: create a temporary browser instance.
        p = await async_playwright().start()
        b = await p.chromium.launch(headless=None)
        c = await b.new_context(
             user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        return c, True

    async def xǁPlaywrightB3DataSourceǁ_get_context__mutmut_5(self):
        """Secures an active browser context for API interaction.

        Supports both managed sessions (via __aenter__) and one-off 
        calls (used primarily in legacy tests or simple CLI tools).
        """
        if self._context:
            return self._context, False # (context, is_temporary_marker)
        
        # Fallback for unmanaged sessions: create a temporary browser instance.
        p = await async_playwright().start()
        b = await p.chromium.launch(headless=self.headless)
        c = None
        return c, True

    async def xǁPlaywrightB3DataSourceǁ_get_context__mutmut_6(self):
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
             user_agent=None
        )
        return c, True

    async def xǁPlaywrightB3DataSourceǁ_get_context__mutmut_7(self):
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
             user_agent="XXMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36XX"
        )
        return c, True

    async def xǁPlaywrightB3DataSourceǁ_get_context__mutmut_8(self):
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
             user_agent="mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/120.0.0.0 safari/537.36"
        )
        return c, True

    async def xǁPlaywrightB3DataSourceǁ_get_context__mutmut_9(self):
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
             user_agent="MOZILLA/5.0 (WINDOWS NT 10.0; WIN64; X64) APPLEWEBKIT/537.36 (KHTML, LIKE GECKO) CHROME/120.0.0.0 SAFARI/537.36"
        )
        return c, True

    async def xǁPlaywrightB3DataSourceǁ_get_context__mutmut_10(self):
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
        return c, False
    
    xǁPlaywrightB3DataSourceǁ_get_context__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPlaywrightB3DataSourceǁ_get_context__mutmut_1': xǁPlaywrightB3DataSourceǁ_get_context__mutmut_1, 
        'xǁPlaywrightB3DataSourceǁ_get_context__mutmut_2': xǁPlaywrightB3DataSourceǁ_get_context__mutmut_2, 
        'xǁPlaywrightB3DataSourceǁ_get_context__mutmut_3': xǁPlaywrightB3DataSourceǁ_get_context__mutmut_3, 
        'xǁPlaywrightB3DataSourceǁ_get_context__mutmut_4': xǁPlaywrightB3DataSourceǁ_get_context__mutmut_4, 
        'xǁPlaywrightB3DataSourceǁ_get_context__mutmut_5': xǁPlaywrightB3DataSourceǁ_get_context__mutmut_5, 
        'xǁPlaywrightB3DataSourceǁ_get_context__mutmut_6': xǁPlaywrightB3DataSourceǁ_get_context__mutmut_6, 
        'xǁPlaywrightB3DataSourceǁ_get_context__mutmut_7': xǁPlaywrightB3DataSourceǁ_get_context__mutmut_7, 
        'xǁPlaywrightB3DataSourceǁ_get_context__mutmut_8': xǁPlaywrightB3DataSourceǁ_get_context__mutmut_8, 
        'xǁPlaywrightB3DataSourceǁ_get_context__mutmut_9': xǁPlaywrightB3DataSourceǁ_get_context__mutmut_9, 
        'xǁPlaywrightB3DataSourceǁ_get_context__mutmut_10': xǁPlaywrightB3DataSourceǁ_get_context__mutmut_10
    }
    xǁPlaywrightB3DataSourceǁ_get_context__mutmut_orig.__name__ = 'xǁPlaywrightB3DataSourceǁ_get_context'

    async def fetch_initial_companies(self) -> List[Dict[str, Any]]:
        args = []# type: ignore
        kwargs = {}# type: ignore
        return await _mutmut_trampoline(object.__getattribute__(self, 'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_orig'), object.__getattribute__(self, 'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_mutants'), args, kwargs, self)

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_orig(self) -> List[Dict[str, Any]]:
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_1(self) -> List[Dict[str, Any]]:
        """Retrieves the full list of companies currently listed on B3.

        Returns:
            List[Dict[str, Any]]: Raw records from the discovery endpoint.

        Raises:
            B3RateLimitExceededError: If the 429 quota is reached.
        """
        all_companies = None
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_2(self) -> List[Dict[str, Any]]:
        """Retrieves the full list of companies currently listed on B3.

        Returns:
            List[Dict[str, Any]]: Raw records from the discovery endpoint.

        Raises:
            B3RateLimitExceededError: If the 429 quota is reached.
        """
        all_companies = []
        context, is_temp = None
        
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_3(self) -> List[Dict[str, Any]]:
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
                page = None
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_4(self) -> List[Dict[str, Any]]:
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
                await page.goto(None, wait_until="networkidle")
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_5(self) -> List[Dict[str, Any]]:
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
                await page.goto(self.homepage_url, wait_until=None)
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_6(self) -> List[Dict[str, Any]]:
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
                await page.goto(wait_until="networkidle")
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_7(self) -> List[Dict[str, Any]]:
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
                await page.goto(self.homepage_url, )
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_8(self) -> List[Dict[str, Any]]:
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
                await page.goto(self.homepage_url, wait_until="XXnetworkidleXX")
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_9(self) -> List[Dict[str, Any]]:
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
                await page.goto(self.homepage_url, wait_until="NETWORKIDLE")
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_10(self) -> List[Dict[str, Any]]:
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
            page_num = None 
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_11(self) -> List[Dict[str, Any]]:
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
            page_num = +1 
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_12(self) -> List[Dict[str, Any]]:
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
            page_num = -2 
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_13(self) -> List[Dict[str, Any]]:
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
            total_pages = None

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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_14(self) -> List[Dict[str, Any]]:
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
            total_pages = +1

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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_15(self) -> List[Dict[str, Any]]:
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
            total_pages = -2

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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_16(self) -> List[Dict[str, Any]]:
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

            while page_num < total_pages:
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_17(self) -> List[Dict[str, Any]]:
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
                payload = None
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_18(self) -> List[Dict[str, Any]]:
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
                payload = {"XXlanguageXX": "pt-br", "pageNumber": page_num, "pageSize": 20}
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_19(self) -> List[Dict[str, Any]]:
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
                payload = {"LANGUAGE": "pt-br", "pageNumber": page_num, "pageSize": 20}
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_20(self) -> List[Dict[str, Any]]:
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
                payload = {"language": "XXpt-brXX", "pageNumber": page_num, "pageSize": 20}
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_21(self) -> List[Dict[str, Any]]:
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
                payload = {"language": "PT-BR", "pageNumber": page_num, "pageSize": 20}
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_22(self) -> List[Dict[str, Any]]:
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
                payload = {"language": "pt-br", "XXpageNumberXX": page_num, "pageSize": 20}
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_23(self) -> List[Dict[str, Any]]:
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
                payload = {"language": "pt-br", "pagenumber": page_num, "pageSize": 20}
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_24(self) -> List[Dict[str, Any]]:
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
                payload = {"language": "pt-br", "PAGENUMBER": page_num, "pageSize": 20}
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_25(self) -> List[Dict[str, Any]]:
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
                payload = {"language": "pt-br", "pageNumber": page_num, "XXpageSizeXX": 20}
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_26(self) -> List[Dict[str, Any]]:
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
                payload = {"language": "pt-br", "pageNumber": page_num, "pagesize": 20}
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_27(self) -> List[Dict[str, Any]]:
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
                payload = {"language": "pt-br", "pageNumber": page_num, "PAGESIZE": 20}
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_28(self) -> List[Dict[str, Any]]:
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
                payload = {"language": "pt-br", "pageNumber": page_num, "pageSize": 21}
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_29(self) -> List[Dict[str, Any]]:
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
                token = None
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_30(self) -> List[Dict[str, Any]]:
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
                token = self._create_token(None)
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_31(self) -> List[Dict[str, Any]]:
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
                endpoint = None

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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_32(self) -> List[Dict[str, Any]]:
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

                response = None
                
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_33(self) -> List[Dict[str, Any]]:
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
                    None,
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_34(self) -> List[Dict[str, Any]]:
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
                    headers=None
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_35(self) -> List[Dict[str, Any]]:
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_36(self) -> List[Dict[str, Any]]:
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_37(self) -> List[Dict[str, Any]]:
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
                        "XXRefererXX": "https://sistemaswebb3-listados.b3.com.br/",
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_38(self) -> List[Dict[str, Any]]:
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
                        "referer": "https://sistemaswebb3-listados.b3.com.br/",
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_39(self) -> List[Dict[str, Any]]:
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
                        "REFERER": "https://sistemaswebb3-listados.b3.com.br/",
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_40(self) -> List[Dict[str, Any]]:
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
                        "Referer": "XXhttps://sistemaswebb3-listados.b3.com.br/XX",
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_41(self) -> List[Dict[str, Any]]:
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
                        "Referer": "HTTPS://SISTEMASWEBB3-LISTADOS.B3.COM.BR/",
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_42(self) -> List[Dict[str, Any]]:
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
                        "XXX-DtRefererXX": self.homepage_url
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_43(self) -> List[Dict[str, Any]]:
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
                        "x-dtreferer": self.homepage_url
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_44(self) -> List[Dict[str, Any]]:
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
                        "X-DTREFERER": self.homepage_url
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_45(self) -> List[Dict[str, Any]]:
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
                
                if response.status != 429:
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_46(self) -> List[Dict[str, Any]]:
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
                
                if response.status == 430:
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_47(self) -> List[Dict[str, Any]]:
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
                        None
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_48(self) -> List[Dict[str, Any]]:
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
                
                if response.ok:
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_49(self) -> List[Dict[str, Any]]:
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
                        None
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_50(self) -> List[Dict[str, Any]]:
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

                body = None
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_51(self) -> List[Dict[str, Any]]:
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
                    direction=None, context="b3_initial", payload_size=len(body)
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_52(self) -> List[Dict[str, Any]]:
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
                    direction="inbound", context=None, payload_size=len(body)
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_53(self) -> List[Dict[str, Any]]:
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
                    direction="inbound", context="b3_initial", payload_size=None
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_54(self) -> List[Dict[str, Any]]:
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
                    context="b3_initial", payload_size=len(body)
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_55(self) -> List[Dict[str, Any]]:
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
                    direction="inbound", payload_size=len(body)
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_56(self) -> List[Dict[str, Any]]:
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
                    direction="inbound", context="b3_initial", )

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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_57(self) -> List[Dict[str, Any]]:
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
                    direction="XXinboundXX", context="b3_initial", payload_size=len(body)
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_58(self) -> List[Dict[str, Any]]:
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
                    direction="INBOUND", context="b3_initial", payload_size=len(body)
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_59(self) -> List[Dict[str, Any]]:
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
                    direction="inbound", context="XXb3_initialXX", payload_size=len(body)
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_60(self) -> List[Dict[str, Any]]:
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
                    direction="inbound", context="B3_INITIAL", payload_size=len(body)
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

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_61(self) -> List[Dict[str, Any]]:
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

                data = None
                if page_num == 1:
                    total_pages = data.get("page", {}).get("totalPages", 1)

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_62(self) -> List[Dict[str, Any]]:
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

                data = json.loads(None)
                if page_num == 1:
                    total_pages = data.get("page", {}).get("totalPages", 1)

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_63(self) -> List[Dict[str, Any]]:
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
                if page_num != 1:
                    total_pages = data.get("page", {}).get("totalPages", 1)

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_64(self) -> List[Dict[str, Any]]:
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
                if page_num == 2:
                    total_pages = data.get("page", {}).get("totalPages", 1)

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_65(self) -> List[Dict[str, Any]]:
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
                    total_pages = None

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_66(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", {}).get(None, 1)

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_67(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", {}).get("totalPages", None)

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_68(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", {}).get(1)

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_69(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", {}).get("totalPages", )

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_70(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get(None, {}).get("totalPages", 1)

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_71(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", None).get("totalPages", 1)

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_72(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get({}).get("totalPages", 1)

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_73(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", ).get("totalPages", 1)

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_74(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("XXpageXX", {}).get("totalPages", 1)

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_75(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("PAGE", {}).get("totalPages", 1)

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_76(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", {}).get("XXtotalPagesXX", 1)

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_77(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", {}).get("totalpages", 1)

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_78(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", {}).get("TOTALPAGES", 1)

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_79(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", {}).get("totalPages", 2)

                companies = data.get("results", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_80(self) -> List[Dict[str, Any]]:
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

                companies = None
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_81(self) -> List[Dict[str, Any]]:
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

                companies = data.get(None, [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_82(self) -> List[Dict[str, Any]]:
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

                companies = data.get("results", None)
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_83(self) -> List[Dict[str, Any]]:
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

                companies = data.get([])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_84(self) -> List[Dict[str, Any]]:
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

                companies = data.get("results", )
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_85(self) -> List[Dict[str, Any]]:
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

                companies = data.get("XXresultsXX", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_86(self) -> List[Dict[str, Any]]:
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

                companies = data.get("RESULTS", [])
                all_companies.extend(companies)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_87(self) -> List[Dict[str, Any]]:
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
                all_companies.extend(None)
                page_num += 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_88(self) -> List[Dict[str, Any]]:
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
                page_num = 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_89(self) -> List[Dict[str, Any]]:
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
                page_num -= 1
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies

    async def xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_90(self) -> List[Dict[str, Any]]:
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
                page_num += 2
        finally:
            if is_temp:
                await context.browser.close()

        return all_companies
    
    xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_1': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_1, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_2': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_2, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_3': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_3, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_4': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_4, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_5': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_5, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_6': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_6, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_7': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_7, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_8': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_8, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_9': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_9, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_10': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_10, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_11': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_11, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_12': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_12, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_13': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_13, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_14': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_14, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_15': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_15, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_16': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_16, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_17': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_17, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_18': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_18, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_19': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_19, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_20': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_20, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_21': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_21, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_22': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_22, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_23': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_23, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_24': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_24, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_25': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_25, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_26': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_26, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_27': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_27, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_28': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_28, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_29': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_29, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_30': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_30, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_31': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_31, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_32': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_32, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_33': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_33, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_34': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_34, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_35': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_35, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_36': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_36, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_37': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_37, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_38': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_38, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_39': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_39, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_40': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_40, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_41': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_41, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_42': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_42, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_43': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_43, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_44': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_44, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_45': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_45, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_46': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_46, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_47': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_47, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_48': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_48, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_49': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_49, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_50': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_50, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_51': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_51, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_52': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_52, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_53': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_53, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_54': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_54, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_55': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_55, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_56': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_56, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_57': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_57, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_58': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_58, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_59': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_59, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_60': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_60, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_61': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_61, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_62': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_62, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_63': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_63, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_64': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_64, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_65': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_65, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_66': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_66, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_67': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_67, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_68': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_68, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_69': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_69, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_70': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_70, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_71': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_71, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_72': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_72, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_73': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_73, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_74': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_74, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_75': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_75, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_76': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_76, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_77': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_77, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_78': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_78, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_79': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_79, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_80': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_80, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_81': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_81, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_82': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_82, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_83': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_83, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_84': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_84, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_85': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_85, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_86': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_86, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_87': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_87, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_88': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_88, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_89': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_89, 
        'xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_90': xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_90
    }
    xǁPlaywrightB3DataSourceǁfetch_initial_companies__mutmut_orig.__name__ = 'xǁPlaywrightB3DataSourceǁfetch_initial_companies'

    async def fetch_company_details(self, cvm_code: str) -> Dict[str, Any]:
        args = [cvm_code]# type: ignore
        kwargs = {}# type: ignore
        return await _mutmut_trampoline(object.__getattribute__(self, 'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_orig'), object.__getattribute__(self, 'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_mutants'), args, kwargs, self)

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_orig(self, cvm_code: str) -> Dict[str, Any]:
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_1(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches granular metadata for a specific issuer by its CVM code.

        This endpoint provides deeper attributes like industry classification 
        and CNPJ that are missing from the initial summary list.
        """
        endpoint_base = None
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_2(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches granular metadata for a specific issuer by its CVM code.

        This endpoint provides deeper attributes like industry classification 
        and CNPJ that are missing from the initial summary list.
        """
        endpoint_base = settings.b3.detail_api
        payload = None
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_3(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches granular metadata for a specific issuer by its CVM code.

        This endpoint provides deeper attributes like industry classification 
        and CNPJ that are missing from the initial summary list.
        """
        endpoint_base = settings.b3.detail_api
        payload = {"XXcodeCVMXX": str(cvm_code), "language": "pt-br"}
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_4(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches granular metadata for a specific issuer by its CVM code.

        This endpoint provides deeper attributes like industry classification 
        and CNPJ that are missing from the initial summary list.
        """
        endpoint_base = settings.b3.detail_api
        payload = {"codecvm": str(cvm_code), "language": "pt-br"}
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_5(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches granular metadata for a specific issuer by its CVM code.

        This endpoint provides deeper attributes like industry classification 
        and CNPJ that are missing from the initial summary list.
        """
        endpoint_base = settings.b3.detail_api
        payload = {"CODECVM": str(cvm_code), "language": "pt-br"}
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_6(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches granular metadata for a specific issuer by its CVM code.

        This endpoint provides deeper attributes like industry classification 
        and CNPJ that are missing from the initial summary list.
        """
        endpoint_base = settings.b3.detail_api
        payload = {"codeCVM": str(None), "language": "pt-br"}
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_7(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches granular metadata for a specific issuer by its CVM code.

        This endpoint provides deeper attributes like industry classification 
        and CNPJ that are missing from the initial summary list.
        """
        endpoint_base = settings.b3.detail_api
        payload = {"codeCVM": str(cvm_code), "XXlanguageXX": "pt-br"}
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_8(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches granular metadata for a specific issuer by its CVM code.

        This endpoint provides deeper attributes like industry classification 
        and CNPJ that are missing from the initial summary list.
        """
        endpoint_base = settings.b3.detail_api
        payload = {"codeCVM": str(cvm_code), "LANGUAGE": "pt-br"}
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_9(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches granular metadata for a specific issuer by its CVM code.

        This endpoint provides deeper attributes like industry classification 
        and CNPJ that are missing from the initial summary list.
        """
        endpoint_base = settings.b3.detail_api
        payload = {"codeCVM": str(cvm_code), "language": "XXpt-brXX"}
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_10(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches granular metadata for a specific issuer by its CVM code.

        This endpoint provides deeper attributes like industry classification 
        and CNPJ that are missing from the initial summary list.
        """
        endpoint_base = settings.b3.detail_api
        payload = {"codeCVM": str(cvm_code), "language": "PT-BR"}
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_11(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches granular metadata for a specific issuer by its CVM code.

        This endpoint provides deeper attributes like industry classification 
        and CNPJ that are missing from the initial summary list.
        """
        endpoint_base = settings.b3.detail_api
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = None
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_12(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches granular metadata for a specific issuer by its CVM code.

        This endpoint provides deeper attributes like industry classification 
        and CNPJ that are missing from the initial summary list.
        """
        endpoint_base = settings.b3.detail_api
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(None)
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_13(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches granular metadata for a specific issuer by its CVM code.

        This endpoint provides deeper attributes like industry classification 
        and CNPJ that are missing from the initial summary list.
        """
        endpoint_base = settings.b3.detail_api
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        context, is_temp = None

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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_14(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches granular metadata for a specific issuer by its CVM code.

        This endpoint provides deeper attributes like industry classification 
        and CNPJ that are missing from the initial summary list.
        """
        endpoint_base = settings.b3.detail_api
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        context, is_temp = await self._get_context()

        try:
            response = None
            
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_15(self, cvm_code: str) -> Dict[str, Any]:
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
                None,
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_16(self, cvm_code: str) -> Dict[str, Any]:
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
                headers=None
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_17(self, cvm_code: str) -> Dict[str, Any]:
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_18(self, cvm_code: str) -> Dict[str, Any]:
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_19(self, cvm_code: str) -> Dict[str, Any]:
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
                    "XXRefererXX": "https://sistemaswebb3-listados.b3.com.br/",
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_20(self, cvm_code: str) -> Dict[str, Any]:
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
                    "referer": "https://sistemaswebb3-listados.b3.com.br/",
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_21(self, cvm_code: str) -> Dict[str, Any]:
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
                    "REFERER": "https://sistemaswebb3-listados.b3.com.br/",
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_22(self, cvm_code: str) -> Dict[str, Any]:
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
                    "Referer": "XXhttps://sistemaswebb3-listados.b3.com.br/XX",
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_23(self, cvm_code: str) -> Dict[str, Any]:
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
                    "Referer": "HTTPS://SISTEMASWEBB3-LISTADOS.B3.COM.BR/",
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_24(self, cvm_code: str) -> Dict[str, Any]:
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
                    "XXX-DtRefererXX": self.homepage_url
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_25(self, cvm_code: str) -> Dict[str, Any]:
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
                    "x-dtreferer": self.homepage_url
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_26(self, cvm_code: str) -> Dict[str, Any]:
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
                    "X-DTREFERER": self.homepage_url
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_27(self, cvm_code: str) -> Dict[str, Any]:
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
            
            if response.status != 429:
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_28(self, cvm_code: str) -> Dict[str, Any]:
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
            
            if response.status == 430:
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_29(self, cvm_code: str) -> Dict[str, Any]:
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
                    None
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_30(self, cvm_code: str) -> Dict[str, Any]:
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

            if response.ok:
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_31(self, cvm_code: str) -> Dict[str, Any]:
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
                    None
                )
            
            body = await response.body()
            self._telemetry.increment_network_transmit_bytes(
                direction="inbound", context="b3_detail", payload_size=len(body)
            )
            
            return json.loads(body)
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_32(self, cvm_code: str) -> Dict[str, Any]:
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
            
            body = None
            self._telemetry.increment_network_transmit_bytes(
                direction="inbound", context="b3_detail", payload_size=len(body)
            )
            
            return json.loads(body)
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_33(self, cvm_code: str) -> Dict[str, Any]:
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
                direction=None, context="b3_detail", payload_size=len(body)
            )
            
            return json.loads(body)
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_34(self, cvm_code: str) -> Dict[str, Any]:
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
                direction="inbound", context=None, payload_size=len(body)
            )
            
            return json.loads(body)
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_35(self, cvm_code: str) -> Dict[str, Any]:
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
                direction="inbound", context="b3_detail", payload_size=None
            )
            
            return json.loads(body)
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_36(self, cvm_code: str) -> Dict[str, Any]:
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
                context="b3_detail", payload_size=len(body)
            )
            
            return json.loads(body)
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_37(self, cvm_code: str) -> Dict[str, Any]:
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
                direction="inbound", payload_size=len(body)
            )
            
            return json.loads(body)
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_38(self, cvm_code: str) -> Dict[str, Any]:
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
                direction="inbound", context="b3_detail", )
            
            return json.loads(body)
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_39(self, cvm_code: str) -> Dict[str, Any]:
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
                direction="XXinboundXX", context="b3_detail", payload_size=len(body)
            )
            
            return json.loads(body)
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_40(self, cvm_code: str) -> Dict[str, Any]:
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
                direction="INBOUND", context="b3_detail", payload_size=len(body)
            )
            
            return json.loads(body)
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_41(self, cvm_code: str) -> Dict[str, Any]:
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
                direction="inbound", context="XXb3_detailXX", payload_size=len(body)
            )
            
            return json.loads(body)
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_42(self, cvm_code: str) -> Dict[str, Any]:
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
                direction="inbound", context="B3_DETAIL", payload_size=len(body)
            )
            
            return json.loads(body)
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_43(self, cvm_code: str) -> Dict[str, Any]:
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
            
            return json.loads(None)
        finally:
            if is_temp:
                await context.browser.close()
    
    xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_1': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_1, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_2': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_2, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_3': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_3, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_4': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_4, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_5': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_5, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_6': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_6, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_7': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_7, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_8': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_8, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_9': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_9, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_10': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_10, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_11': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_11, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_12': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_12, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_13': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_13, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_14': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_14, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_15': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_15, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_16': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_16, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_17': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_17, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_18': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_18, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_19': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_19, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_20': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_20, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_21': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_21, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_22': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_22, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_23': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_23, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_24': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_24, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_25': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_25, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_26': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_26, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_27': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_27, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_28': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_28, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_29': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_29, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_30': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_30, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_31': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_31, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_32': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_32, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_33': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_33, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_34': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_34, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_35': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_35, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_36': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_36, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_37': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_37, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_38': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_38, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_39': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_39, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_40': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_40, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_41': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_41, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_42': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_42, 
        'xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_43': xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_43
    }
    xǁPlaywrightB3DataSourceǁfetch_company_details__mutmut_orig.__name__ = 'xǁPlaywrightB3DataSourceǁfetch_company_details'

    async def fetch_company_financials(self, cvm_code: str) -> Dict[str, Any]:
        args = [cvm_code]# type: ignore
        kwargs = {}# type: ignore
        return await _mutmut_trampoline(object.__getattribute__(self, 'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_orig'), object.__getattribute__(self, 'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_mutants'), args, kwargs, self)

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_orig(self, cvm_code: str) -> Dict[str, Any]:
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_1(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches the latest financial indicators for an issuer.

        Enables data quality checks on the financial health of the issuer 
        during the domain synchronization cycle.
        """
        endpoint_base = None
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_2(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches the latest financial indicators for an issuer.

        Enables data quality checks on the financial health of the issuer 
        during the domain synchronization cycle.
        """
        endpoint_base = settings.b3.financial_api
        payload = None
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_3(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches the latest financial indicators for an issuer.

        Enables data quality checks on the financial health of the issuer 
        during the domain synchronization cycle.
        """
        endpoint_base = settings.b3.financial_api
        payload = {"XXcodeCVMXX": str(cvm_code), "language": "pt-br"}
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_4(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches the latest financial indicators for an issuer.

        Enables data quality checks on the financial health of the issuer 
        during the domain synchronization cycle.
        """
        endpoint_base = settings.b3.financial_api
        payload = {"codecvm": str(cvm_code), "language": "pt-br"}
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_5(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches the latest financial indicators for an issuer.

        Enables data quality checks on the financial health of the issuer 
        during the domain synchronization cycle.
        """
        endpoint_base = settings.b3.financial_api
        payload = {"CODECVM": str(cvm_code), "language": "pt-br"}
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_6(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches the latest financial indicators for an issuer.

        Enables data quality checks on the financial health of the issuer 
        during the domain synchronization cycle.
        """
        endpoint_base = settings.b3.financial_api
        payload = {"codeCVM": str(None), "language": "pt-br"}
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_7(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches the latest financial indicators for an issuer.

        Enables data quality checks on the financial health of the issuer 
        during the domain synchronization cycle.
        """
        endpoint_base = settings.b3.financial_api
        payload = {"codeCVM": str(cvm_code), "XXlanguageXX": "pt-br"}
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_8(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches the latest financial indicators for an issuer.

        Enables data quality checks on the financial health of the issuer 
        during the domain synchronization cycle.
        """
        endpoint_base = settings.b3.financial_api
        payload = {"codeCVM": str(cvm_code), "LANGUAGE": "pt-br"}
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_9(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches the latest financial indicators for an issuer.

        Enables data quality checks on the financial health of the issuer 
        during the domain synchronization cycle.
        """
        endpoint_base = settings.b3.financial_api
        payload = {"codeCVM": str(cvm_code), "language": "XXpt-brXX"}
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_10(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches the latest financial indicators for an issuer.

        Enables data quality checks on the financial health of the issuer 
        during the domain synchronization cycle.
        """
        endpoint_base = settings.b3.financial_api
        payload = {"codeCVM": str(cvm_code), "language": "PT-BR"}
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_11(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches the latest financial indicators for an issuer.

        Enables data quality checks on the financial health of the issuer 
        during the domain synchronization cycle.
        """
        endpoint_base = settings.b3.financial_api
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = None
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_12(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches the latest financial indicators for an issuer.

        Enables data quality checks on the financial health of the issuer 
        during the domain synchronization cycle.
        """
        endpoint_base = settings.b3.financial_api
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(None)
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_13(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches the latest financial indicators for an issuer.

        Enables data quality checks on the financial health of the issuer 
        during the domain synchronization cycle.
        """
        endpoint_base = settings.b3.financial_api
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        context, is_temp = None

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

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_14(self, cvm_code: str) -> Dict[str, Any]:
        """Fetches the latest financial indicators for an issuer.

        Enables data quality checks on the financial health of the issuer 
        during the domain synchronization cycle.
        """
        endpoint_base = settings.b3.financial_api
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        context, is_temp = await self._get_context()

        try:
            response = None
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
            return await response.json()
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_15(self, cvm_code: str) -> Dict[str, Any]:
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
                None,
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_16(self, cvm_code: str) -> Dict[str, Any]:
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
                headers=None
            )
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
            return await response.json()
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_17(self, cvm_code: str) -> Dict[str, Any]:
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

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_18(self, cvm_code: str) -> Dict[str, Any]:
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
                )
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
            return await response.json()
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_19(self, cvm_code: str) -> Dict[str, Any]:
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
                    "XXRefererXX": "https://sistemaswebb3-listados.b3.com.br/",
                    "X-DtReferer": self.homepage_url
                }
            )
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
            return await response.json()
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_20(self, cvm_code: str) -> Dict[str, Any]:
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
                    "referer": "https://sistemaswebb3-listados.b3.com.br/",
                    "X-DtReferer": self.homepage_url
                }
            )
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
            return await response.json()
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_21(self, cvm_code: str) -> Dict[str, Any]:
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
                    "REFERER": "https://sistemaswebb3-listados.b3.com.br/",
                    "X-DtReferer": self.homepage_url
                }
            )
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
            return await response.json()
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_22(self, cvm_code: str) -> Dict[str, Any]:
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
                    "Referer": "XXhttps://sistemaswebb3-listados.b3.com.br/XX",
                    "X-DtReferer": self.homepage_url
                }
            )
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
            return await response.json()
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_23(self, cvm_code: str) -> Dict[str, Any]:
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
                    "Referer": "HTTPS://SISTEMASWEBB3-LISTADOS.B3.COM.BR/",
                    "X-DtReferer": self.homepage_url
                }
            )
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
            return await response.json()
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_24(self, cvm_code: str) -> Dict[str, Any]:
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
                    "XXX-DtRefererXX": self.homepage_url
                }
            )
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
            return await response.json()
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_25(self, cvm_code: str) -> Dict[str, Any]:
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
                    "x-dtreferer": self.homepage_url
                }
            )
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
            return await response.json()
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_26(self, cvm_code: str) -> Dict[str, Any]:
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
                    "X-DTREFERER": self.homepage_url
                }
            )
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
            return await response.json()
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_27(self, cvm_code: str) -> Dict[str, Any]:
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
            if response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
            return await response.json()
        finally:
            if is_temp:
                await context.browser.close()

    async def xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_28(self, cvm_code: str) -> Dict[str, Any]:
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
                raise Exception(None)
            return await response.json()
        finally:
            if is_temp:
                await context.browser.close()
    
    xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_1': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_1, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_2': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_2, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_3': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_3, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_4': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_4, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_5': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_5, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_6': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_6, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_7': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_7, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_8': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_8, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_9': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_9, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_10': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_10, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_11': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_11, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_12': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_12, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_13': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_13, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_14': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_14, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_15': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_15, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_16': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_16, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_17': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_17, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_18': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_18, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_19': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_19, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_20': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_20, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_21': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_21, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_22': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_22, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_23': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_23, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_24': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_24, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_25': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_25, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_26': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_26, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_27': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_27, 
        'xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_28': xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_28
    }
    xǁPlaywrightB3DataSourceǁfetch_company_financials__mutmut_orig.__name__ = 'xǁPlaywrightB3DataSourceǁfetch_company_financials'
