import glob
from typing import Optional
from pydantic import BaseModel, Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


# Dynamic Environment Discovery from env/ folder
# Precedence follows the order in the tuple; last file overrides previous ones.
ENV_FILES = sorted(glob.glob(".envs/*.env"))

# Ensure profile.env is last to allow runtime/environment-specific overrides
# to take precedence over baseline configurations.
if ".envs/profile.env" in ENV_FILES:
    ENV_FILES.remove(".envs/profile.env")
    ENV_FILES.append(".envs/profile.env")


class B3Settings(BaseModel):
    """Constants and endpoints for the B3 External Data Source (Brazilian Stock Exchange).

    Encapsulates knowledge about B3's internal API structure and data quality rules.

    Attributes:
        homepage_url (str): Entry point for the Playwright scraper.
        initial_companies_api (str): B3 endpoint for fetching the initial company list.
        detail_api (str): Endpoint for fine-grained company metadata.
        financial_api (str): Endpoint for downloading historical financial reports.
        referer_url (str): The common Referer header required for B3 API calls.
        words_to_remove (list[str]): Noise phrases found in B3 data that must be scrubbed
            to maintain Domain integrity (e.g., 'EM RECUPERACAO JUDICIAL').
    """

    homepage_url: str = (
        "https://sistemaswebb3-listados.b3.com.br/listedCompaniesPage/?language=pt-br"
    )
    initial_companies_api: str = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetInitialCompanies/"
    detail_api: str = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetDetail/"
    financial_api: str = "https://sistemaswebb3-listados.b3.com.br/listedCompaniesProxy/CompanyCall/GetListedFinancial/"
    referer_url: str = "https://sistemaswebb3-listados.b3.com.br/"
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


class AppSettings(BaseModel):
    """General application metadata and operational limits.

    Attributes:
        title (str): The human-readable name of the platform.
        description (str): A brief overview of the system's purpose.
        version (str): The current SemVer of the application.
        debug (bool): Flag to enable/disable detailed error reporting.
        headless (bool): Controls whether the B3 Scraper UI is visible during execution.
        max_concurrency (int): Throughput limit to prevent rate-limiting or resource exhaustion.
        log_dir (str): Directory where structural logs are persisted.
        log_name (str): Filename for primary application logs.
    """

    title: str = "FLY.AI Finance Data"
    description: str = "SOTA Finance Data Platform using DDD and Hexagonal Architecture"
    version: str = "0.2.0"
    debug: bool = False
    headless: bool = True
    max_concurrency: int = 50
    log_dir: str = "logs"
    log_name: str = "app.log"
    environment: str = Field(description="Deployment environment (development, staging, production) (APP__ENVIRONMENT)")
    model_config = {"extra": "ignore"}


class DatabaseSettings(BaseModel):
    """Persistence configurations for the Primary Relational Store.

    Ensures type safety between environment variables and SQLAlchemy drivers
    by validating connection strings or assembling them from atomic credentials.

    Attributes:
        url (str): The full JDBC/SQLAlchemy connection string.
        user (str): Database username.
        password (str): Database password.
        name (str): The specific database name/schema to connect to.
        host (str): Network address of the database server.
        port (int): Listening port for the database service.
        connection_timeout (int): Grace period before failing a connection attempt.
    """

    url: str = Field(description="Full connection string (Strictly typed as str)")

    user: Optional[str] = Field(default=None, description="DB user (DB__USER)")
    password: Optional[str] = Field(
        default=None, description="DB password (DB__PASSWORD)"
    )
    name: Optional[str] = Field(default=None, description="DB name (DB__NAME)")
    host: str = Field(default="localhost", description="DB host (DB__HOST)")
    port: int = Field(default=5432, description="DB port (DB__PORT)")
    connection_timeout: int = Field(default=10, alias="db_connection_timeout")

    model_config = {"extra": "ignore", "populate_by_name": True}

    @model_validator(mode="before")
    @classmethod
    def assemble_or_validate(cls, values: dict) -> dict:
        """Assembles the SQLAlchemy URL from atomic fields if the full URL is not provided.

        This ensures a Single Source of Truth (SSOT) for the connection string,
        preventing configuration drift where credentials in individual fields
        differ from the one in the full URL.

        Args:
            values (dict): Raw input data from environment variables or .env files.

        Returns:
            dict: The validated and potentially augmented configuration dictionary.

        Raises:
            ValueError: If both partial credentials and a full URL are provided,
                or if neither is sufficient to establish a connection.
        """
        url = values.get("url")
        user = values.get("user")
        password = values.get("password")
        name = values.get("name")

        host = values.get("host", "localhost")
        port = values.get("port", 5432)

        has_atomic_credentials = bool(user or password or name)
        is_fully_atomic = bool(user and password and name)

        # Fail-Fast to prevent ambiguous configuration states.
        if url and has_atomic_credentials:
            raise ValueError(
                "CRITICAL CONFIG CONFLICT: Choose to provide EITHER 'DB__URL' OR "
                "the atomic credentials ('DB__USER', 'DB__PASSWORD', 'DB__NAME')."
            )

        if url:
            return values

        if is_fully_atomic:
            # Construct canonical URL for SQLAlchemy async engine initialization.
            values["url"] = (
                f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{name}"
            )
            return values

        raise ValueError("Database configuration is incomplete.")


