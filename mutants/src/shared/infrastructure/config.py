from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict
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

# 1. Create subgroups inheriting from BaseModel (not BaseSettings)
class AppSettings(BaseModel):
    title: str = "FLY.AI Finance Data"
    description: str = "SOTA Finance Data Platform using DDD and Hexagonal Architecture"
    version: str = "0.2.0"
    debug: bool = False
    log_dir: str = "logs"
    log_name: str = "app.log"

class DatabaseSettings(BaseModel):
    url: str = Field(
        default="postgresql://postgres:postgres@localhost:5432/flyai_b3",
        description="SQLAlchemy database connection string"
    )

class RedisSettings(BaseModel):
    url: str = Field(
        default="redis://localhost:6379/0",
        description="Redis connection string"
    )

class B3Settings(BaseModel):
    homepage_url: str = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/?language=pt-br"
    initial_companies_api: str = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetInitialCompanies/"
    detail_api: str = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetDetail/"
    financial_api: str = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetListedFinancial/"
    headless: bool = False # True
    words_to_remove: list[str] = [
        "  EM LIQUIDACAO",
        " EM LIQUIDACAO",
        " EXTRAJUDICIAL",
        "  EM RECUPERACAO JUDICIAL",
        "  EM REC JUDICIAL",
        " EM RECUPERACAO JUDICIAL",
        " EM LIQUIDACAO EXTRAJUDICIAL",
        " EMPRESA FALIDA",
    ]
    max_concurrency: int = 50

# 2. The main class brings everything together
class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    db: DatabaseSettings = DatabaseSettings()
    redis: RedisSettings = RedisSettings()
    b3: B3Settings = B3Settings()

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        # The clever trick: Tells Pydantic how to read nested variables from the .env file
        env_nested_delimiter="__", 
        case_sensitive=False
    )

# Single instance (Singleton) exported for the project
settings = Settings()