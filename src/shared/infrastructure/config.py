from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# 1. Create subgroups inheriting from BaseModel (not BaseSettings)
class AppSettings(BaseModel):
    title: str = "FLY.AI Finance Data"
    description: str = "SOTA Finance Data Platform using DDD and Hexagonal Architecture"
    version: str = "0.2.0"
    debug: bool = False
    log_dir: str = "logs"
    log_name: str = "app.log"

class DatabaseSettings(BaseModel):
    # SOTA: No hardcoded credentials. 
    # Use '...' to mark as required, forcing Pydantic to find it in .env or Environment Variables
    url: str = Field(
        ..., 
        description="SQLAlchemy database connection string (Sensitive - must come from environment)"
    )

class RedisSettings(BaseModel):
    # SOTA: Required connection string for security and configuration clarity
    url: str = Field(
        ..., 
        description="Redis connection string (Sensitive - must come from environment)"
    )

class B3Settings(BaseModel):
    # Internal URLs are usually safe as defaults, but can be overridden
    homepage_url: str = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/?language=pt-br"
    initial_companies_api: str = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetInitialCompanies/"
    detail_api: str = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetDetail/"
    financial_api: str = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetListedFinancial/"
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

# 2. The main class brings everything together
class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    db: DatabaseSettings
    redis: RedisSettings
    b3: B3Settings = B3Settings()

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        # Explicitly tells Pydantic to map ENV__VARS to nested objects
        env_nested_delimiter="__", 
        case_sensitive=False
    )

# Single instance (Singleton) exported for the project
# This will RAISE an error immediately if DB__URL or REDIS__URL are missing
settings = Settings()