class RedisSettings(BaseModel):
    """Configuration for the Distributed Cache and Synchronization layer.

    Used primarily for rate limiting and cross-worker state management.

    Attributes:
        url (str): The full Redis connection string.
        host (str): Network address of the Redis server.
        port (int): Listening port for the Redis service.
        db (int): Logical database index within the Redis instance.
    """

    url: str = Field(description="Full Redis URL (Strictly typed as str)")

    host: str = Field(default="localhost", description="Redis host (REDIS__HOST)")
    port: int = Field(default=6379, description="Redis port (REDIS__PORT)")
    db: int = Field(default=0, description="Redis DB index (REDIS__DB)")

    model_config = {"extra": "ignore"}

    @model_validator(mode="before")
    @classmethod
    def assemble_redis_url(cls, values: dict) -> dict:
        """Enforces a canonical Redis URL for uniform adapter initialization.

        Providing multiple ways to define the connection can lead to
        hard-to-debug misconfigurations in distributed environments.

        Args:
            values (dict): Input configuration data.

        Returns:
            dict: Validated configuration.

        Raises:
            ValueError: If configuration is ambiguous or insufficient.
        """
        url = values.get("url")
        host = values.get("host", "localhost")
        port = values.get("port", 6379)
        db = values.get("db", 0)

        has_atomic_credentials = bool(
            "host" in values or "port" in values or "db" in values
        )

        if url and has_atomic_credentials:
            raise ValueError(
                "CRITICAL CONFIG CONFLICT: Choose to provide EITHER 'REDIS__URL' OR "
                "the atomic credentials ('REDIS__HOST', 'REDIS__PORT', 'REDIS__DB')."
            )

        if url:
            return values

        values["url"] = f"redis://{host}:{port}/{db}"
        return values


class OtelSettings(BaseModel):
    """OpenTelemetry configuration for Distributed Tracing and Observability.

    Integrates with Grafana Tempo/Loki for full request lifecycle visibility.

    Attributes:
        endpoint (str): The OTLP gRPC endpoint for trace ingestion.
        service_name (str): Identifier for this service within the trace topology.
        enabled (bool): Toggle for telemetry collection to avoid overhead in lean environments.
        excluded_urls (str): Urls excluded from OTel tracing.
    """

    endpoint: str = Field(
        description="OTLP gRPC endpoint for trace export (OTEL__ENDPOINT)",
    )
    service_name: str = Field(
        description="OTel service.name resource attribute (OTEL__SERVICE_NAME)",
    )
    enabled: bool = Field(
        default=True,
        description="Master switch for distributed tracing",
    )
    excluded_urls: str = Field(
        description="Urls excluded from OTel tracing (OTEL__EXCLUDED_URLS)"
    )
    model_config = {"extra": "ignore"}


class PrometheusSettings(BaseModel):
    """Configuration for Prometheus metrics."""
    pushgateway_url: str = Field(description="URL for Prometheus Pushgateway (PROMETHEUS__PUSHGATEWAY_URL)")
    model_config = {"extra": "ignore"}


class Settings(BaseSettings):
    """Root configuration object orchestrating all system parameters.

    Utilizes __ as a nested delimiter to allow environment variables like
    APP__DEBUG=true to be mapped to settings.app.debug.
    """

    b3: B3Settings = B3Settings()
    app: AppSettings
    db: DatabaseSettings
    redis: RedisSettings
    otel: OtelSettings
    prometheus: PrometheusSettings

    model_config = SettingsConfigDict(
        env_file=tuple(ENV_FILES),
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        case_sensitive=False,
        extra="ignore",
    )


# System-wide Settings Singleton.
# Initialized at import-time to enforce a Fail-Fast startup strategy if
# critical environment variables (like DB credentials) are missing.
settings = Settings()
