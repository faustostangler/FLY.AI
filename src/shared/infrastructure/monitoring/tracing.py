"""OpenTelemetry Tracing Setup — Distributed Observability Infrastructure.

This module assembles the tracing pipeline, connecting the system to 
Grafana Tempo for distributed tracing and Loki for log correlation.
Strict adherence to Hexagonal Architecture ensures that the Domain layer 
remains pure and unaware of this instrumentation.
"""

import logging
import os
from typing import Optional

from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.sqlalchemy import SQLAlchemyInstrumentor


logger = logging.getLogger(__name__)


class OTelLogFilter(logging.Filter):
    """Enriches log records with OpenTelemetry context for correlation.

    Injected Trace IDs and Span IDs allow for seamless pivoting between 
    logs in Loki and traces in Tempo within Grafana. Without this correlation, 
    debugging distributed failures becomes a needle-in-a-haystack operation.

    Format placeholders available for log formatters: %(trace_id)s, %(span_id)s
    """

    def filter(self, record: logging.LogRecord) -> bool:
        """Injects OTel metadata into every LogRecord passed through this filter.

        Standard logging doesn't know about the current execution context. 
        We extract it here to ensure every log line is traceable.

        Args:
            record (logging.LogRecord): The log record to be enriched.

        Returns:
            bool: Always True to allow the record to propagate.
        """
        span = trace.get_current_span()
        ctx = span.get_span_context()

        # If we have an active, recordable span, inject hex-encoded IDs.
        if span.is_recording() and ctx.trace_id != 0:
            record.trace_id = format(ctx.trace_id, "032x")  # type: ignore[attr-defined]
            record.span_id = format(ctx.span_id, "016x")  # type: ignore[attr-defined]
        else:
            # Provide zeroed defaults to avoid KeyError in format strings 
            # when no trace context exists.
            record.trace_id = "0" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True


def setup_tracing(
    app: Optional[object] = None,
    engine: Optional[object] = None,
    service_name: Optional[str] = None,
) -> None:
    """Bootstraps the global OpenTelemetry pipeline and auto-instrumentation.

    Centralizing tracing setup in a single entry point ensures consistent 
    resource attributes and exporter configurations across all system roles 
    (API, Scraper, Worker).

    Args:
        app (Optional[object]): FastAPI application instance for HTTP instrumentation.
        engine (Optional[object]): SQLAlchemy engine instance for SQL query spans.
        service_name (Optional[str]): Human-readable identifier for the service.
            Defaults to OTEL_SERVICE_NAME env var or 'fly_ai_core'.

    Note:
        This function is idempotent and should be called once during the 
        application's 'startup' or 'lifespan' event.
    """
    resolved_name = service_name or os.getenv("OTEL_SERVICE_NAME", "fly_ai_core")
    environment = os.getenv("APP_ENV", "production")

    # Identity Registry: Defines how this service appears in the infrastructure map.
    resource = Resource.create({
        SERVICE_NAME: resolved_name,
        "deployment.environment": environment,
        "service.namespace": "fly_ai",
    })

    # The TracerProvider is the source of all tracers.
    provider = TracerProvider(resource=resource)

    # OTLP / gRPC Exporter: Sends telemetry to the collector (Tempo).
    otlp_endpoint = os.getenv("OTLP_ENDPOINT", "http://tempo:4317")

    try:
        exporter = OTLPSpanExporter(
            endpoint=otlp_endpoint,
            insecure=True,  # Communication within the docker-compose network.
        )
        # Using a Batch processor to minimize the performance impact on hot paths.
        processor = BatchSpanProcessor(exporter)
        provider.add_span_processor(processor)
        logger.info(
            "OTel tracing configured: service=%s endpoint=%s env=%s",
            resolved_name,
            otlp_endpoint,
            environment,
        )
    except Exception as exc:
        # We fail gracefully here to prevent an observability outage from
        # taking down the actual business processing.
        logger.warning(
            "OTel exporter failed to initialize (traces will be dropped): %s",
            exc,
        )

    # Activate the provider globally so libraries can retrieve tracers.
    trace.set_tracer_provider(provider)

    # HTTP Auto-Instrumentation.
    if app is not None:
        # Exclude high-frequency, low-value routes like /metrics or /health
        # to reduce noise and lower ingestion costs (FinOps).
        excluded_urls_str = os.getenv("OTEL_EXCLUDED_URLS", "metrics,health")
        
        FastAPIInstrumentor.instrument_app(
            app,  # type: ignore[arg-type]
            excluded_urls=excluded_urls_str
        )
        logger.info(f"OTel: FastAPI auto-instrumented (ignoring: {excluded_urls_str})")

    # Database Auto-Instrumentation.
    if engine is not None:
        # Captures every SQL execution as a span, including raw queries.
        SQLAlchemyInstrumentor().instrument(engine=engine)  # type: ignore[arg-type]
        logger.info("OTel: SQLAlchemy auto-instrumented (database observability active)")
