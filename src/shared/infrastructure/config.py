import glob
from typing import Optional
from pydantic import BaseModel, Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


# Dynamic Environment Discovery from env/ folder
# Last file in the tuple has precedence in Pydantic Settings.
ENV_FILES = sorted(glob.glob(".env/*.env"))

# Ensure profile.env is last if it exists (for ORM/Profile overrides)
if ".env/profile.env" in ENV_FILES:
    ENV_FILES.remove(".env/profile.env")
    ENV_FILES.append(".env/profile.env")


class AppSettings(BaseModel):
    title: str = "FLY.AI Finance Data"
    description: str = "SOTA Finance Data Platform using DDD and Hexagonal Architecture"
    version: str = "0.2.0"
    debug: bool = False
    headless: bool = True
    max_concurrency: int = 50
    log_dir: str = "logs"
    log_name: str = "app.log"
    model_config = {"extra": "ignore"}


class DatabaseSettings(BaseModel):
    """
    SOTA Database Config: Strict Type Hinting & Anti-Shadowing.
    """
    # 1. Defined as str from the start (no Optional). Ends MyPy/SQLAlchemy issues.
    url: str = Field(description="Full connection string (Strictly typed as str)")
    
    user: Optional[str] = Field(default=None, description="DB user (DB__USER)")
    password: Optional[str] = Field(default=None, description="DB password (DB__PASSWORD)")
    name: Optional[str] = Field(default=None, description="DB name (DB__NAME)")
    host: str = Field(default="localhost", description="DB host (DB__HOST)")
    port: int = Field(default=5432, description="DB port (DB__PORT)")
    connection_timeout: int = Field(default=10, alias="db_connection_timeout")

    model_config = {"extra": "ignore", "populate_by_name": True}

    # 2. mode='before' intercepts BEFORE validation
    @model_validator(mode='before')
    @classmethod
    def assemble_or_validate(cls, values: dict) -> dict:
        url = values.get('url')
        user = values.get('user')
        password = values.get('password')
        name = values.get('name')
        
        host = values.get('host', 'localhost')
        port = values.get('port', 5432)

        has_atomic_credentials = bool(user or password or name)
        is_fully_atomic = bool(user and password and name)

        # Fail-Fast: Prevents the developer from making conflicting configurations in .env
        if url and has_atomic_credentials:
            raise ValueError(
                "CRITICAL CONFIG CONFLICT: Choose to provide EITHER 'DB__URL' OR "
                "the atomic credentials ('DB__USER', 'DB__PASSWORD', 'DB__NAME')."
            )

        if url:
            return values
        
        if is_fully_atomic:
            values['url'] = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{name}"
            return values
            
        raise ValueError("Database configuration is incomplete.")


class RedisSettings(BaseModel):
    """
    SOTA Redis Config: Strict Type Hinting & Anti-Shadowing.
    """
    url: str = Field(description="Full Redis URL (Strictly typed as str)")
    
    host: str = Field(default="localhost", description="Redis host (REDIS__HOST)")
    port: int = Field(default=6379, description="Redis port (REDIS__PORT)")
    db: int = Field(default=0, description="Redis DB index (REDIS__DB)")

    model_config = {"extra": "ignore"}

    @model_validator(mode='before')
    @classmethod
    def assemble_redis_url(cls, values: dict) -> dict:
        url = values.get('url')
        host = values.get('host', 'localhost')
        port = values.get('port', 6379)
        db = values.get('db', 0)
        
        has_atomic_credentials = bool('host' in values or 'port' in values or 'db' in values)

        if url and has_atomic_credentials:
             raise ValueError(
                "CRITICAL CONFIG CONFLICT: Choose to provide EITHER 'REDIS__URL' OR "
                "the atomic credentials ('REDIS__HOST', 'REDIS__PORT', 'REDIS__DB')."
            )

        if url:
            return values
            
        values['url'] = f"redis://{host}:{port}/{db}"
        return values


class B3Settings(BaseModel):
    homepage_url: str = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/?language=pt-br"
    initial_companies_api: str = (
        "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetInitialCompanies/"
    )
    detail_api: str = (
        "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetDetail/"
    )
    financial_api: str = (
        "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetListedFinancial/"
    )
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
    model_config = {"extra": "ignore"}


class Settings(BaseSettings):
    """Root settings. Loads from .env with __ as nested delimiter."""
    app: AppSettings = AppSettings()
    db: DatabaseSettings
    redis: RedisSettings = RedisSettings()
    b3: B3Settings = B3Settings()

    model_config = SettingsConfigDict(
        env_file=tuple(ENV_FILES),
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="ignore",
    )


# Singleton — fails fast at import if required env vars are missing
settings = Settings()