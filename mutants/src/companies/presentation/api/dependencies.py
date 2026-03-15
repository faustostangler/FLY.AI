from fastapi import Depends
from sqlalchemy.orm import Session
from shared.infrastructure.database.connection import get_db
from companies.infrastructure.adapters.database.postgres_company_repository import PostgresCompanyRepository
from companies.infrastructure.adapters.data_sources.playwright_b3_data_source import PlaywrightB3DataSource
from companies.application.use_cases.sync_b3_companies import SyncB3CompaniesUseCase
from shared.domain.ports.telemetry_port import TelemetryPort
from shared.infrastructure.adapters.prometheus_telemetry import PrometheusTelemetryAdapter
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

def get_telemetry_port() -> TelemetryPort:
    """Dependency Provider for TelemetryPort"""
    return PrometheusTelemetryAdapter()

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

def get_b3_data_source(telemetry: TelemetryPort = Depends(get_telemetry_port)) -> PlaywrightB3DataSource:
    args = [telemetry]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_get_b3_data_source__mutmut_orig, x_get_b3_data_source__mutmut_mutants, args, kwargs, None)

def x_get_b3_data_source__mutmut_orig(telemetry: TelemetryPort = Depends(get_telemetry_port)) -> PlaywrightB3DataSource:
    """Dependency Provider for B3DataSource Port. Default headless mode from settings."""
    return PlaywrightB3DataSource(telemetry=telemetry)

def x_get_b3_data_source__mutmut_1(telemetry: TelemetryPort = Depends(get_telemetry_port)) -> PlaywrightB3DataSource:
    """Dependency Provider for B3DataSource Port. Default headless mode from settings."""
    return PlaywrightB3DataSource(telemetry=None)

x_get_b3_data_source__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_get_b3_data_source__mutmut_1': x_get_b3_data_source__mutmut_1
}
x_get_b3_data_source__mutmut_orig.__name__ = 'x_get_b3_data_source'

def get_sync_b3_companies_use_case(
    data_source: PlaywrightB3DataSource = Depends(get_b3_data_source),
    repository: PostgresCompanyRepository = Depends(get_company_repository),
    telemetry: TelemetryPort = Depends(get_telemetry_port)
) -> SyncB3CompaniesUseCase:
    args = [data_source, repository, telemetry]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_get_sync_b3_companies_use_case__mutmut_orig, x_get_sync_b3_companies_use_case__mutmut_mutants, args, kwargs, None)

def x_get_sync_b3_companies_use_case__mutmut_orig(
    data_source: PlaywrightB3DataSource = Depends(get_b3_data_source),
    repository: PostgresCompanyRepository = Depends(get_company_repository),
    telemetry: TelemetryPort = Depends(get_telemetry_port)
) -> SyncB3CompaniesUseCase:
    """Dependency Provider for the Sync Use Case"""
    return SyncB3CompaniesUseCase(data_source=data_source, repository=repository, telemetry=telemetry)

def x_get_sync_b3_companies_use_case__mutmut_1(
    data_source: PlaywrightB3DataSource = Depends(get_b3_data_source),
    repository: PostgresCompanyRepository = Depends(get_company_repository),
    telemetry: TelemetryPort = Depends(get_telemetry_port)
) -> SyncB3CompaniesUseCase:
    """Dependency Provider for the Sync Use Case"""
    return SyncB3CompaniesUseCase(data_source=None, repository=repository, telemetry=telemetry)

def x_get_sync_b3_companies_use_case__mutmut_2(
    data_source: PlaywrightB3DataSource = Depends(get_b3_data_source),
    repository: PostgresCompanyRepository = Depends(get_company_repository),
    telemetry: TelemetryPort = Depends(get_telemetry_port)
) -> SyncB3CompaniesUseCase:
    """Dependency Provider for the Sync Use Case"""
    return SyncB3CompaniesUseCase(data_source=data_source, repository=None, telemetry=telemetry)

def x_get_sync_b3_companies_use_case__mutmut_3(
    data_source: PlaywrightB3DataSource = Depends(get_b3_data_source),
    repository: PostgresCompanyRepository = Depends(get_company_repository),
    telemetry: TelemetryPort = Depends(get_telemetry_port)
) -> SyncB3CompaniesUseCase:
    """Dependency Provider for the Sync Use Case"""
    return SyncB3CompaniesUseCase(data_source=data_source, repository=repository, telemetry=None)

def x_get_sync_b3_companies_use_case__mutmut_4(
    data_source: PlaywrightB3DataSource = Depends(get_b3_data_source),
    repository: PostgresCompanyRepository = Depends(get_company_repository),
    telemetry: TelemetryPort = Depends(get_telemetry_port)
) -> SyncB3CompaniesUseCase:
    """Dependency Provider for the Sync Use Case"""
    return SyncB3CompaniesUseCase(repository=repository, telemetry=telemetry)

def x_get_sync_b3_companies_use_case__mutmut_5(
    data_source: PlaywrightB3DataSource = Depends(get_b3_data_source),
    repository: PostgresCompanyRepository = Depends(get_company_repository),
    telemetry: TelemetryPort = Depends(get_telemetry_port)
) -> SyncB3CompaniesUseCase:
    """Dependency Provider for the Sync Use Case"""
    return SyncB3CompaniesUseCase(data_source=data_source, telemetry=telemetry)

def x_get_sync_b3_companies_use_case__mutmut_6(
    data_source: PlaywrightB3DataSource = Depends(get_b3_data_source),
    repository: PostgresCompanyRepository = Depends(get_company_repository),
    telemetry: TelemetryPort = Depends(get_telemetry_port)
) -> SyncB3CompaniesUseCase:
    """Dependency Provider for the Sync Use Case"""
    return SyncB3CompaniesUseCase(data_source=data_source, repository=repository, )

x_get_sync_b3_companies_use_case__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_get_sync_b3_companies_use_case__mutmut_1': x_get_sync_b3_companies_use_case__mutmut_1, 
    'x_get_sync_b3_companies_use_case__mutmut_2': x_get_sync_b3_companies_use_case__mutmut_2, 
    'x_get_sync_b3_companies_use_case__mutmut_3': x_get_sync_b3_companies_use_case__mutmut_3, 
    'x_get_sync_b3_companies_use_case__mutmut_4': x_get_sync_b3_companies_use_case__mutmut_4, 
    'x_get_sync_b3_companies_use_case__mutmut_5': x_get_sync_b3_companies_use_case__mutmut_5, 
    'x_get_sync_b3_companies_use_case__mutmut_6': x_get_sync_b3_companies_use_case__mutmut_6
}
x_get_sync_b3_companies_use_case__mutmut_orig.__name__ = 'x_get_sync_b3_companies_use_case'
