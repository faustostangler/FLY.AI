import logging
import sys
from typing import Any, Dict

import structlog
from opentelemetry import trace


def inject_opentelemetry_context(
    logger: logging.Logger, log_method: str, event_dict: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Processor to inject OpenTelemetry trace_id and span_id into log payload.
    
    This ensures that every structured log can be perfectly correlated with
    distributed traces in Grafana Tempo, without requiring developers to
    manually pass these IDs down the call stack.

    Args:
        logger: The logger instance.
        log_method: The name of the log method (info, error, etc).
        event_dict: The current log payload.

    Returns:
        The mutated log payload with telemetry IDs, if available.
    """
    span = trace.get_current_span()
    if span.is_recording():
        span_context = span.get_span_context()
        # Loki and Tempo expect standard 32-character and 16-character hex strings
        event_dict["trace_id"] = format(span_context.trace_id, "032x")
        event_dict["span_id"] = format(span_context.span_id, "016x")
    
    return event_dict


def setup_structlog(log_level: str = "INFO", is_local_dev: bool = False) -> None:
    """
    Bootstraps the global logging configuration using structlog.

    Replaces standard logging formatters with a JSON-based pipeline for production,
    or a human-readable colored pipeline for local development. Strictly adheres
    to 12-Factor App principles by emitting logs only to stdout.

    Args:
        log_level (str): The base logging level (e.g., "INFO", "DEBUG").
        is_local_dev (bool): If True, uses human-readable console output instead of JSON.
    """
    # 1. Define the shared processors for both structlog and standard logging
    shared_processors = [
        structlog.contextvars.merge_contextvars,  # Injects variables bound via middleware
        structlog.stdlib.add_log_level,           # Injects 'level' (info, error)
        structlog.stdlib.add_logger_name,         # Injects 'logger' (e.g., companies.api)
        inject_opentelemetry_context,             # OTel Trace/Span correlation
        structlog.processors.TimeStamper(fmt="iso", utc=True), # ISO8601 for Loki ordering
        structlog.processors.StackInfoRenderer(), # Extracts stack traces safely
        structlog.processors.format_exc_info,     # Formats exception info into 'exception' key
        structlog.processors.UnicodeDecoder(),    # Ensures safe string encoding
    ]

    # 2. Configure standard library logging to route through structlog
    # This captures logs from Uvicorn, FastAPI, and SQLAlchemy
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout, # 12-Factor: stdout only, no FileHandlers
        level=getattr(logging, log_level.upper(), logging.INFO),
    )

    # 3. Determine the final formatter based on the environment
    if is_local_dev:
        # Developer Experience (DX): Colored, readable logs for the IDE
        renderer = structlog.dev.ConsoleRenderer()
    else:
        # SRE/Production: Pure JSON for FluentBit/Promtail to ship to Grafana Loki
        renderer = structlog.processors.JSONRenderer()

    # 4. Apply configuration to structlog
    structlog.configure(
        processors=shared_processors + [
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ],
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    # 5. Apply the structlog formatter to the root logger
    formatter = structlog.stdlib.ProcessorFormatter(
        foreign_pre_chain=shared_processors,
        processors=[
            structlog.stdlib.ProcessorFormatter.remove_processors_meta,
            renderer,
        ],
    )

    root_logger = logging.getLogger()
    for handler in root_logger.handlers:
        handler.setFormatter(formatter)
