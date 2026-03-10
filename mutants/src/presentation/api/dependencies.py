from fastapi import Depends
from sqlalchemy.orm import Session
from infrastructure.database.connection import get_db
from infrastructure.adapters.database.postgres_company_repository import PostgresCompanyRepository
from infrastructure.adapters.scrapers.playwright_b3_scraper import PlaywrightB3Scraper
from application.use_cases.sync_b3_companies import SyncB3CompaniesUseCase
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

def get_company_repository(db: Session = Depends(get_db)) -> PostgresCompanyRepository:
    args = [db]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_get_company_repository__mutmut_orig, x_get_company_repository__mutmut_mutants, args, kwargs, None)

def x_get_company_repository__mutmut_orig(db: Session = Depends(get_db)) -> PostgresCompanyRepository:
    """Dependency Provider for CompanyRepository Port"""
    return PostgresCompanyRepository(session=db)

def x_get_company_repository__mutmut_1(db: Session = Depends(get_db)) -> PostgresCompanyRepository:
    """Dependency Provider for CompanyRepository Port"""
    return PostgresCompanyRepository(session=None)

x_get_company_repository__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_get_company_repository__mutmut_1': x_get_company_repository__mutmut_1
}
x_get_company_repository__mutmut_orig.__name__ = 'x_get_company_repository'

def get_b3_scraper() -> PlaywrightB3Scraper:
    args = []# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_get_b3_scraper__mutmut_orig, x_get_b3_scraper__mutmut_mutants, args, kwargs, None)

def x_get_b3_scraper__mutmut_orig() -> PlaywrightB3Scraper:
    """Dependency Provider for B3Scraper Port. Uses headless by default."""
    return PlaywrightB3Scraper(headless=True)

def x_get_b3_scraper__mutmut_1() -> PlaywrightB3Scraper:
    """Dependency Provider for B3Scraper Port. Uses headless by default."""
    return PlaywrightB3Scraper(headless=None)

def x_get_b3_scraper__mutmut_2() -> PlaywrightB3Scraper:
    """Dependency Provider for B3Scraper Port. Uses headless by default."""
    return PlaywrightB3Scraper(headless=False)

x_get_b3_scraper__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_get_b3_scraper__mutmut_1': x_get_b3_scraper__mutmut_1, 
    'x_get_b3_scraper__mutmut_2': x_get_b3_scraper__mutmut_2
}
x_get_b3_scraper__mutmut_orig.__name__ = 'x_get_b3_scraper'

def get_sync_b3_companies_use_case(
    scraper: PlaywrightB3Scraper = Depends(get_b3_scraper),
    repository: PostgresCompanyRepository = Depends(get_company_repository)
) -> SyncB3CompaniesUseCase:
    args = [scraper, repository]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_get_sync_b3_companies_use_case__mutmut_orig, x_get_sync_b3_companies_use_case__mutmut_mutants, args, kwargs, None)

def x_get_sync_b3_companies_use_case__mutmut_orig(
    scraper: PlaywrightB3Scraper = Depends(get_b3_scraper),
    repository: PostgresCompanyRepository = Depends(get_company_repository)
) -> SyncB3CompaniesUseCase:
    """Dependency Provider for the Sync Use Case"""
    return SyncB3CompaniesUseCase(scraper=scraper, repository=repository)

def x_get_sync_b3_companies_use_case__mutmut_1(
    scraper: PlaywrightB3Scraper = Depends(get_b3_scraper),
    repository: PostgresCompanyRepository = Depends(get_company_repository)
) -> SyncB3CompaniesUseCase:
    """Dependency Provider for the Sync Use Case"""
    return SyncB3CompaniesUseCase(scraper=None, repository=repository)

def x_get_sync_b3_companies_use_case__mutmut_2(
    scraper: PlaywrightB3Scraper = Depends(get_b3_scraper),
    repository: PostgresCompanyRepository = Depends(get_company_repository)
) -> SyncB3CompaniesUseCase:
    """Dependency Provider for the Sync Use Case"""
    return SyncB3CompaniesUseCase(scraper=scraper, repository=None)

def x_get_sync_b3_companies_use_case__mutmut_3(
    scraper: PlaywrightB3Scraper = Depends(get_b3_scraper),
    repository: PostgresCompanyRepository = Depends(get_company_repository)
) -> SyncB3CompaniesUseCase:
    """Dependency Provider for the Sync Use Case"""
    return SyncB3CompaniesUseCase(repository=repository)

def x_get_sync_b3_companies_use_case__mutmut_4(
    scraper: PlaywrightB3Scraper = Depends(get_b3_scraper),
    repository: PostgresCompanyRepository = Depends(get_company_repository)
) -> SyncB3CompaniesUseCase:
    """Dependency Provider for the Sync Use Case"""
    return SyncB3CompaniesUseCase(scraper=scraper, )

x_get_sync_b3_companies_use_case__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_get_sync_b3_companies_use_case__mutmut_1': x_get_sync_b3_companies_use_case__mutmut_1, 
    'x_get_sync_b3_companies_use_case__mutmut_2': x_get_sync_b3_companies_use_case__mutmut_2, 
    'x_get_sync_b3_companies_use_case__mutmut_3': x_get_sync_b3_companies_use_case__mutmut_3, 
    'x_get_sync_b3_companies_use_case__mutmut_4': x_get_sync_b3_companies_use_case__mutmut_4
}
x_get_sync_b3_companies_use_case__mutmut_orig.__name__ = 'x_get_sync_b3_companies_use_case'
