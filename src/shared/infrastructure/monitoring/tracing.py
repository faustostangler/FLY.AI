"""
OpenTelemetry Tracing Setup — Hexagonal Infrastructure Layer.

This module belongs to the Infrastructure layer (Ports & Adapters).
The Domain remains pure and framework-independent.

Responsibilities:
    1. Configure TracerProvider with OTLP exporter → Grafana Tempo.
    2. Auto-instrument FastAPI (HTTP spans) and SQLAlchemy (DB spans).
    3. Inject trace_id/span_id into Python logs for Loki correlation.

Usage:
    from shared.infrastructure.monitoring.tracing import setup_tracing
    setup_tracing(app=fastapi_app)
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


# =========================================================================
# 1. OTel Log Filter — Injects trace_id & span_id into every log record
# =========================================================================

class OTelLogFilter(logging.Filter):
    """
    Logging filter that enriches log records with OpenTelemetry context.

    When there is an active span, the trace_id and span_id are injected
    into the log record. This enables the Loki → Tempo correlation:
    clicking a trace_id in Grafana Explore opens the full distributed trace.

    Format placeholders: %(trace_id)s, %(span_id)s
    """

    def filter(self, record: logging.LogRecord) -> bool:
        span = trace.get_current_span()
        ctx = span.get_span_context()

        if span.is_recording() and ctx.trace_id != 0:
            record.trace_id = format(ctx.trace_id, "032x")  # type: ignore[attr-defined]
            record.span_id = format(ctx.span_id, "016x")  # type: ignore[attr-defined]
        else:
            record.trace_id = "0" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True


# =========================================================================
# 2. Tracing Setup — Pure Infrastructure Wiring
# =========================================================================

def setup_tracing(
    app: Optional[object] = None,
    engine: Optional[object] = None,
    service_name: Optional[str] = None,
) -> None:
    """
    Bootstrap OpenTelemetry distributed tracing.

    Args:
        app: FastAPI application instance (for HTTP auto-instrumentation).
        engine: SQLAlchemy engine instance (for DB auto-instrumentation).
        service_name: Override for the OTel service.name resource attribute.
                      Defaults to OTEL_SERVICE_NAME env var or 'fly_ai_core'.

    Architecture Note:
        This function is called ONCE at application startup (lifespan).
        It configures the global TracerProvider and instruments adapters.
        The Domain layer has ZERO knowledge of tracing.
    """
    resolved_name = service_name or os.getenv("OTEL_SERVICE_NAME", "fly_ai_core")
    environment = os.getenv("APP_ENV", "production")

    # --- Resource: Identity of this service in the trace ecosystem ---
    resource = Resource.create({
        SERVICE_NAME: resolved_name,
        "deployment.environment": environment,
        "service.namespace": "fly_ai",
    })

    # --- TracerProvider: Central orchestrator ---
    provider = TracerProvider(resource=resource)

    # --- OTLP Exporter → Grafana Tempo (gRPC, insecure for docker-compose) ---
    otlp_endpoint = os.getenv("OTLP_ENDPOINT", "http://tempo:4317")

    try:
        exporter = OTLPSpanExporter(
            endpoint=otlp_endpoint,
            insecure=True,
        )
        processor = BatchSpanProcessor(exporter)
        provider.add_span_processor(processor)
        logger.info(
            "OTel tracing configured: service=%s endpoint=%s env=%s",
            resolved_name,
            otlp_endpoint,
            environment,
        )
    except Exception as exc:
        logger.warning(
            "OTel exporter failed to initialize (traces will be dropped): %s",
            exc,
        )

    # --- Set global provider ---
    trace.set_tracer_provider(provider)

    # --- Auto-Instrumentation: FastAPI (HTTP layer) ---
    if app is not None:
        # SOTA: FinOps & Noise Reduction
        # Lê as rotas ignoradas do ambiente (ex: metrics,health)
        excluded_urls_str = os.getenv("OTEL_EXCLUDED_URLS", "metrics,health")
        
        FastAPIInstrumentor.instrument_app(
            app,  # type: ignore[arg-type]
            excluded_urls=excluded_urls_str
        )
        logger.info(f"OTel: FastAPI auto-instrumented (ignoring routes: {excluded_urls_str})")

    # --- Auto-Instrumentation: SQLAlchemy (Database layer) ---
    if engine is not None:
        SQLAlchemyInstrumentor().instrument(engine=engine)  # type: ignore[arg-type]
        logger.info("OTel: SQLAlchemy auto-instrumented (spans per query)")
