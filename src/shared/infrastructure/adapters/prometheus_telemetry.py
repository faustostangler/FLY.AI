from shared.domain.ports.telemetry_port import TelemetryPort
from shared.infrastructure.monitoring.metrics import (
    ACTIVE_SYNC_TASKS,
    COMPANIES_SYNCED_TOTAL,
    COMPANIES_BY_SECTOR,
    COMPANIES_BY_SEGMENT,
    SYNC_DURATION_SECONDS,
    DATE_PARSING_FAILURES,
    B3_RATE_LIMIT_HITS,
    NETWORK_TRANSMIT_BYTES_TOTAL,
)

class PrometheusTelemetryAdapter(TelemetryPort):
    def increment_active_sync_tasks(self) -> None:
        ACTIVE_SYNC_TASKS.inc()

    def decrement_active_sync_tasks(self) -> None:
        ACTIVE_SYNC_TASKS.dec()

    def increment_companies_synced(self, count: int, status: str) -> None:
        COMPANIES_SYNCED_TOTAL.labels(status=status).inc(count)

    def set_companies_by_sector(self, sector: str, count: int) -> None:
        COMPANIES_BY_SECTOR.labels(sector=sector).set(count)

    def set_companies_by_segment(self, segment: str, count: int) -> None:
        COMPANIES_BY_SEGMENT.labels(segment=segment).set(count)

    def observe_sync_duration(self, context: str, duration: float) -> None:
        SYNC_DURATION_SECONDS.labels(context=context).observe(duration)

    def increment_date_parsing_failures(self, field: str, source: str) -> None:
        DATE_PARSING_FAILURES.labels(field=field, source=source).inc()

    def increment_b3_rate_limit_hits(self) -> None:
        B3_RATE_LIMIT_HITS.inc()

    def increment_network_transmit_bytes(self, direction: str, context: str, payload_size: int) -> None:
        NETWORK_TRANSMIT_BYTES_TOTAL.labels(direction=direction, context=context).inc(payload_size)
