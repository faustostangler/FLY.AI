from typing import List, Dict, Any
from playwright.async_api import async_playwright, Page, BrowserContext
from domain.ports.scrapers.b3_scraper_port import B3ScraperPort
import json
import base64
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

class PlaywrightB3Scraper(B3ScraperPort):
    def __init__(self, headless: bool = True):
        args = [headless]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPlaywrightB3Scraperǁ__init____mutmut_orig'), object.__getattribute__(self, 'xǁPlaywrightB3Scraperǁ__init____mutmut_mutants'), args, kwargs, self)
    def xǁPlaywrightB3Scraperǁ__init____mutmut_orig(self, headless: bool = True):
        self.headless = headless
        self.homepage_url = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/?language=pt-br"
        self.initial_companies_api = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetInitialCompanies/"
        
    def xǁPlaywrightB3Scraperǁ__init____mutmut_1(self, headless: bool = False):
        self.headless = headless
        self.homepage_url = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/?language=pt-br"
        self.initial_companies_api = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetInitialCompanies/"
        
    def xǁPlaywrightB3Scraperǁ__init____mutmut_2(self, headless: bool = True):
        self.headless = None
        self.homepage_url = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/?language=pt-br"
        self.initial_companies_api = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetInitialCompanies/"
        
    def xǁPlaywrightB3Scraperǁ__init____mutmut_3(self, headless: bool = True):
        self.headless = headless
        self.homepage_url = None
        self.initial_companies_api = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetInitialCompanies/"
        
    def xǁPlaywrightB3Scraperǁ__init____mutmut_4(self, headless: bool = True):
        self.headless = headless
        self.homepage_url = "XXhttps://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/?language=pt-brXX"
        self.initial_companies_api = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetInitialCompanies/"
        
    def xǁPlaywrightB3Scraperǁ__init____mutmut_5(self, headless: bool = True):
        self.headless = headless
        self.homepage_url = "https://sistemaswebb3-listados.b3.com.br/listedcompaniespage/?language=pt-br"
        self.initial_companies_api = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetInitialCompanies/"
        
    def xǁPlaywrightB3Scraperǁ__init____mutmut_6(self, headless: bool = True):
        self.headless = headless
        self.homepage_url = "HTTPS://SISTEMASWEBB3-LISTADOS.B3.COM.BR/LISTEDCOMPANIESPAGE/?LANGUAGE=PT-BR"
        self.initial_companies_api = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetInitialCompanies/"
        
    def xǁPlaywrightB3Scraperǁ__init____mutmut_7(self, headless: bool = True):
        self.headless = headless
        self.homepage_url = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/?language=pt-br"
        self.initial_companies_api = None
        
    def xǁPlaywrightB3Scraperǁ__init____mutmut_8(self, headless: bool = True):
        self.headless = headless
        self.homepage_url = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/?language=pt-br"
        self.initial_companies_api = "XXhttps://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetInitialCompanies/XX"
        
    def xǁPlaywrightB3Scraperǁ__init____mutmut_9(self, headless: bool = True):
        self.headless = headless
        self.homepage_url = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/?language=pt-br"
        self.initial_companies_api = "https://sistemaswebb3-listados.b3.com.br/listedcompaniesproxy/companydatacall/getinitialcompanies/"
        
    def xǁPlaywrightB3Scraperǁ__init____mutmut_10(self, headless: bool = True):
        self.headless = headless
        self.homepage_url = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/?language=pt-br"
        self.initial_companies_api = "HTTPS://SISTEMASWEBB3-LISTADOS.B3.COM.BR/LISTEDCOMPANIESPROXY/COMPANYDATACALL/GETINITIALCOMPANIES/"
        
    
    xǁPlaywrightB3Scraperǁ__init____mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPlaywrightB3Scraperǁ__init____mutmut_1': xǁPlaywrightB3Scraperǁ__init____mutmut_1, 
        'xǁPlaywrightB3Scraperǁ__init____mutmut_2': xǁPlaywrightB3Scraperǁ__init____mutmut_2, 
        'xǁPlaywrightB3Scraperǁ__init____mutmut_3': xǁPlaywrightB3Scraperǁ__init____mutmut_3, 
        'xǁPlaywrightB3Scraperǁ__init____mutmut_4': xǁPlaywrightB3Scraperǁ__init____mutmut_4, 
        'xǁPlaywrightB3Scraperǁ__init____mutmut_5': xǁPlaywrightB3Scraperǁ__init____mutmut_5, 
        'xǁPlaywrightB3Scraperǁ__init____mutmut_6': xǁPlaywrightB3Scraperǁ__init____mutmut_6, 
        'xǁPlaywrightB3Scraperǁ__init____mutmut_7': xǁPlaywrightB3Scraperǁ__init____mutmut_7, 
        'xǁPlaywrightB3Scraperǁ__init____mutmut_8': xǁPlaywrightB3Scraperǁ__init____mutmut_8, 
        'xǁPlaywrightB3Scraperǁ__init____mutmut_9': xǁPlaywrightB3Scraperǁ__init____mutmut_9, 
        'xǁPlaywrightB3Scraperǁ__init____mutmut_10': xǁPlaywrightB3Scraperǁ__init____mutmut_10
    }
    xǁPlaywrightB3Scraperǁ__init____mutmut_orig.__name__ = 'xǁPlaywrightB3Scraperǁ__init__'
    def _create_token(self, payload: dict) -> str:
        args = [payload]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁPlaywrightB3Scraperǁ_create_token__mutmut_orig'), object.__getattribute__(self, 'xǁPlaywrightB3Scraperǁ_create_token__mutmut_mutants'), args, kwargs, self)
    def xǁPlaywrightB3Scraperǁ_create_token__mutmut_orig(self, payload: dict) -> str:
        """Helper to create the base64 token required by B3 endpoints."""
        json_str = json.dumps(payload)
        return base64.b64encode(json_str.encode('utf-8')).decode('utf-8')
    def xǁPlaywrightB3Scraperǁ_create_token__mutmut_1(self, payload: dict) -> str:
        """Helper to create the base64 token required by B3 endpoints."""
        json_str = None
        return base64.b64encode(json_str.encode('utf-8')).decode('utf-8')
    def xǁPlaywrightB3Scraperǁ_create_token__mutmut_2(self, payload: dict) -> str:
        """Helper to create the base64 token required by B3 endpoints."""
        json_str = json.dumps(None)
        return base64.b64encode(json_str.encode('utf-8')).decode('utf-8')
    def xǁPlaywrightB3Scraperǁ_create_token__mutmut_3(self, payload: dict) -> str:
        """Helper to create the base64 token required by B3 endpoints."""
        json_str = json.dumps(payload)
        return base64.b64encode(json_str.encode('utf-8')).decode(None)
    def xǁPlaywrightB3Scraperǁ_create_token__mutmut_4(self, payload: dict) -> str:
        """Helper to create the base64 token required by B3 endpoints."""
        json_str = json.dumps(payload)
        return base64.b64encode(None).decode('utf-8')
    def xǁPlaywrightB3Scraperǁ_create_token__mutmut_5(self, payload: dict) -> str:
        """Helper to create the base64 token required by B3 endpoints."""
        json_str = json.dumps(payload)
        return base64.b64encode(json_str.encode(None)).decode('utf-8')
    def xǁPlaywrightB3Scraperǁ_create_token__mutmut_6(self, payload: dict) -> str:
        """Helper to create the base64 token required by B3 endpoints."""
        json_str = json.dumps(payload)
        return base64.b64encode(json_str.encode('XXutf-8XX')).decode('utf-8')
    def xǁPlaywrightB3Scraperǁ_create_token__mutmut_7(self, payload: dict) -> str:
        """Helper to create the base64 token required by B3 endpoints."""
        json_str = json.dumps(payload)
        return base64.b64encode(json_str.encode('UTF-8')).decode('utf-8')
    def xǁPlaywrightB3Scraperǁ_create_token__mutmut_8(self, payload: dict) -> str:
        """Helper to create the base64 token required by B3 endpoints."""
        json_str = json.dumps(payload)
        return base64.b64encode(json_str.encode('utf-8')).decode('XXutf-8XX')
    def xǁPlaywrightB3Scraperǁ_create_token__mutmut_9(self, payload: dict) -> str:
        """Helper to create the base64 token required by B3 endpoints."""
        json_str = json.dumps(payload)
        return base64.b64encode(json_str.encode('utf-8')).decode('UTF-8')
    
    xǁPlaywrightB3Scraperǁ_create_token__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPlaywrightB3Scraperǁ_create_token__mutmut_1': xǁPlaywrightB3Scraperǁ_create_token__mutmut_1, 
        'xǁPlaywrightB3Scraperǁ_create_token__mutmut_2': xǁPlaywrightB3Scraperǁ_create_token__mutmut_2, 
        'xǁPlaywrightB3Scraperǁ_create_token__mutmut_3': xǁPlaywrightB3Scraperǁ_create_token__mutmut_3, 
        'xǁPlaywrightB3Scraperǁ_create_token__mutmut_4': xǁPlaywrightB3Scraperǁ_create_token__mutmut_4, 
        'xǁPlaywrightB3Scraperǁ_create_token__mutmut_5': xǁPlaywrightB3Scraperǁ_create_token__mutmut_5, 
        'xǁPlaywrightB3Scraperǁ_create_token__mutmut_6': xǁPlaywrightB3Scraperǁ_create_token__mutmut_6, 
        'xǁPlaywrightB3Scraperǁ_create_token__mutmut_7': xǁPlaywrightB3Scraperǁ_create_token__mutmut_7, 
        'xǁPlaywrightB3Scraperǁ_create_token__mutmut_8': xǁPlaywrightB3Scraperǁ_create_token__mutmut_8, 
        'xǁPlaywrightB3Scraperǁ_create_token__mutmut_9': xǁPlaywrightB3Scraperǁ_create_token__mutmut_9
    }
    xǁPlaywrightB3Scraperǁ_create_token__mutmut_orig.__name__ = 'xǁPlaywrightB3Scraperǁ_create_token'

    async def fetch_initial_companies(self) -> List[Dict[str, Any]]:
        args = []# type: ignore
        kwargs = {}# type: ignore
        return await _mutmut_trampoline(object.__getattribute__(self, 'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_orig'), object.__getattribute__(self, 'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_mutants'), args, kwargs, self)

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_orig(self) -> List[Dict[str, Any]]:
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_1(self) -> List[Dict[str, Any]]:
        """
        Navigates to the B3 page to get cookies/WAF clearance, then hits the backend API
        to fetch the paginated list of all companies.
        """
        all_companies = None
        
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_2(self) -> List[Dict[str, Any]]:
        """
        Navigates to the B3 page to get cookies/WAF clearance, then hits the backend API
        to fetch the paginated list of all companies.
        """
        all_companies = []
        
        async with async_playwright() as p:
            browser = None
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_3(self) -> List[Dict[str, Any]]:
        """
        Navigates to the B3 page to get cookies/WAF clearance, then hits the backend API
        to fetch the paginated list of all companies.
        """
        all_companies = []
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=None)
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_4(self) -> List[Dict[str, Any]]:
        """
        Navigates to the B3 page to get cookies/WAF clearance, then hits the backend API
        to fetch the paginated list of all companies.
        """
        all_companies = []
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = None
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_5(self) -> List[Dict[str, Any]]:
        """
        Navigates to the B3 page to get cookies/WAF clearance, then hits the backend API
        to fetch the paginated list of all companies.
        """
        all_companies = []
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context(
                user_agent=None
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_6(self) -> List[Dict[str, Any]]:
        """
        Navigates to the B3 page to get cookies/WAF clearance, then hits the backend API
        to fetch the paginated list of all companies.
        """
        all_companies = []
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context(
                user_agent="XXMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36XX"
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_7(self) -> List[Dict[str, Any]]:
        """
        Navigates to the B3 page to get cookies/WAF clearance, then hits the backend API
        to fetch the paginated list of all companies.
        """
        all_companies = []
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context(
                user_agent="mozilla/5.0 (windows nt 10.0; win64; x64) applewebkit/537.36 (khtml, like gecko) chrome/120.0.0.0 safari/537.36"
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_8(self) -> List[Dict[str, Any]]:
        """
        Navigates to the B3 page to get cookies/WAF clearance, then hits the backend API
        to fetch the paginated list of all companies.
        """
        all_companies = []
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context(
                user_agent="MOZILLA/5.0 (WINDOWS NT 10.0; WIN64; X64) APPLEWEBKIT/537.36 (KHTML, LIKE GECKO) CHROME/120.0.0.0 SAFARI/537.36"
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_9(self) -> List[Dict[str, Any]]:
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
            page = None
            
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_10(self) -> List[Dict[str, Any]]:
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
            await page.goto(None, wait_until="networkidle")
            
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_11(self) -> List[Dict[str, Any]]:
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
            await page.goto(self.homepage_url, wait_until=None)
            
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_12(self) -> List[Dict[str, Any]]:
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
            await page.goto(wait_until="networkidle")
            
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_13(self) -> List[Dict[str, Any]]:
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
            await page.goto(self.homepage_url, )
            
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_14(self) -> List[Dict[str, Any]]:
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
            await page.goto(self.homepage_url, wait_until="XXnetworkidleXX")
            
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_15(self) -> List[Dict[str, Any]]:
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
            await page.goto(self.homepage_url, wait_until="NETWORKIDLE")
            
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_16(self) -> List[Dict[str, Any]]:
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
            page_num = None
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_17(self) -> List[Dict[str, Any]]:
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
            page_num = 2
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_18(self) -> List[Dict[str, Any]]:
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
            total_pages = None
            
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_19(self) -> List[Dict[str, Any]]:
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
            total_pages = 2
            
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_20(self) -> List[Dict[str, Any]]:
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
            
            while page_num < total_pages:
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_21(self) -> List[Dict[str, Any]]:
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
                payload = None
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_22(self) -> List[Dict[str, Any]]:
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
                payload = {"XXlanguageXX": "pt-br", "pageNumber": page_num, "pageSize": 120}
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_23(self) -> List[Dict[str, Any]]:
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
                payload = {"LANGUAGE": "pt-br", "pageNumber": page_num, "pageSize": 120}
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_24(self) -> List[Dict[str, Any]]:
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
                payload = {"language": "XXpt-brXX", "pageNumber": page_num, "pageSize": 120}
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_25(self) -> List[Dict[str, Any]]:
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
                payload = {"language": "PT-BR", "pageNumber": page_num, "pageSize": 120}
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_26(self) -> List[Dict[str, Any]]:
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
                payload = {"language": "pt-br", "XXpageNumberXX": page_num, "pageSize": 120}
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_27(self) -> List[Dict[str, Any]]:
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
                payload = {"language": "pt-br", "pagenumber": page_num, "pageSize": 120}
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_28(self) -> List[Dict[str, Any]]:
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
                payload = {"language": "pt-br", "PAGENUMBER": page_num, "pageSize": 120}
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_29(self) -> List[Dict[str, Any]]:
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
                payload = {"language": "pt-br", "pageNumber": page_num, "XXpageSizeXX": 120}
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_30(self) -> List[Dict[str, Any]]:
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
                payload = {"language": "pt-br", "pageNumber": page_num, "pagesize": 120}
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_31(self) -> List[Dict[str, Any]]:
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
                payload = {"language": "pt-br", "pageNumber": page_num, "PAGESIZE": 120}
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_32(self) -> List[Dict[str, Any]]:
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
                payload = {"language": "pt-br", "pageNumber": page_num, "pageSize": 121}
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_33(self) -> List[Dict[str, Any]]:
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
                token = None
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_34(self) -> List[Dict[str, Any]]:
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
                token = self._create_token(None)
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_35(self) -> List[Dict[str, Any]]:
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
                endpoint = None
                
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_36(self) -> List[Dict[str, Any]]:
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
                
                response = None
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_37(self) -> List[Dict[str, Any]]:
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
                
                response = await context.request.get(None)
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

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_38(self) -> List[Dict[str, Any]]:
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
                if response.ok:
                    raise Exception(f"Failed to fetch page {page_num}: {response.status}")
                
                data = await response.json()
                
                if page_num == 1:
                    total_pages = data.get("page", {}).get("totalPages", 1)
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_39(self) -> List[Dict[str, Any]]:
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
                    raise Exception(None)
                
                data = await response.json()
                
                if page_num == 1:
                    total_pages = data.get("page", {}).get("totalPages", 1)
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_40(self) -> List[Dict[str, Any]]:
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
                
                data = None
                
                if page_num == 1:
                    total_pages = data.get("page", {}).get("totalPages", 1)
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_41(self) -> List[Dict[str, Any]]:
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
                
                if page_num != 1:
                    total_pages = data.get("page", {}).get("totalPages", 1)
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_42(self) -> List[Dict[str, Any]]:
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
                
                if page_num == 2:
                    total_pages = data.get("page", {}).get("totalPages", 1)
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_43(self) -> List[Dict[str, Any]]:
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
                    total_pages = None
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_44(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", {}).get(None, 1)
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_45(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", {}).get("totalPages", None)
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_46(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", {}).get(1)
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_47(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", {}).get("totalPages", )
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_48(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get(None, {}).get("totalPages", 1)
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_49(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", None).get("totalPages", 1)
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_50(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get({}).get("totalPages", 1)
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_51(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", ).get("totalPages", 1)
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_52(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("XXpageXX", {}).get("totalPages", 1)
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_53(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("PAGE", {}).get("totalPages", 1)
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_54(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", {}).get("XXtotalPagesXX", 1)
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_55(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", {}).get("totalpages", 1)
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_56(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", {}).get("TOTALPAGES", 1)
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_57(self) -> List[Dict[str, Any]]:
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
                    total_pages = data.get("page", {}).get("totalPages", 2)
                
                companies = data.get("results", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_58(self) -> List[Dict[str, Any]]:
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
                
                companies = None
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_59(self) -> List[Dict[str, Any]]:
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
                
                companies = data.get(None, [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_60(self) -> List[Dict[str, Any]]:
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
                
                companies = data.get("results", None)
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_61(self) -> List[Dict[str, Any]]:
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
                
                companies = data.get([])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_62(self) -> List[Dict[str, Any]]:
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
                
                companies = data.get("results", )
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_63(self) -> List[Dict[str, Any]]:
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
                
                companies = data.get("XXresultsXX", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_64(self) -> List[Dict[str, Any]]:
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
                
                companies = data.get("RESULTS", [])
                all_companies.extend(companies)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_65(self) -> List[Dict[str, Any]]:
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
                all_companies.extend(None)
                
                page_num += 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_66(self) -> List[Dict[str, Any]]:
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
                
                page_num = 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_67(self) -> List[Dict[str, Any]]:
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
                
                page_num -= 1
                
            await browser.close()
            
        return all_companies

    async def xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_68(self) -> List[Dict[str, Any]]:
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
                
                page_num += 2
                
            await browser.close()
            
        return all_companies
    
    xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_1': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_1, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_2': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_2, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_3': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_3, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_4': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_4, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_5': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_5, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_6': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_6, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_7': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_7, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_8': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_8, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_9': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_9, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_10': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_10, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_11': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_11, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_12': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_12, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_13': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_13, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_14': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_14, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_15': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_15, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_16': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_16, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_17': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_17, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_18': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_18, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_19': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_19, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_20': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_20, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_21': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_21, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_22': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_22, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_23': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_23, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_24': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_24, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_25': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_25, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_26': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_26, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_27': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_27, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_28': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_28, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_29': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_29, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_30': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_30, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_31': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_31, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_32': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_32, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_33': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_33, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_34': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_34, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_35': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_35, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_36': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_36, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_37': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_37, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_38': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_38, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_39': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_39, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_40': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_40, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_41': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_41, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_42': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_42, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_43': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_43, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_44': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_44, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_45': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_45, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_46': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_46, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_47': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_47, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_48': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_48, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_49': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_49, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_50': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_50, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_51': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_51, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_52': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_52, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_53': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_53, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_54': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_54, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_55': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_55, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_56': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_56, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_57': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_57, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_58': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_58, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_59': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_59, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_60': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_60, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_61': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_61, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_62': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_62, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_63': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_63, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_64': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_64, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_65': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_65, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_66': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_66, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_67': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_67, 
        'xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_68': xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_68
    }
    xǁPlaywrightB3Scraperǁfetch_initial_companies__mutmut_orig.__name__ = 'xǁPlaywrightB3Scraperǁfetch_initial_companies'

    async def fetch_company_details(self, cvm_code: str) -> Dict[str, Any]:
        args = [cvm_code]# type: ignore
        kwargs = {}# type: ignore
        return await _mutmut_trampoline(object.__getattribute__(self, 'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_orig'), object.__getattribute__(self, 'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_mutants'), args, kwargs, self)

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_orig(self, cvm_code: str) -> Dict[str, Any]:
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

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_1(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = None
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

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_2(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "XXhttps://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/XX"
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

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_3(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedcompaniesproxy/companydatacall/getdetail/"
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

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_4(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "HTTPS://SISTEMASWEBB3-LISTADOS.B3.COM.BR/LISTEDCOMPANIESPROXY/COMPANYDATACALL/GETDETAIL/"
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

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_5(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = None
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

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_6(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"XXcodeCVMXX": str(cvm_code), "language": "pt-br"}
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

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_7(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"codecvm": str(cvm_code), "language": "pt-br"}
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

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_8(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"CODECVM": str(cvm_code), "language": "pt-br"}
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

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_9(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"codeCVM": str(None), "language": "pt-br"}
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

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_10(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"codeCVM": str(cvm_code), "XXlanguageXX": "pt-br"}
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

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_11(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"codeCVM": str(cvm_code), "LANGUAGE": "pt-br"}
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

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_12(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"codeCVM": str(cvm_code), "language": "XXpt-brXX"}
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

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_13(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"codeCVM": str(cvm_code), "language": "PT-BR"}
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

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_14(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = None
        
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

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_15(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(None)
        
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

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_16(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = None
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

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_17(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=None)
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

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_18(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = None
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

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_19(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            page = None
            
            # Get session
            await page.goto(self.homepage_url, wait_until="networkidle")
            
            # API Request
            response = await context.request.get(f"{endpoint_base}{token}")
            if not response.ok:
                raise Exception(f"Failed to fetch details for {cvm_code}: {response.status}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_20(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            page = await context.new_page()
            
            # Get session
            await page.goto(None, wait_until="networkidle")
            
            # API Request
            response = await context.request.get(f"{endpoint_base}{token}")
            if not response.ok:
                raise Exception(f"Failed to fetch details for {cvm_code}: {response.status}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_21(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            page = await context.new_page()
            
            # Get session
            await page.goto(self.homepage_url, wait_until=None)
            
            # API Request
            response = await context.request.get(f"{endpoint_base}{token}")
            if not response.ok:
                raise Exception(f"Failed to fetch details for {cvm_code}: {response.status}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_22(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            page = await context.new_page()
            
            # Get session
            await page.goto(wait_until="networkidle")
            
            # API Request
            response = await context.request.get(f"{endpoint_base}{token}")
            if not response.ok:
                raise Exception(f"Failed to fetch details for {cvm_code}: {response.status}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_23(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            page = await context.new_page()
            
            # Get session
            await page.goto(self.homepage_url, )
            
            # API Request
            response = await context.request.get(f"{endpoint_base}{token}")
            if not response.ok:
                raise Exception(f"Failed to fetch details for {cvm_code}: {response.status}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_24(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            page = await context.new_page()
            
            # Get session
            await page.goto(self.homepage_url, wait_until="XXnetworkidleXX")
            
            # API Request
            response = await context.request.get(f"{endpoint_base}{token}")
            if not response.ok:
                raise Exception(f"Failed to fetch details for {cvm_code}: {response.status}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_25(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch details for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            page = await context.new_page()
            
            # Get session
            await page.goto(self.homepage_url, wait_until="NETWORKIDLE")
            
            # API Request
            response = await context.request.get(f"{endpoint_base}{token}")
            if not response.ok:
                raise Exception(f"Failed to fetch details for {cvm_code}: {response.status}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_26(self, cvm_code: str) -> Dict[str, Any]:
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
            response = None
            if not response.ok:
                raise Exception(f"Failed to fetch details for {cvm_code}: {response.status}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_27(self, cvm_code: str) -> Dict[str, Any]:
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
            response = await context.request.get(None)
            if not response.ok:
                raise Exception(f"Failed to fetch details for {cvm_code}: {response.status}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_28(self, cvm_code: str) -> Dict[str, Any]:
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
            if response.ok:
                raise Exception(f"Failed to fetch details for {cvm_code}: {response.status}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_29(self, cvm_code: str) -> Dict[str, Any]:
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
                raise Exception(None)
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_30(self, cvm_code: str) -> Dict[str, Any]:
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
                
            data = None
            await browser.close()
            return data
    
    xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_1': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_1, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_2': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_2, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_3': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_3, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_4': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_4, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_5': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_5, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_6': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_6, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_7': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_7, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_8': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_8, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_9': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_9, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_10': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_10, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_11': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_11, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_12': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_12, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_13': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_13, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_14': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_14, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_15': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_15, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_16': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_16, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_17': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_17, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_18': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_18, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_19': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_19, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_20': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_20, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_21': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_21, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_22': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_22, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_23': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_23, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_24': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_24, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_25': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_25, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_26': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_26, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_27': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_27, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_28': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_28, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_29': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_29, 
        'xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_30': xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_30
    }
    xǁPlaywrightB3Scraperǁfetch_company_details__mutmut_orig.__name__ = 'xǁPlaywrightB3Scraperǁfetch_company_details'

    async def fetch_company_financials(self, cvm_code: str) -> Dict[str, Any]:
        args = [cvm_code]# type: ignore
        kwargs = {}# type: ignore
        return await _mutmut_trampoline(object.__getattribute__(self, 'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_orig'), object.__getattribute__(self, 'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_mutants'), args, kwargs, self)

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_orig(self, cvm_code: str) -> Dict[str, Any]:
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

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_1(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = None
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

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_2(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "XXhttps://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/XX"
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

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_3(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedcompaniesproxy/companydatacall/getlistedfinancial/"
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

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_4(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "HTTPS://SISTEMASWEBB3-LISTADOS.B3.COM.BR/LISTEDCOMPANIESPROXY/COMPANYDATACALL/GETLISTEDFINANCIAL/"
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

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_5(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = None
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

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_6(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"XXcodeCVMXX": str(cvm_code), "language": "pt-br"}
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

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_7(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codecvm": str(cvm_code), "language": "pt-br"}
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

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_8(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"CODECVM": str(cvm_code), "language": "pt-br"}
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

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_9(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(None), "language": "pt-br"}
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

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_10(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(cvm_code), "XXlanguageXX": "pt-br"}
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

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_11(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(cvm_code), "LANGUAGE": "pt-br"}
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

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_12(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(cvm_code), "language": "XXpt-brXX"}
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

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_13(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(cvm_code), "language": "PT-BR"}
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

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_14(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = None
        
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

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_15(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(None)
        
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

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_16(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = None
            context = await browser.new_context()
            page = await context.new_page()
            
            await page.goto(self.homepage_url, wait_until="networkidle")
            
            response = await context.request.get(f"{endpoint_base}{token}")
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_17(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=None)
            context = await browser.new_context()
            page = await context.new_page()
            
            await page.goto(self.homepage_url, wait_until="networkidle")
            
            response = await context.request.get(f"{endpoint_base}{token}")
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_18(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = None
            page = await context.new_page()
            
            await page.goto(self.homepage_url, wait_until="networkidle")
            
            response = await context.request.get(f"{endpoint_base}{token}")
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_19(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            page = None
            
            await page.goto(self.homepage_url, wait_until="networkidle")
            
            response = await context.request.get(f"{endpoint_base}{token}")
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_20(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            page = await context.new_page()
            
            await page.goto(None, wait_until="networkidle")
            
            response = await context.request.get(f"{endpoint_base}{token}")
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_21(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            page = await context.new_page()
            
            await page.goto(self.homepage_url, wait_until=None)
            
            response = await context.request.get(f"{endpoint_base}{token}")
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_22(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            page = await context.new_page()
            
            await page.goto(wait_until="networkidle")
            
            response = await context.request.get(f"{endpoint_base}{token}")
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_23(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            page = await context.new_page()
            
            await page.goto(self.homepage_url, )
            
            response = await context.request.get(f"{endpoint_base}{token}")
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_24(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            page = await context.new_page()
            
            await page.goto(self.homepage_url, wait_until="XXnetworkidleXX")
            
            response = await context.request.get(f"{endpoint_base}{token}")
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_25(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            page = await context.new_page()
            
            await page.goto(self.homepage_url, wait_until="NETWORKIDLE")
            
            response = await context.request.get(f"{endpoint_base}{token}")
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_26(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            page = await context.new_page()
            
            await page.goto(self.homepage_url, wait_until="networkidle")
            
            response = None
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_27(self, cvm_code: str) -> Dict[str, Any]:
        """Fetch financials and shareholders for a specific CVM Code"""
        endpoint_base = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"
        payload = {"codeCVM": str(cvm_code), "language": "pt-br"}
        token = self._create_token(payload)
        
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context()
            page = await context.new_page()
            
            await page.goto(self.homepage_url, wait_until="networkidle")
            
            response = await context.request.get(None)
            if not response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_28(self, cvm_code: str) -> Dict[str, Any]:
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
            if response.ok:
                raise Exception(f"Failed to fetch financials for {cvm_code}")
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_29(self, cvm_code: str) -> Dict[str, Any]:
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
                raise Exception(None)
                
            data = await response.json()
            await browser.close()
            return data

    async def xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_30(self, cvm_code: str) -> Dict[str, Any]:
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
                
            data = None
            await browser.close()
            return data
    
    xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_1': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_1, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_2': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_2, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_3': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_3, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_4': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_4, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_5': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_5, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_6': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_6, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_7': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_7, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_8': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_8, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_9': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_9, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_10': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_10, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_11': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_11, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_12': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_12, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_13': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_13, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_14': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_14, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_15': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_15, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_16': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_16, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_17': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_17, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_18': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_18, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_19': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_19, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_20': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_20, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_21': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_21, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_22': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_22, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_23': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_23, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_24': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_24, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_25': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_25, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_26': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_26, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_27': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_27, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_28': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_28, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_29': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_29, 
        'xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_30': xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_30
    }
    xǁPlaywrightB3Scraperǁfetch_company_financials__mutmut_orig.__name__ = 'xǁPlaywrightB3Scraperǁfetch_company_financials'
