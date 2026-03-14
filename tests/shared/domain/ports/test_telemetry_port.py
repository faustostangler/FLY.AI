"""Contract tests for the TelemetryPort abstract interface.

Verifies that the port contract is correctly defined and that
any concrete adapter implementing TelemetryPort will satisfy
the expected interface. This is a Consumer-Driven Contract test
at the Domain layer — no infrastructure dependencies.
"""

import pytest
from abc import ABC
from shared.domain.ports.telemetry_port import TelemetryPort


class TestTelemetryPortContract:
    """Ensures the TelemetryPort ABC defines the complete domain contract."""

    def test_telemetry_port_is_abstract(self):
        """TelemetryPort must be abstract — direct instantiation is forbidden."""
        assert issubclass(TelemetryPort, ABC)
        with pytest.raises(TypeError):
            TelemetryPort()

    def test_telemetry_port_defines_sync_task_lifecycle(self):
        """Domain requires active sync task tracking (Saturation signal)."""
        assert hasattr(TelemetryPort, "increment_active_sync_tasks")
        assert hasattr(TelemetryPort, "decrement_active_sync_tasks")

    def test_telemetry_port_defines_companies_synced(self):
        """Domain requires issuer sync outcome tracking (Business KPI)."""
        assert hasattr(TelemetryPort, "increment_companies_synced")

    def test_telemetry_port_defines_sector_segment_gauges(self):
        """Domain requires real-time universe distribution metrics."""
        assert hasattr(TelemetryPort, "set_companies_by_sector")
        assert hasattr(TelemetryPort, "set_companies_by_segment")

    def test_telemetry_port_defines_sync_duration(self):
        """Domain requires sync latency observation (Latency signal)."""
        assert hasattr(TelemetryPort, "observe_sync_duration")

    def test_telemetry_port_defines_date_parsing_failures(self):
        """Domain requires data quality tracking for ACL resilience."""
        assert hasattr(TelemetryPort, "increment_date_parsing_failures")

    def test_telemetry_port_defines_rate_limit_tracking(self):
        """Domain requires B3 rate limit hit tracking (External adapter health)."""
        assert hasattr(TelemetryPort, "increment_b3_rate_limit_hits")

    def test_telemetry_port_defines_network_bytes(self):
        """Domain requires network traffic measurement (Traffic signal)."""
        assert hasattr(TelemetryPort, "increment_network_transmit_bytes")

    def test_telemetry_port_defines_validation_errors(self):
        """Domain requires data validation error tracking (Error signal)."""
        assert hasattr(TelemetryPort, "increment_data_validation_error")

    def test_telemetry_port_defines_generic_sync_errors(self):
        """Domain requires catch-all error taxonomy for unexpected failures."""
        assert hasattr(TelemetryPort, "increment_generic_sync_error")

    def test_concrete_mock_satisfies_contract(self, mock_telemetry):
        """A valid implementation must pass isinstance check."""
        assert isinstance(mock_telemetry, TelemetryPort)

    def test_concrete_mock_methods_are_callable(self, mock_telemetry):
        """All contract methods must be callable without raising."""
        mock_telemetry.increment_active_sync_tasks()
        mock_telemetry.decrement_active_sync_tasks()
        mock_telemetry.increment_companies_synced(count=10, status="success")
        mock_telemetry.set_companies_by_sector(sector="Financeiro", count=42)
        mock_telemetry.set_companies_by_segment(segment="NM", count=100)
        mock_telemetry.observe_sync_duration(context="companies", duration=12.5)
        mock_telemetry.increment_date_parsing_failures(field="date_listing", source="B3")
        mock_telemetry.increment_b3_rate_limit_hits()
        mock_telemetry.increment_network_transmit_bytes(
            direction="inbound", context="b3_initial", payload_size=1024
        )
        mock_telemetry.increment_data_validation_error(
            entity="Company", field="cnpj", reason="invalid_check_digits"
        )
        mock_telemetry.increment_generic_sync_error(type="TimeoutError")
