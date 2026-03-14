import math
from prometheus_client import Counter, Histogram, Gauge

def get_buckets(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """
    Gera buckets em escala logarítmica de min_val até max_val.
    O step representa o incremento no expoente (base 10).
    Ex: step=0.3 ~= fator de 2.
    """
    if min_val <= 0:
        raise ValueError("min_val deve ser maior que 0 para escala logarítmica")
    
    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)
    
    # +1e-9 para mitigar imprecisões de float no cálculo do range
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))

# ======================================================================
# 1. THE FOUR GOLDEN SIGNALS (System Health)
# ======================================================================

# LATENCY (Histogramas com buckets realistas para API)
HTTP_REQUEST_DURATION = Histogram(
    "http_request_duration_seconds",
    "Tempo de resposta da API em segundos",
    ["method", "endpoint"],
    buckets=get_buckets(0.01, 20.0, step=0.1)
)

# TRAFFIC
HTTP_REQUESTS_TOTAL = Counter(
    "http_requests_total",
    "Total de requisições HTTP recebidas",
    ["method", "endpoint", "status"]
)

# ERRORS
HTTP_REQUESTS_FAILED_TOTAL = Counter(
    "http_requests_failed_total",
    "Total de requisições que resultaram em erro",
    ["method", "endpoint", "error_type"]
)

# CONCURRENCY (In-Flight Requests)
IN_FLIGHT_REQUESTS = Gauge(
    "http_requests_in_flight",
    "Quantidade de requisições HTTP sendo processadas no momento",
    ["method", "endpoint"]
)

# PAYLOAD SIZES (Request)
HTTP_REQUEST_SIZE = Histogram(
    "http_request_size_bytes",
    "Tamanho do payload da requisição HTTP em bytes",
    ["method", "endpoint"],
    buckets=get_buckets(128, 1048576 * 10, step=0.6)
)

# SATURATION (Métrica de Domínio / Infra)
DB_CONNECTIONS_ACTIVE = Gauge(
    "db_connections_active",
    "Quantidade de conexões ativas no pool do banco de dados",
    ["database"]
)

# ======================================================================
# 2. DOMAIN METRICS (Ubiquitous Language & Business Outcomes)
# ======================================================================

# BUSINESS OUTCOMES
COMPANIES_SYNCED_TOTAL = Counter(
    "companies_synced_total",
    "Total de empresas sincronizadas pelo worker",
    ["status"]
)

# Legacy compatibility / Additional Domain Metrics
ENTITIES_SYNCED_TOTAL = COMPANIES_SYNCED_TOTAL # Alias if needed, but we'll update uses

ACTIVE_SYNC_TASKS = Gauge(
    "active_sync_tasks_count",
    "Number of background synchronization tasks currently running"
)

SYNC_DURATION_SECONDS = Histogram(
    "sync_duration_seconds",
    "Time spent in the synchronization use case",
    ["context"],
    buckets=get_buckets(0.1, 1800.0, step=0.3)
)

# DATA QUALITY
DATE_PARSING_FAILURES = Counter(
    "domain_date_parsing_failures_total",
    "Total number of failures during date string parsing (Data Quality)",
    ["field", "source"]
)

DATA_VALIDATION_ERRORS = Counter(
    "domain_data_validation_errors_total",
    "Total business validation failures (CNPJ, Ticker format, etc)",
    ["entity", "field", "reason"]
)

# ERRORS & FAILURES
GENERIC_SYNC_ERRORS = Counter(
    "domain_sync_errors_total",
    "Total generic or unexpected failures during synchronization",
    ["type"]
)

# INTEGRATION EFFICIENCY
B3_RATE_LIMIT_HITS = Counter(
    "domain_b3_rate_limit_hits_total",
    "Total HTTP 429 received from B3 Data Source"
)

# NETWORK / INFRA
NETWORK_TRANSMIT_BYTES_TOTAL = Counter(
    "network_transmit_bytes_total",
    "Total network traffic transmitted in bytes",
    ["direction", "context"]
)

HTTP_RESPONSE_SIZE = Histogram(
    "http_response_size_bytes",
    "Size of HTTP responses in bytes",
    ["method", "endpoint"],
    buckets=get_buckets(128, 1048576 * 10, step=0.6)
)

# MARKET INSIGHTS
COMPANIES_BY_SECTOR = Gauge(
    "domain_companies_by_sector_count",
    "Snapshot of company distribution by economic sector",
    ["sector"]
)

COMPANIES_BY_SEGMENT = Gauge(
    "domain_companies_by_segment_count",
    "Snapshot of company distribution by B3 listing segment",
    ["segment"]
)

NEW_ISSUERS_DISCOVERED = Counter(
    "domain_new_issuers_discovered_total",
    "Number of brand new companies discovered in the latest sync"
)

# ======================================================================
# 3. APP INFO (Deployment Tracking)
# ======================================================================
import os
from shared.infrastructure.config import settings

APP_INFO = Gauge(
    "app_info",
    "Informações estáticas sobre a aplicação (versão, ambiente)",
    ["version", "environment"]
)

# Seta o valor estático logo na inicialização
# Pode usar 'development' como fallback se APP_ENV não estiver setado
env = os.getenv("APP_ENV", "development")
APP_INFO.labels(version=getattr(settings.app, "version", "unknown"), environment=env).set(1)
