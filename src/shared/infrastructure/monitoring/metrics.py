from prometheus_client import Counter, Histogram, Gauge, REGISTRY

class MetricsProvider:
    """
    Centralized Prometheus metrics provider for FLY.AI.
    Implements the Four Golden Signals and Domain-Driven Metrics.
    """
    _instance = None
    _registry = REGISTRY
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MetricsProvider, cls).__new__(cls)
            cls._instance._init_metrics()
        return cls._instance
    
    def _init_metrics(self):
        # ======================================================================
        # 1. THE FOUR GOLDEN SIGNALS (System Health)
        # ======================================================================
        
        # LATENCY: The time it takes to service a request
        self.http_request_duration_seconds = Histogram(
            "http_request_duration_seconds",
            "Latency of HTTP requests in seconds",
            ["method", "endpoint"]
        )
        
        # TRAFFIC: Demand placed on the system
        self.http_requests_total = Counter(
            "http_requests_total",
            "Total number of HTTP requests handled",
            ["method", "endpoint", "status"]
        )
        
        # ERRORS: The rate of requests that fail
        self.http_requests_failed_total = Counter(
            "http_requests_failed_total",
            "Total number of HTTP requests that resulted in an error",
            ["method", "endpoint", "error_type"]
        )
        
        # NETWORK: Payload and transmission sizes
        self.http_response_size_bytes = Histogram(
            "http_response_size_bytes",
            "Size of HTTP responses in bytes",
            ["method", "endpoint"],
            buckets=[128, 512, 1024, 5120, 10240, 51200, 102400, 512000, 1048576, 5242880]
        )
        
        self.network_transmit_bytes_total = Counter(
            "network_transmit_bytes_total",
            "Total network traffic transmitted in bytes",
            ["direction", "context"] # direction='inbound' (download) or 'outbound' (api response)
        )
        
        # SATURATION: How 'full' the service is
        self.active_sync_tasks = Gauge(
            "active_sync_tasks_count",
            "Number of background synchronization tasks currently running"
        )
        
        # ======================================================================
        # 2. DOMAIN METRICS (Ubiquitous Language & Business Outcomes)
        # ======================================================================
        
        # DATA QUALITY: Resilience monitoring
        self.date_parsing_failures = Counter(
            "domain_date_parsing_failures_total",
            "Total number of failures during date string parsing (Data Quality)",
            ["field", "source"]
        )
        
        self.data_validation_errors = Counter(
            "domain_data_validation_errors_total",
            "Total business validation failures (CNPJ, Ticker format, etc)",
            ["entity", "field", "reason"]
        )
        
        # BUSINESS LIFECYCLE: Tracking market events
        self.entities_synced_total = Counter(
            "domain_entities_synced_total",
            "Total companies successfully synchronized with the database",
            ["context", "source"]
        )
        
        self.new_issuers_discovered = Counter(
            "domain_new_issuers_discovered_total",
            "Number of brand new companies discovered in the latest sync"
        )
        
        # INTEGRATION EFFICIENCY: Provider health
        self.b3_rate_limit_hits = Counter(
            "domain_b3_rate_limit_hits_total",
            "Total HTTP 429 received from B3 Data Source"
        )
        
        # MARKET INSIGHTS: High-level business state
        self.companies_by_sector = Gauge(
            "domain_companies_by_sector_count",
            "Snapshot of company distribution by economic sector",
            ["sector"]
        )
        
        self.companies_by_segment = Gauge(
            "domain_companies_by_segment_count",
            "Snapshot of company distribution by B3 listing segment",
            ["segment"]
        )

        # Legacy/Support
        self.sync_duration_seconds = Histogram(
            "sync_duration_seconds",
            "Time spent in the synchronization use case",
            ["context"]
        )

# Global metrics accessibility
metrics = MetricsProvider()
