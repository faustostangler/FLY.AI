import logging
from unittest.mock import patch, MagicMock

from shared.infrastructure.monitoring.tracing import OTelLogFilter, setup_tracing


class TestTracing:
    """Verifies the OpenTelemetry initialization schema.

    Observability is not optional. Ensuring traces and logs are tied
    perfectly together (trace_id / span_id injection) enables full distributed debugging.
    """

    def test_otel_log_filter_injects_ids_when_recording(self):
        """Verifies exactly that when OTel is recording a span, IDs are ported to the log record."""
        log_filter = OTelLogFilter()
        record = logging.LogRecord(
            "test_logger", logging.INFO, "path", 10, "Test Message", (), None
        )

        with patch(
            "shared.infrastructure.monitoring.tracing.trace.get_current_span"
        ) as mock_get_span:
            mock_span = MagicMock()
            mock_span.is_recording.return_value = True

            # Simulated IDs from context
            mock_ctx = MagicMock()
            mock_ctx.trace_id = 0xABCDEF1234567890ABCDEF1234567890
            mock_ctx.span_id = 0x1234567890ABCDEF
            mock_span.get_span_context.return_value = mock_ctx
            mock_get_span.return_value = mock_span

            result = log_filter.filter(record)

            assert result is True
            assert getattr(record, "trace_id") == format(mock_ctx.trace_id, "032x")
            assert getattr(record, "span_id") == format(mock_ctx.span_id, "016x")

    def test_otel_log_filter_defaults_to_zeros_when_no_active_span(self):
        """If there is no active Span, log formatters shouldn't crash; they should get zeroes."""
        log_filter = OTelLogFilter()
        record = logging.LogRecord(
            "test_logger", logging.INFO, "path", 10, "Test Message", (), None
        )

        with patch(
            "shared.infrastructure.monitoring.tracing.trace.get_current_span"
        ) as mock_get_span:
            mock_span = MagicMock()
            mock_span.is_recording.return_value = False

            mock_ctx = MagicMock()
            mock_ctx.trace_id = 0
            mock_span.get_span_context.return_value = mock_ctx
            mock_get_span.return_value = mock_span

            result = log_filter.filter(record)

            assert result is True
            assert getattr(record, "trace_id") == "0" * 32
            assert getattr(record, "span_id") == "0" * 16

    @patch("shared.infrastructure.monitoring.tracing.trace.set_tracer_provider")
    @patch("shared.infrastructure.monitoring.tracing.BatchSpanProcessor")
    @patch("shared.infrastructure.monitoring.tracing.OTLPSpanExporter")
    @patch("shared.infrastructure.monitoring.tracing.TracerProvider")
    @patch("shared.infrastructure.monitoring.tracing.Resource.create")
    def test_setup_tracing_happy_path(
        self,
        mock_resource,
        mock_provider,
        mock_exporter,
        mock_processor,
        mock_set_provider,
    ):
        """Verifies the core architectural hooks for OpenTelemetry wireup."""
        mock_resource.return_value = "mocked_resource"
        mock_provider_instance = MagicMock()
        mock_provider.return_value = mock_provider_instance

        setup_tracing(service_name="test_service")

        # Verify provider setup
        mock_provider.assert_called_once_with(resource="mocked_resource")
        mock_exporter.assert_called_once()
        mock_processor.assert_called_once()
        mock_provider_instance.add_span_processor.assert_called_once()

        mock_set_provider.assert_called_once_with(mock_provider_instance)

    @patch("shared.infrastructure.monitoring.tracing.trace.set_tracer_provider")
    @patch("shared.infrastructure.monitoring.tracing.BatchSpanProcessor")
    @patch("shared.infrastructure.monitoring.tracing.OTLPSpanExporter")
    @patch("shared.infrastructure.monitoring.tracing.TracerProvider")
    @patch("shared.infrastructure.monitoring.tracing.Resource.create")
    def test_setup_tracing_graceful_exporter_failure(
        self,
        mock_resource,
        mock_provider,
        mock_exporter,
        mock_processor,
        mock_set_provider,
        caplog,
    ):
        """SRE resilience: Tracing failures shouldn't crash the application."""
        mock_exporter.side_effect = Exception("OTLP network failure")

        import logging

        with caplog.at_level(logging.WARNING):
            setup_tracing()

        assert "OTel exporter failed to initialize" in caplog.text

        # Provider should still be set to avoid trace calls crashing internally
        mock_set_provider.assert_called_once()

    @patch("shared.infrastructure.monitoring.tracing.FastAPIInstrumentor")
    @patch("shared.infrastructure.monitoring.tracing.SQLAlchemyInstrumentor")
    @patch("shared.infrastructure.monitoring.tracing.OTLPSpanExporter")
    def test_setup_tracing_auto_instrumentation(
        self, mock_exporter, mock_sql, mock_fastapi
    ):
        """Check if FastAPI and SQLAlchemy get instrumented correctly when passed."""
        app_mock = MagicMock()
        engine_mock = MagicMock()

        setup_tracing(app=app_mock, engine=engine_mock)

        mock_fastapi.instrument_app.assert_called_once()

        # Verify SQLAlchemy instrument is called
        mock_sql_instance = mock_sql.return_value
        mock_sql_instance.instrument.assert_called_once_with(engine=engine_mock)

    def test_otel_log_filter_ignores_valid_trace_id_if_not_recording(self):
        """
        Mata o mutante que troca 'and' por 'or'.
        Prova que se o span não estiver a gravar (mesmo tendo um trace_id residual),
        os IDs de correlação devem ser zerados para não poluir o Grafana Loki.
        """
        from shared.infrastructure.monitoring.tracing import OTelLogFilter
        import logging

        # 1. Setup: Criamos um mock de um Span que NÃO está a gravar (False)
        mock_span = MagicMock()
        mock_span.is_recording.return_value = False

        # 2. Setup: Mas o contexto AINDA tem um trace_id válido (!= 0) (True)
        mock_ctx = MagicMock()
        mock_ctx.trace_id = 123456789
        mock_span.get_span_context.return_value = mock_ctx

        # Interceptamos a chamada ao OpenTelemetry
        with patch(
            "shared.infrastructure.monitoring.tracing.trace.get_current_span",
            return_value=mock_span,
        ):
            log_filter = OTelLogFilter()
            record = logging.LogRecord(
                "name", logging.INFO, "pathname", 1, "msg", (), None
            )

            # Executa
            log_filter.filter(record)

            # VALIDAÇÃO COMPORTAMENTAL ESTRITA:
            # Como is_recording() é False, o 'AND' original forçaria a cair no 'else'.
            # O mutante 'OR' cairia no 'if' e injetaria o "123456789" formatado.
            # Nós exigimos que caia no 'else' (tudo zeros).
            assert record.trace_id == "00000000000000000000000000000000", (
                "Falha Crítica: LogFilter aceitou um span que não está a gravar!"
            )
            assert record.span_id == "0000000000000000", (
                "Falha Crítica: LogFilter vazou o span_id!"
            )
