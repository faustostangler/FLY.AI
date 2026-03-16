import math
from prometheus_client import Counter, Histogram, Gauge
from shared.infrastructure.config import settings


def get_buckets(min_val: float = 1, max_val: float = 100, step: float = 0.1):
    """Generates logarithmic buckets for Prometheus histograms.

    Logarithmic spacing is superior for request durations and payload sizes
    across several orders of magnitude, providing higher resolution at lower values
    where most requests fall, while still capturing long-tail outliers.

    Args:
        min_val (float): The starting value for the first bucket.
        max_val (float): The upper bound for the last bucket.
        step (float): The logarithmic step (base 10) between buckets.

    Returns:
        tuple[float]: A sequence of rounded bucket boundaries.

    Raises:
        ValueError: If min_val is non-positive, as log10 requires positive values.
    """
    if min_val <= 0:
        raise ValueError("min_val must be greater than 0 for logarithmic scale.")

    start_exp = math.log10(min_val)
    end_exp = math.log10(max_val)

    # +1e-9 to mitigate float precision issues during range calculation.
    num_steps = int((end_exp - start_exp) / step + 1e-9) + 1
    return tuple(round(10 ** (start_exp + i * step), 4) for i in range(num_steps))


# ======================================================================
# 1. THE FOUR GOLDEN SIGNALS (System Health & SRE Compliance)
# ======================================================================

# LATENCY: Measures the time it takes to service a request.
# Tracking latency allows for the detection of performance regressions
# and the identification of slow path bottlenecks in the API layer.
HTTP_REQUEST_DURATION = Histogram(
    "http_request_duration_seconds",
    "API response time in seconds",
    ["method", "endpoint"],
    buckets=get_buckets(0.01, 20.0, step=0.1),
)

# TRAFFIC: Measures the demand placed on the system.
# Essential for capacity planning and understanding the impact of
# external events or automated scrapers on the platform.
HTTP_REQUESTS_TOTAL = Counter(
    "http_requests_total",
    "Total count of received HTTP requests",
    ["method", "endpoint", "status"],
)

# ERRORS: Measures the rate of requests that fail.
# High error rates are the primary indicator of system instability
# or upstream data source failures.
HTTP_REQUESTS_FAILED_TOTAL = Counter(
    "http_requests_failed_total",
    "Total count of failed HTTP requests",
    ["method", "endpoint", "error_type"],
)

# CONCURRENCY (Saturation): Measures how "full" the service is.
# Monitoring in-flight requests helps prevent cascading failures
# caused by resource exhaustion.
IN_FLIGHT_REQUESTS = Gauge(
    "http_requests_in_flight",
    "Current number of concurrent HTTP requests being processed",
    ["method", "endpoint"],
)

# PAYLOAD SIZES: Tracks data volume per interaction.
# Unexpected spikes in request size can indicate malicious behavior
# or misalignment between the scraper and the API.
HTTP_REQUEST_SIZE = Histogram(
    "http_request_size_bytes",
    "Size of the HTTP request payload in bytes",
    ["method", "endpoint"],
    buckets=get_buckets(128, 1048576 * 10, step=0.6),
)

# SATURATION (Infra): Low-level resource utilization.
# Tracking DB connections prevents "maximum connections reached" errors
# during high-concurrency sync cycles.
DB_CONNECTIONS_ACTIVE = Gauge(
    "db_connections_active",
    "Number of active connections in the database pool",
    ["database"],
)

# ======================================================================
# 2. DOMAIN METRICS (Ubiquitous Language & Business Outcomes)
# ======================================================================

# BUSINESS OUTCOME: Success of the B3 Synchronization event.
# This is the primary KPI for the platform's core value proposition.
COMPANIES_SYNCED_TOTAL = Counter(
    "companies_synced_total",
    "Total count of companies processed during synchronization",
    ["status"],
)

# Alias for legacy compatibility (should be deprecated when refactoring finishes).
ENTITIES_SYNCED_TOTAL = COMPANIES_SYNCED_TOTAL

ACTIVE_SYNC_TASKS = Gauge(
    "active_sync_tasks_count",
    "Number of background synchronization tasks currently running",
)

# SYNC DURATION: Measures the efficiency of the domain sync logic.
# Long sync times directly delay data availability for downstream analysis.
SYNC_DURATION_SECONDS = Histogram(
    "sync_duration_seconds",
    "Wall-clock time spent in the synchronization use case",
    ["context"],
    buckets=get_buckets(0.1, 1800.0, step=0.3),
)

# DATA QUALITY: Measures the integrity of the information retrieved from B3.
# Parsing failures signal changes in B3's internal data formats that
# require adaptation in the Infrastructure layer (ACL).
DATE_PARSING_FAILURES = Counter(
    "domain_date_parsing_failures_total",
    "Total occurrences of date-string parsing failures (Data Integrity KPI)",
    ["field", "source"],
)

DATA_VALIDATION_ERRORS = Counter(
    "domain_data_validation_errors_total",
    "Total business rule violations (e.g., invalid CNPJ or Ticker format)",
    ["entity", "field", "reason"],
)

# DOMAIN RESILIENCE: Tracks how the domain handles errors.
GENERIC_SYNC_ERRORS = Counter(
    "domain_sync_errors_total",
    "Total unexpected failures during the orchestration of sync tasks",
    ["type"],
)

SYNC_TRIGGER_REJECTED = Counter(
    "domain_sync_trigger_rejected_total",
    "Total times a sync was rejected (e.g., due to daily idempotency)",
    ["reason"],
)

# EXTERNAL ADAPTER PERFORMANCE: Monitored via Rate Limit Detection.
# Frequent 429s from B3 indicate that the 'max_concurrency' setting
# is too aggressive for current infrastructure limits.
B3_RATE_LIMIT_HITS = Counter(
    "domain_b3_rate_limit_hits_total",
    "Total count of HTTP 429 (Too Many Requests) received from B3",
)

# NETWORK EFFICIENCY
NETWORK_TRANSMIT_BYTES_TOTAL = Counter(
    "network_transmit_bytes_total",
    "Accumulated network traffic transmitted in bytes",
    ["direction", "context"],
)

HTTP_RESPONSE_SIZE = Histogram(
    "http_response_size_bytes",
    "Size of the HTTP responses returned to clients/workers",
    ["method", "endpoint"],
    buckets=get_buckets(128, 1048576 * 10, step=0.6),
)

# DOMAIN SNAPSHOTS: Real-time status of the Financial Universe.
COMPANIES_BY_SECTOR = Gauge(
    "domain_companies_by_sector_count",
    "Current distribution of issuers grouped by Economic Sector",
    ["sector"],
)

COMPANIES_BY_SEGMENT = Gauge(
    "domain_companies_by_segment_count",
    "Current distribution of issuers grouped by B3 Listing Segment",
    ["segment"],
)

NEW_ISSUERS_DISCOVERED = Counter(
    "domain_new_issuers_discovered_total",
    "Count of previously unknown issuers identified in the latest sync cycle",
)

# ======================================================================
# 3. APP INFO (Deployment & Version Tracking)
# ======================================================================

# APP METADATA: Static information exported as a Gauge with value 1.
# Allows for grouping metrics by version or environment in Grafana
# to detect if a specific deployment version introduced a regression.
APP_INFO = Gauge(
    "app_info",
    "Static metadata about the running instance (version, environment)",
    ["version", "environment"],
)

# Initialize static values at startup.
APP_INFO.labels(
    version=getattr(settings.app, "version", "unknown"), environment=settings.app.environment
).set(1)
