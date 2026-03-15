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

    def test_abstract_methods_do_nothing(self):
        """Verify the abstract methods simply pass when explicitly called (e.g. via super)."""

        class DummyPort(TelemetryPort):
            def increment_active_sync_tasks(self):
                super().increment_active_sync_tasks()

            def decrement_active_sync_tasks(self):
                super().decrement_active_sync_tasks()

            def increment_companies_synced(self, count, status):
                super().increment_companies_synced(count, status)

            def set_companies_by_sector(self, sector, count):
                super().set_companies_by_sector(sector, count)

            def set_companies_by_segment(self, segment, count):
                super().set_companies_by_segment(segment, count)

            def observe_sync_duration(self, context, duration):
                super().observe_sync_duration(context, duration)

            def increment_date_parsing_failures(self, field, source):
                super().increment_date_parsing_failures(field, source)

            def increment_b3_rate_limit_hits(self):
                super().increment_b3_rate_limit_hits()

            def increment_network_transmit_bytes(
                self, direction, context, payload_size
            ):
                super().increment_network_transmit_bytes(
                    direction, context, payload_size
                )

            def increment_data_validation_error(self, entity, field, reason):
                super().increment_data_validation_error(entity, field, reason)

            def increment_generic_sync_error(self, type):
                super().increment_generic_sync_error(type)

        port = DummyPort()

        # Test each method to hit the "pass" block in the ABC
        port.increment_active_sync_tasks()
        port.decrement_active_sync_tasks()
        port.increment_companies_synced(1, "x")
        port.set_companies_by_sector("x", 1)
        port.set_companies_by_segment("y", 1)
        port.observe_sync_duration("a", 1.0)
        port.increment_date_parsing_failures("x", "y")
        port.increment_b3_rate_limit_hits()
        port.increment_network_transmit_bytes("x", "y", 1)
        port.increment_data_validation_error("x", "y", "z")
        port.increment_generic_sync_error("x")
