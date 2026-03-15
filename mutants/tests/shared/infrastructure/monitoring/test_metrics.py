"""Tests for the Prometheus metrics infrastructure module.

Validates that the Golden Signals and Domain Metrics defined in
metrics.py are correctly registered in the Prometheus collector
registry and can be incremented without errors.
"""

import pytest
from prometheus_client import REGISTRY
from shared.infrastructure.monitoring import metrics


class TestGoldenSignalMetrics:
    """Verifies the Four Golden Signals metric definitions."""

    def test_http_request_duration_exists(self):
        """Latency signal: histogram for API response times."""
        assert metrics.HTTP_REQUEST_DURATION is not None

    def test_http_requests_total_exists(self):
        """Traffic signal: counter for total HTTP requests."""
        assert metrics.HTTP_REQUESTS_TOTAL is not None

    def test_http_requests_failed_total_exists(self):
        """Error signal: counter for failed HTTP requests."""
        assert metrics.HTTP_REQUESTS_FAILED_TOTAL is not None

    def test_in_flight_requests_exists(self):
        """Saturation signal: gauge for concurrent requests."""
        assert metrics.IN_FLIGHT_REQUESTS is not None


class TestDomainMetrics:
    """Verifies Domain Metrics use Ubiquitous Language."""

    def test_companies_synced_total_exists(self):
        """Business KPI: counter for B3 sync outcomes."""
        assert metrics.COMPANIES_SYNCED_TOTAL is not None

    def test_active_sync_tasks_exists(self):
        """Saturation: gauge for running sync workers."""
        assert metrics.ACTIVE_SYNC_TASKS is not None

    def test_sync_duration_seconds_exists(self):
        """Latency: histogram for sync wall-clock time."""
        assert metrics.SYNC_DURATION_SECONDS is not None

    def test_date_parsing_failures_exists(self):
        """Data Quality: counter for date parsing failures."""
        assert metrics.DATE_PARSING_FAILURES is not None

    def test_data_validation_errors_exists(self):
        """Data Quality: counter for business rule violations."""
        assert metrics.DATA_VALIDATION_ERRORS is not None

    def test_b3_rate_limit_hits_exists(self):
        """External Adapter: counter for B3 429 responses."""
        assert metrics.B3_RATE_LIMIT_HITS is not None


class TestMetricRegistration:
    """Validates that metrics correctly interact with the Prometheus registry."""

    def test_counter_increment_succeeds(self):
        """Counters must be incrementable without raising."""
        before = REGISTRY.get_sample_value(
            "http_requests_total",
            {"method": "GET", "endpoint": "/test_metric", "status": "200"},
        ) or 0.0

        metrics.HTTP_REQUESTS_TOTAL.labels(
            method="GET", endpoint="/test_metric", status="200"
        ).inc()

        after = REGISTRY.get_sample_value(
            "http_requests_total",
            {"method": "GET", "endpoint": "/test_metric", "status": "200"},
        )
        assert after == before + 1.0

    def test_gauge_inc_dec_succeeds(self):
        """Gauges must support increment and decrement."""
        metrics.ACTIVE_SYNC_TASKS.inc()
        metrics.ACTIVE_SYNC_TASKS.dec()

    def test_histogram_observe_succeeds(self):
        """Histograms must accept observation values."""
        metrics.SYNC_DURATION_SECONDS.labels(context="test").observe(1.5)


class TestGetBuckets:
    """Tests for the logarithmic bucket generator."""

    def test_get_buckets_returns_tuple(self):
        """Must return a tuple of floats."""
        result = metrics.get_buckets(1, 100, 0.5)
        assert isinstance(result, tuple)
        assert all(isinstance(b, float) for b in result)

    def test_get_buckets_ascending_order(self):
        """Bucket boundaries must be in strictly ascending order."""
        result = metrics.get_buckets(1, 100, 0.5)
        for i in range(len(result) - 1):
            assert result[i] < result[i + 1]

    def test_get_buckets_raises_on_zero_min(self):
        """log10(0) is undefined — must raise ValueError."""
        with pytest.raises(ValueError, match="min_val must be greater than 0"):
            metrics.get_buckets(0, 100, 0.5)

    def test_get_buckets_raises_on_negative_min(self):
        """Negative values must also raise ValueError."""
        with pytest.raises(ValueError, match="min_val must be greater than 0"):
            metrics.get_buckets(-1, 100, 0.5)

    def test_get_buckets_first_bucket_matches_min(self):
        """First bucket should be approximately equal to min_val."""
        result = metrics.get_buckets(1.0, 100, 0.5)
        assert result[0] == pytest.approx(1.0, abs=0.01)
