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