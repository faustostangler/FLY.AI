from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# 1. Criamos os subgrupos herdando de BaseModel (não BaseSettings)
class AppSettings(BaseModel):
    title: str = "FLY.AI Finance Data"
    version: str = "0.2.0"
    debug: bool = False

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
    initial_companies_api: str = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetInitialCompanies/"
    detail_api: str = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetDetail/"
    financial_api: str = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyDataCall/GetListedFinancial/"

# 2. A classe principal junta tudo
class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    db: DatabaseSettings = DatabaseSettings()
    redis: RedisSettings = RedisSettings()
    b3: B3Settings = B3Settings()

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        # O Pulo do Gato: Diz ao Pydantic como ler o arquivo .env
        env_nested_delimiter="__", 
        case_sensitive=False
    )

# Instância única exportada para o projeto
settings = Settings()