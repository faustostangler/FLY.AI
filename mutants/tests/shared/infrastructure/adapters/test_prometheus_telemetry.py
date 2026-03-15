import pytest
from unittest.mock import patch

from shared.infrastructure.adapters.prometheus_telemetry import PrometheusTelemetryAdapter

class TestPrometheusTelemetryAdapter:
    """Contract tests for the Prometheus Telemetry Adapter.

    Ensures that domain metrics events correctly actuate the underlying
    Prometheus SDK implementations without bleeding infrastructure logic
    into the Domain or Application layers.
    """

    @pytest.fixture
    def adapter(self):
        return PrometheusTelemetryAdapter()

    @patch("shared.infrastructure.adapters.prometheus_telemetry.ACTIVE_SYNC_TASKS.inc")
    def test_increment_active_sync_tasks(self, mock_inc, adapter):
        adapter.increment_active_sync_tasks()
        mock_inc.assert_called_once()

    @patch("shared.infrastructure.adapters.prometheus_telemetry.ACTIVE_SYNC_TASKS.dec")
    def test_decrement_active_sync_tasks(self, mock_dec, adapter):
        adapter.decrement_active_sync_tasks()
        mock_dec.assert_called_once()

    @patch("shared.infrastructure.adapters.prometheus_telemetry.COMPANIES_SYNCED_TOTAL.labels")
    def test_increment_companies_synced(self, mock_labels, adapter):
        adapter.increment_companies_synced(count=5, status="success")
        mock_labels.assert_called_once_with(status="success")
        mock_labels.return_value.inc.assert_called_once_with(5)

    @patch("shared.infrastructure.adapters.prometheus_telemetry.COMPANIES_BY_SECTOR.labels")
    def test_set_companies_by_sector(self, mock_labels, adapter):
        adapter.set_companies_by_sector("Energy", 10)
        mock_labels.assert_called_once_with(sector="Energy")
        mock_labels.return_value.set.assert_called_once_with(10)

    @patch("shared.infrastructure.adapters.prometheus_telemetry.COMPANIES_BY_SEGMENT.labels")
    def test_set_companies_by_segment(self, mock_labels, adapter):
        adapter.set_companies_by_segment("Novo Mercado", 50)
        mock_labels.assert_called_once_with(segment="Novo Mercado")
        mock_labels.return_value.set.assert_called_once_with(50)

    @patch("shared.infrastructure.adapters.prometheus_telemetry.SYNC_DURATION_SECONDS.labels")
    def test_observe_sync_duration(self, mock_labels, adapter):
        adapter.observe_sync_duration("API", 1.5)
        mock_labels.assert_called_once_with(context="API")
        mock_labels.return_value.observe.assert_called_once_with(1.5)

    @patch("shared.infrastructure.adapters.prometheus_telemetry.DATE_PARSING_FAILURES.labels")
    def test_increment_date_parsing_failures(self, mock_labels, adapter):
        adapter.increment_date_parsing_failures("dateListing", "invalid format")
        mock_labels.assert_called_once_with(field="dateListing", source="invalid format")
        mock_labels.return_value.inc.assert_called_once()

    @patch("shared.infrastructure.adapters.prometheus_telemetry.B3_RATE_LIMIT_HITS.inc")
    def test_increment_b3_rate_limit_hits(self, mock_inc, adapter):
        adapter.increment_b3_rate_limit_hits()
        mock_inc.assert_called_once()

    @patch("shared.infrastructure.adapters.prometheus_telemetry.NETWORK_TRANSMIT_BYTES_TOTAL.labels")
    def test_increment_network_transmit_bytes(self, mock_labels, adapter):
        adapter.increment_network_transmit_bytes("tx", "api_call", 1024)
        mock_labels.assert_called_once_with(direction="tx", context="api_call")
        mock_labels.return_value.inc.assert_called_once_with(1024)

    @patch("shared.infrastructure.adapters.prometheus_telemetry.DATA_VALIDATION_ERRORS.labels")
    def test_increment_data_validation_error(self, mock_labels, adapter):
        adapter.increment_data_validation_error("Company", "cnpj", "invalid schema")
        mock_labels.assert_called_once_with(entity="Company", field="cnpj", reason="invalid schema")
        mock_labels.return_value.inc.assert_called_once()

    @patch("shared.infrastructure.adapters.prometheus_telemetry.GENERIC_SYNC_ERRORS.labels")
    def test_increment_generic_sync_error(self, mock_labels, adapter):
        adapter.increment_generic_sync_error("NetworkError")
        mock_labels.assert_called_once_with(type="NetworkError")
        mock_labels.return_value.inc.assert_called_once()
