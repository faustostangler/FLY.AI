import pytest
from prometheus_client import REGISTRY
from shared.infrastructure.monitoring.metrics import MetricsProvider

def test_metrics_singleton():
    m1 = MetricsProvider()
    m2 = MetricsProvider()
    assert m1 is m2

def test_metrics_initialization():
    m = MetricsProvider()
    # Check if a few key metrics are present
    assert hasattr(m, "http_requests_total")
    assert hasattr(m, "date_parsing_failures")
    assert hasattr(m, "entities_synced_total")

def test_metrics_recording():
    m = MetricsProvider()
    
    # Capture initial value if possible, or just ensure it doesn't crash
    val_before = REGISTRY.get_sample_value("http_requests_total", {"method": "GET", "endpoint": "/test", "status": "200"}) or 0.0
    m.http_requests_total.labels(method="GET", endpoint="/test", status="200").inc()
    m.date_parsing_failures.labels(field="test_field", source="test_source").inc()
    
    # Verify they are in the registry and incremented correctly
    val_after = REGISTRY.get_sample_value("http_requests_total", {"method": "GET", "endpoint": "/test", "status": "200"})
    assert val_after == val_before + 1.0
