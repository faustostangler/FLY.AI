from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseModel):
    title: str = "FLY.AI Finance Data"
    description: str = "SOTA Finance Data Platform using DDD and Hexagonal Architecture"
    version: str = "0.2.0"
    debug: bool = False
    log_dir: str = "logs"
    log_name: str = "app.log"
    model_config = {"extra": "ignore"}


class DatabaseSettings(BaseModel):
    """
    SOTA Database Config: Strict Type Hinting & Anti-Shadowing.
    Maps: DB__URL, DB__USER, DB__PASSWORD, DB__NAME, DB__HOST, DB__PORT
    """
    # Tipagem estrita: Sempre será uma string, o MyPy e o SQLAlchemy agradecem.
    url: str = Field(description="Full connection string (Strictly typed as str)")
    
    user: Optional[str] = Field(default=None, description="DB user (DB__USER)")
    password: Optional[str] = Field(default=None, description="DB password (DB__PASSWORD)")
    name: Optional[str] = Field(default=None, description="DB name (DB__NAME)")
    host: str = Field(default="localhost", description="DB host (DB__HOST)")
    port: int = Field(default=5432, description="DB port (DB__PORT)")

    model_config = {"extra": "ignore"}

    @model_validator(mode='before')
    @classmethod
    def assemble_or_validate(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        """Intercepta os dados brutos ANTES da validação do modelo."""
        url = values.get('url')
        user = values.get('user')
        password = values.get('password')
        name = values.get('name')
        
        # O .get() precisa de fallback aqui porque os defaults da classe ainda não foram aplicados
        host = values.get('host', 'localhost')
        port = values.get('port', 5432)

        has_atomic_credentials = bool(user or password or name)
        is_fully_atomic = bool(user and password and name)

        # 1. Anti-Shadowing: Fail Fast se o desenvolvedor misturar os paradigmas
        if url and has_atomic_credentials:
            raise ValueError(
                "CRITICAL CONFIG CONFLICT: Você forneceu 'DB__URL' e credenciais atômicas "
                "('DB__USER', 'DB__PASSWORD' ou 'DB__NAME') simultaneamente. "
                "Para evitar shadowing e erros silenciosos, escolha apenas um paradigma no seu .env ou docker-compose."
            )

        # 2. Se a URL foi injetada (ex: pelo docker-compose ou PaaS), apenas repassa
        if url:
            return values
        
        # 3. Se temos as credenciais atômicas, montamos a URL e injetamos no dicionário
        if is_fully_atomic:
            values['url'] = (
                f"postgresql+psycopg2://{user}:{password}"
                f"@{host}:{port}/{name}"
            )
            return values
            
        raise ValueError(
            "Database configuration is incomplete. Provide either a full 'DB__URL' "
            "or the atomic credentials ('DB__USER', 'DB__PASSWORD', 'DB__NAME')."
        )


class RedisSettings(BaseModel):
    """
    SOTA Redis Config: Strict Type Hinting & Anti-Shadowing.
    Maps: REDIS__URL, REDIS__HOST, REDIS__PORT, REDIS__DB
    """
    url: str = Field(description="Full Redis URL")
    host: str = Field(default="localhost", description="Redis host (REDIS__HOST)")
    port: int = Field(default=6379, description="Redis port (REDIS__PORT)")
    db: int = Field(default=0, description="Redis DB index (REDIS__DB)")

    model_config = {"extra": "ignore"}

    @model_validator(mode='before')
    @classmethod
    def assemble_redis_url(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        url = values.get('url')
        
        # Anti-Shadowing para o Redis
        if url and ('host' in values or 'port' in values):
            raise ValueError(
                "CRITICAL CONFIG CONFLICT: Forneça REDIS__URL ou (REDIS__HOST / REDIS__PORT), não ambos."
            )

        if not url:
            host = values.get('host', 'localhost')
            port = values.get('port', 6379)
            db = values.get('db', 0)
            values['url'] = f"redis://{host}:{port}/{db}"
            
        return values


class B3Settings(BaseModel):
    """B3 Scraper configuration. Env mapping: B3__HEADLESS, B3__MAX_CONCURRENCY, etc."""
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
    headless: bool = True
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
    model_config = {"extra": "ignore"}


class Settings(BaseSettings):
    """Root settings. Loads from .env with __ as nested delimiter."""
    app: AppSettings = AppSettings()
    db: DatabaseSettings
    redis: RedisSettings = RedisSettings()
    b3: B3Settings = B3Settings()

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="ignore",
    )


# Singleton — fails fast at import if required env vars or validation rules are broken
settings = Settings()