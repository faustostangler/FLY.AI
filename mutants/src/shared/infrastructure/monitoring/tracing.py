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
from typing import Annotated
from typing import Callable
from typing import ClassVar

MutantDict = Annotated[dict[str, Callable], "Mutant"] # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None): # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os # type: ignore
    mutant_under_test = os.environ['MUTANT_UNDER_TEST'] # type: ignore
    if mutant_under_test == 'fail': # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore
        raise MutmutProgrammaticFailException('Failed programmatically')       # type: ignore
    elif mutant_under_test == 'stats': # type: ignore
        from mutmut.__main__ import record_trampoline_hit # type: ignore
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore
    if not mutant_under_test.startswith(prefix): # type: ignore
        result = orig(*call_args, **call_kwargs) # type: ignore
        return result # type: ignore
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore
    if self_arg is not None: # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore
    return result # type: ignore


class OTelLogFilter(logging.Filter):
    """Enriches log records with OpenTelemetry context for correlation.

    Injected Trace IDs and Span IDs allow for seamless pivoting between 
    logs in Loki and traces in Tempo within Grafana. Without this correlation, 
    debugging distributed failures becomes a needle-in-a-haystack operation.

    Format placeholders available for log formatters: %(trace_id)s, %(span_id)s
    """

    def filter(self, record: logging.LogRecord) -> bool:
        args = [record]# type: ignore
        kwargs = {}# type: ignore
        return _mutmut_trampoline(object.__getattribute__(self, 'xǁOTelLogFilterǁfilter__mutmut_orig'), object.__getattribute__(self, 'xǁOTelLogFilterǁfilter__mutmut_mutants'), args, kwargs, self)

    def xǁOTelLogFilterǁfilter__mutmut_orig(self, record: logging.LogRecord) -> bool:
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

    def xǁOTelLogFilterǁfilter__mutmut_1(self, record: logging.LogRecord) -> bool:
        """Injects OTel metadata into every LogRecord passed through this filter.

        Standard logging doesn't know about the current execution context. 
        We extract it here to ensure every log line is traceable.

        Args:
            record (logging.LogRecord): The log record to be enriched.

        Returns:
            bool: Always True to allow the record to propagate.
        """
        span = None
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

    def xǁOTelLogFilterǁfilter__mutmut_2(self, record: logging.LogRecord) -> bool:
        """Injects OTel metadata into every LogRecord passed through this filter.

        Standard logging doesn't know about the current execution context. 
        We extract it here to ensure every log line is traceable.

        Args:
            record (logging.LogRecord): The log record to be enriched.

        Returns:
            bool: Always True to allow the record to propagate.
        """
        span = trace.get_current_span()
        ctx = None

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

    def xǁOTelLogFilterǁfilter__mutmut_3(self, record: logging.LogRecord) -> bool:
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
        if span.is_recording() or ctx.trace_id != 0:
            record.trace_id = format(ctx.trace_id, "032x")  # type: ignore[attr-defined]
            record.span_id = format(ctx.span_id, "016x")  # type: ignore[attr-defined]
        else:
            # Provide zeroed defaults to avoid KeyError in format strings 
            # when no trace context exists.
            record.trace_id = "0" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_4(self, record: logging.LogRecord) -> bool:
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
        if span.is_recording() and ctx.trace_id == 0:
            record.trace_id = format(ctx.trace_id, "032x")  # type: ignore[attr-defined]
            record.span_id = format(ctx.span_id, "016x")  # type: ignore[attr-defined]
        else:
            # Provide zeroed defaults to avoid KeyError in format strings 
            # when no trace context exists.
            record.trace_id = "0" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_5(self, record: logging.LogRecord) -> bool:
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
        if span.is_recording() and ctx.trace_id != 1:
            record.trace_id = format(ctx.trace_id, "032x")  # type: ignore[attr-defined]
            record.span_id = format(ctx.span_id, "016x")  # type: ignore[attr-defined]
        else:
            # Provide zeroed defaults to avoid KeyError in format strings 
            # when no trace context exists.
            record.trace_id = "0" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_6(self, record: logging.LogRecord) -> bool:
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
            record.trace_id = None  # type: ignore[attr-defined]
            record.span_id = format(ctx.span_id, "016x")  # type: ignore[attr-defined]
        else:
            # Provide zeroed defaults to avoid KeyError in format strings 
            # when no trace context exists.
            record.trace_id = "0" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_7(self, record: logging.LogRecord) -> bool:
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
            record.trace_id = format(None, "032x")  # type: ignore[attr-defined]
            record.span_id = format(ctx.span_id, "016x")  # type: ignore[attr-defined]
        else:
            # Provide zeroed defaults to avoid KeyError in format strings 
            # when no trace context exists.
            record.trace_id = "0" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_8(self, record: logging.LogRecord) -> bool:
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
            record.trace_id = format(ctx.trace_id, None)  # type: ignore[attr-defined]
            record.span_id = format(ctx.span_id, "016x")  # type: ignore[attr-defined]
        else:
            # Provide zeroed defaults to avoid KeyError in format strings 
            # when no trace context exists.
            record.trace_id = "0" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_9(self, record: logging.LogRecord) -> bool:
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
            record.trace_id = format("032x")  # type: ignore[attr-defined]
            record.span_id = format(ctx.span_id, "016x")  # type: ignore[attr-defined]
        else:
            # Provide zeroed defaults to avoid KeyError in format strings 
            # when no trace context exists.
            record.trace_id = "0" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_10(self, record: logging.LogRecord) -> bool:
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
            record.trace_id = format(ctx.trace_id, )  # type: ignore[attr-defined]
            record.span_id = format(ctx.span_id, "016x")  # type: ignore[attr-defined]
        else:
            # Provide zeroed defaults to avoid KeyError in format strings 
            # when no trace context exists.
            record.trace_id = "0" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_11(self, record: logging.LogRecord) -> bool:
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
            record.trace_id = format(ctx.trace_id, "XX032xXX")  # type: ignore[attr-defined]
            record.span_id = format(ctx.span_id, "016x")  # type: ignore[attr-defined]
        else:
            # Provide zeroed defaults to avoid KeyError in format strings 
            # when no trace context exists.
            record.trace_id = "0" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_12(self, record: logging.LogRecord) -> bool:
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
            record.trace_id = format(ctx.trace_id, "032X")  # type: ignore[attr-defined]
            record.span_id = format(ctx.span_id, "016x")  # type: ignore[attr-defined]
        else:
            # Provide zeroed defaults to avoid KeyError in format strings 
            # when no trace context exists.
            record.trace_id = "0" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_13(self, record: logging.LogRecord) -> bool:
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
            record.span_id = None  # type: ignore[attr-defined]
        else:
            # Provide zeroed defaults to avoid KeyError in format strings 
            # when no trace context exists.
            record.trace_id = "0" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_14(self, record: logging.LogRecord) -> bool:
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
            record.span_id = format(None, "016x")  # type: ignore[attr-defined]
        else:
            # Provide zeroed defaults to avoid KeyError in format strings 
            # when no trace context exists.
            record.trace_id = "0" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_15(self, record: logging.LogRecord) -> bool:
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
            record.span_id = format(ctx.span_id, None)  # type: ignore[attr-defined]
        else:
            # Provide zeroed defaults to avoid KeyError in format strings 
            # when no trace context exists.
            record.trace_id = "0" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_16(self, record: logging.LogRecord) -> bool:
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
            record.span_id = format("016x")  # type: ignore[attr-defined]
        else:
            # Provide zeroed defaults to avoid KeyError in format strings 
            # when no trace context exists.
            record.trace_id = "0" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_17(self, record: logging.LogRecord) -> bool:
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
            record.span_id = format(ctx.span_id, )  # type: ignore[attr-defined]
        else:
            # Provide zeroed defaults to avoid KeyError in format strings 
            # when no trace context exists.
            record.trace_id = "0" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_18(self, record: logging.LogRecord) -> bool:
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
            record.span_id = format(ctx.span_id, "XX016xXX")  # type: ignore[attr-defined]
        else:
            # Provide zeroed defaults to avoid KeyError in format strings 
            # when no trace context exists.
            record.trace_id = "0" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_19(self, record: logging.LogRecord) -> bool:
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
            record.span_id = format(ctx.span_id, "016X")  # type: ignore[attr-defined]
        else:
            # Provide zeroed defaults to avoid KeyError in format strings 
            # when no trace context exists.
            record.trace_id = "0" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_20(self, record: logging.LogRecord) -> bool:
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
            record.trace_id = None  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_21(self, record: logging.LogRecord) -> bool:
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
            record.trace_id = "0" / 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_22(self, record: logging.LogRecord) -> bool:
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
            record.trace_id = "XX0XX" * 32  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_23(self, record: logging.LogRecord) -> bool:
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
            record.trace_id = "0" * 33  # type: ignore[attr-defined]
            record.span_id = "0" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_24(self, record: logging.LogRecord) -> bool:
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
            record.span_id = None  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_25(self, record: logging.LogRecord) -> bool:
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
            record.span_id = "0" / 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_26(self, record: logging.LogRecord) -> bool:
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
            record.span_id = "XX0XX" * 16  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_27(self, record: logging.LogRecord) -> bool:
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
            record.span_id = "0" * 17  # type: ignore[attr-defined]

        return True

    def xǁOTelLogFilterǁfilter__mutmut_28(self, record: logging.LogRecord) -> bool:
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

        return False
    
    xǁOTelLogFilterǁfilter__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
    'xǁOTelLogFilterǁfilter__mutmut_1': xǁOTelLogFilterǁfilter__mutmut_1, 
        'xǁOTelLogFilterǁfilter__mutmut_2': xǁOTelLogFilterǁfilter__mutmut_2, 
        'xǁOTelLogFilterǁfilter__mutmut_3': xǁOTelLogFilterǁfilter__mutmut_3, 
        'xǁOTelLogFilterǁfilter__mutmut_4': xǁOTelLogFilterǁfilter__mutmut_4, 
        'xǁOTelLogFilterǁfilter__mutmut_5': xǁOTelLogFilterǁfilter__mutmut_5, 
        'xǁOTelLogFilterǁfilter__mutmut_6': xǁOTelLogFilterǁfilter__mutmut_6, 
        'xǁOTelLogFilterǁfilter__mutmut_7': xǁOTelLogFilterǁfilter__mutmut_7, 
        'xǁOTelLogFilterǁfilter__mutmut_8': xǁOTelLogFilterǁfilter__mutmut_8, 
        'xǁOTelLogFilterǁfilter__mutmut_9': xǁOTelLogFilterǁfilter__mutmut_9, 
        'xǁOTelLogFilterǁfilter__mutmut_10': xǁOTelLogFilterǁfilter__mutmut_10, 
        'xǁOTelLogFilterǁfilter__mutmut_11': xǁOTelLogFilterǁfilter__mutmut_11, 
        'xǁOTelLogFilterǁfilter__mutmut_12': xǁOTelLogFilterǁfilter__mutmut_12, 
        'xǁOTelLogFilterǁfilter__mutmut_13': xǁOTelLogFilterǁfilter__mutmut_13, 
        'xǁOTelLogFilterǁfilter__mutmut_14': xǁOTelLogFilterǁfilter__mutmut_14, 
        'xǁOTelLogFilterǁfilter__mutmut_15': xǁOTelLogFilterǁfilter__mutmut_15, 
        'xǁOTelLogFilterǁfilter__mutmut_16': xǁOTelLogFilterǁfilter__mutmut_16, 
        'xǁOTelLogFilterǁfilter__mutmut_17': xǁOTelLogFilterǁfilter__mutmut_17, 
        'xǁOTelLogFilterǁfilter__mutmut_18': xǁOTelLogFilterǁfilter__mutmut_18, 
        'xǁOTelLogFilterǁfilter__mutmut_19': xǁOTelLogFilterǁfilter__mutmut_19, 
        'xǁOTelLogFilterǁfilter__mutmut_20': xǁOTelLogFilterǁfilter__mutmut_20, 
        'xǁOTelLogFilterǁfilter__mutmut_21': xǁOTelLogFilterǁfilter__mutmut_21, 
        'xǁOTelLogFilterǁfilter__mutmut_22': xǁOTelLogFilterǁfilter__mutmut_22, 
        'xǁOTelLogFilterǁfilter__mutmut_23': xǁOTelLogFilterǁfilter__mutmut_23, 
        'xǁOTelLogFilterǁfilter__mutmut_24': xǁOTelLogFilterǁfilter__mutmut_24, 
        'xǁOTelLogFilterǁfilter__mutmut_25': xǁOTelLogFilterǁfilter__mutmut_25, 
        'xǁOTelLogFilterǁfilter__mutmut_26': xǁOTelLogFilterǁfilter__mutmut_26, 
        'xǁOTelLogFilterǁfilter__mutmut_27': xǁOTelLogFilterǁfilter__mutmut_27, 
        'xǁOTelLogFilterǁfilter__mutmut_28': xǁOTelLogFilterǁfilter__mutmut_28
    }
    xǁOTelLogFilterǁfilter__mutmut_orig.__name__ = 'xǁOTelLogFilterǁfilter'


def setup_tracing(
    app: Optional[object] = None,
    engine: Optional[object] = None,
    service_name: Optional[str] = None,
) -> None:
    args = [app, engine, service_name]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_setup_tracing__mutmut_orig, x_setup_tracing__mutmut_mutants, args, kwargs, None)


def x_setup_tracing__mutmut_orig(
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


def x_setup_tracing__mutmut_1(
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
    resolved_name = None
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


def x_setup_tracing__mutmut_2(
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
    resolved_name = service_name and os.getenv("OTEL_SERVICE_NAME", "fly_ai_core")
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


def x_setup_tracing__mutmut_3(
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
    resolved_name = service_name or os.getenv(None, "fly_ai_core")
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


def x_setup_tracing__mutmut_4(
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
    resolved_name = service_name or os.getenv("OTEL_SERVICE_NAME", None)
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


def x_setup_tracing__mutmut_5(
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
    resolved_name = service_name or os.getenv("fly_ai_core")
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


def x_setup_tracing__mutmut_6(
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
    resolved_name = service_name or os.getenv("OTEL_SERVICE_NAME", )
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


def x_setup_tracing__mutmut_7(
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
    resolved_name = service_name or os.getenv("XXOTEL_SERVICE_NAMEXX", "fly_ai_core")
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


def x_setup_tracing__mutmut_8(
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
    resolved_name = service_name or os.getenv("otel_service_name", "fly_ai_core")
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


def x_setup_tracing__mutmut_9(
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
    resolved_name = service_name or os.getenv("OTEL_SERVICE_NAME", "XXfly_ai_coreXX")
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


def x_setup_tracing__mutmut_10(
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
    resolved_name = service_name or os.getenv("OTEL_SERVICE_NAME", "FLY_AI_CORE")
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


def x_setup_tracing__mutmut_11(
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
    environment = None

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


def x_setup_tracing__mutmut_12(
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
    environment = os.getenv(None, "production")

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


def x_setup_tracing__mutmut_13(
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
    environment = os.getenv("APP_ENV", None)

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


def x_setup_tracing__mutmut_14(
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
    environment = os.getenv("production")

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


def x_setup_tracing__mutmut_15(
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
    environment = os.getenv("APP_ENV", )

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


def x_setup_tracing__mutmut_16(
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
    environment = os.getenv("XXAPP_ENVXX", "production")

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


def x_setup_tracing__mutmut_17(
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
    environment = os.getenv("app_env", "production")

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


def x_setup_tracing__mutmut_18(
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
    environment = os.getenv("APP_ENV", "XXproductionXX")

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


def x_setup_tracing__mutmut_19(
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
    environment = os.getenv("APP_ENV", "PRODUCTION")

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


def x_setup_tracing__mutmut_20(
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
    resource = None

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


def x_setup_tracing__mutmut_21(
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
    resource = Resource.create(None)

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


def x_setup_tracing__mutmut_22(
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
        "XXdeployment.environmentXX": environment,
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


def x_setup_tracing__mutmut_23(
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
        "DEPLOYMENT.ENVIRONMENT": environment,
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


def x_setup_tracing__mutmut_24(
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
        "XXservice.namespaceXX": "fly_ai",
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


def x_setup_tracing__mutmut_25(
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
        "SERVICE.NAMESPACE": "fly_ai",
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


def x_setup_tracing__mutmut_26(
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
        "service.namespace": "XXfly_aiXX",
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


def x_setup_tracing__mutmut_27(
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
        "service.namespace": "FLY_AI",
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


def x_setup_tracing__mutmut_28(
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
    provider = None

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


def x_setup_tracing__mutmut_29(
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
    provider = TracerProvider(resource=None)

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


def x_setup_tracing__mutmut_30(
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
    otlp_endpoint = None

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


def x_setup_tracing__mutmut_31(
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
    otlp_endpoint = os.getenv(None, "http://tempo:4317")

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


def x_setup_tracing__mutmut_32(
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
    otlp_endpoint = os.getenv("OTLP_ENDPOINT", None)

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


def x_setup_tracing__mutmut_33(
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
    otlp_endpoint = os.getenv("http://tempo:4317")

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


def x_setup_tracing__mutmut_34(
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
    otlp_endpoint = os.getenv("OTLP_ENDPOINT", )

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


def x_setup_tracing__mutmut_35(
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
    otlp_endpoint = os.getenv("XXOTLP_ENDPOINTXX", "http://tempo:4317")

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


def x_setup_tracing__mutmut_36(
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
    otlp_endpoint = os.getenv("otlp_endpoint", "http://tempo:4317")

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


def x_setup_tracing__mutmut_37(
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
    otlp_endpoint = os.getenv("OTLP_ENDPOINT", "XXhttp://tempo:4317XX")

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


def x_setup_tracing__mutmut_38(
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
    otlp_endpoint = os.getenv("OTLP_ENDPOINT", "HTTP://TEMPO:4317")

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


def x_setup_tracing__mutmut_39(
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
        exporter = None
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


def x_setup_tracing__mutmut_40(
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
            endpoint=None,
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


def x_setup_tracing__mutmut_41(
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
            insecure=None,  # Communication within the docker-compose network.
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


def x_setup_tracing__mutmut_42(
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


def x_setup_tracing__mutmut_43(
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


def x_setup_tracing__mutmut_44(
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
            insecure=False,  # Communication within the docker-compose network.
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


def x_setup_tracing__mutmut_45(
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
        processor = None
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


def x_setup_tracing__mutmut_46(
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
        processor = BatchSpanProcessor(None)
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


def x_setup_tracing__mutmut_47(
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
        provider.add_span_processor(None)
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


def x_setup_tracing__mutmut_48(
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
            None,
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


def x_setup_tracing__mutmut_49(
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
            None,
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


def x_setup_tracing__mutmut_50(
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
            None,
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


def x_setup_tracing__mutmut_51(
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
            None,
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


def x_setup_tracing__mutmut_52(
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


def x_setup_tracing__mutmut_53(
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


def x_setup_tracing__mutmut_54(
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


def x_setup_tracing__mutmut_55(
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


def x_setup_tracing__mutmut_56(
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
            "XXOTel tracing configured: service=%s endpoint=%s env=%sXX",
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


def x_setup_tracing__mutmut_57(
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
            "otel tracing configured: service=%s endpoint=%s env=%s",
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


def x_setup_tracing__mutmut_58(
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
            "OTEL TRACING CONFIGURED: SERVICE=%S ENDPOINT=%S ENV=%S",
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


def x_setup_tracing__mutmut_59(
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
            None,
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


def x_setup_tracing__mutmut_60(
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
            None,
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


def x_setup_tracing__mutmut_61(
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


def x_setup_tracing__mutmut_62(
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


def x_setup_tracing__mutmut_63(
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
            "XXOTel exporter failed to initialize (traces will be dropped): %sXX",
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


def x_setup_tracing__mutmut_64(
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
            "otel exporter failed to initialize (traces will be dropped): %s",
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


def x_setup_tracing__mutmut_65(
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
            "OTEL EXPORTER FAILED TO INITIALIZE (TRACES WILL BE DROPPED): %S",
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


def x_setup_tracing__mutmut_66(
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
    trace.set_tracer_provider(None)

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


def x_setup_tracing__mutmut_67(
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
    if app is None:
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


def x_setup_tracing__mutmut_68(
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
        excluded_urls_str = None
        
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


def x_setup_tracing__mutmut_69(
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
        excluded_urls_str = os.getenv(None, "metrics,health")
        
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


def x_setup_tracing__mutmut_70(
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
        excluded_urls_str = os.getenv("OTEL_EXCLUDED_URLS", None)
        
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


def x_setup_tracing__mutmut_71(
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
        excluded_urls_str = os.getenv("metrics,health")
        
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


def x_setup_tracing__mutmut_72(
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
        excluded_urls_str = os.getenv("OTEL_EXCLUDED_URLS", )
        
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


def x_setup_tracing__mutmut_73(
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
        excluded_urls_str = os.getenv("XXOTEL_EXCLUDED_URLSXX", "metrics,health")
        
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


def x_setup_tracing__mutmut_74(
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
        excluded_urls_str = os.getenv("otel_excluded_urls", "metrics,health")
        
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


def x_setup_tracing__mutmut_75(
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
        excluded_urls_str = os.getenv("OTEL_EXCLUDED_URLS", "XXmetrics,healthXX")
        
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


def x_setup_tracing__mutmut_76(
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
        excluded_urls_str = os.getenv("OTEL_EXCLUDED_URLS", "METRICS,HEALTH")
        
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


def x_setup_tracing__mutmut_77(
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
            None,  # type: ignore[arg-type]
            excluded_urls=excluded_urls_str
        )
        logger.info(f"OTel: FastAPI auto-instrumented (ignoring: {excluded_urls_str})")

    # Database Auto-Instrumentation.
    if engine is not None:
        # Captures every SQL execution as a span, including raw queries.
        SQLAlchemyInstrumentor().instrument(engine=engine)  # type: ignore[arg-type]
        logger.info("OTel: SQLAlchemy auto-instrumented (database observability active)")


def x_setup_tracing__mutmut_78(
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
            excluded_urls=None
        )
        logger.info(f"OTel: FastAPI auto-instrumented (ignoring: {excluded_urls_str})")

    # Database Auto-Instrumentation.
    if engine is not None:
        # Captures every SQL execution as a span, including raw queries.
        SQLAlchemyInstrumentor().instrument(engine=engine)  # type: ignore[arg-type]
        logger.info("OTel: SQLAlchemy auto-instrumented (database observability active)")


def x_setup_tracing__mutmut_79(
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
            excluded_urls=excluded_urls_str
        )
        logger.info(f"OTel: FastAPI auto-instrumented (ignoring: {excluded_urls_str})")

    # Database Auto-Instrumentation.
    if engine is not None:
        # Captures every SQL execution as a span, including raw queries.
        SQLAlchemyInstrumentor().instrument(engine=engine)  # type: ignore[arg-type]
        logger.info("OTel: SQLAlchemy auto-instrumented (database observability active)")


def x_setup_tracing__mutmut_80(
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
            )
        logger.info(f"OTel: FastAPI auto-instrumented (ignoring: {excluded_urls_str})")

    # Database Auto-Instrumentation.
    if engine is not None:
        # Captures every SQL execution as a span, including raw queries.
        SQLAlchemyInstrumentor().instrument(engine=engine)  # type: ignore[arg-type]
        logger.info("OTel: SQLAlchemy auto-instrumented (database observability active)")


def x_setup_tracing__mutmut_81(
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
        logger.info(None)

    # Database Auto-Instrumentation.
    if engine is not None:
        # Captures every SQL execution as a span, including raw queries.
        SQLAlchemyInstrumentor().instrument(engine=engine)  # type: ignore[arg-type]
        logger.info("OTel: SQLAlchemy auto-instrumented (database observability active)")


def x_setup_tracing__mutmut_82(
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
    if engine is None:
        # Captures every SQL execution as a span, including raw queries.
        SQLAlchemyInstrumentor().instrument(engine=engine)  # type: ignore[arg-type]
        logger.info("OTel: SQLAlchemy auto-instrumented (database observability active)")


def x_setup_tracing__mutmut_83(
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
        SQLAlchemyInstrumentor().instrument(engine=None)  # type: ignore[arg-type]
        logger.info("OTel: SQLAlchemy auto-instrumented (database observability active)")


def x_setup_tracing__mutmut_84(
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
        logger.info(None)


def x_setup_tracing__mutmut_85(
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
        logger.info("XXOTel: SQLAlchemy auto-instrumented (database observability active)XX")


def x_setup_tracing__mutmut_86(
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
        logger.info("otel: sqlalchemy auto-instrumented (database observability active)")


def x_setup_tracing__mutmut_87(
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
        logger.info("OTEL: SQLALCHEMY AUTO-INSTRUMENTED (DATABASE OBSERVABILITY ACTIVE)")

x_setup_tracing__mutmut_mutants : ClassVar[MutantDict] = { # type: ignore
'x_setup_tracing__mutmut_1': x_setup_tracing__mutmut_1, 
    'x_setup_tracing__mutmut_2': x_setup_tracing__mutmut_2, 
    'x_setup_tracing__mutmut_3': x_setup_tracing__mutmut_3, 
    'x_setup_tracing__mutmut_4': x_setup_tracing__mutmut_4, 
    'x_setup_tracing__mutmut_5': x_setup_tracing__mutmut_5, 
    'x_setup_tracing__mutmut_6': x_setup_tracing__mutmut_6, 
    'x_setup_tracing__mutmut_7': x_setup_tracing__mutmut_7, 
    'x_setup_tracing__mutmut_8': x_setup_tracing__mutmut_8, 
    'x_setup_tracing__mutmut_9': x_setup_tracing__mutmut_9, 
    'x_setup_tracing__mutmut_10': x_setup_tracing__mutmut_10, 
    'x_setup_tracing__mutmut_11': x_setup_tracing__mutmut_11, 
    'x_setup_tracing__mutmut_12': x_setup_tracing__mutmut_12, 
    'x_setup_tracing__mutmut_13': x_setup_tracing__mutmut_13, 
    'x_setup_tracing__mutmut_14': x_setup_tracing__mutmut_14, 
    'x_setup_tracing__mutmut_15': x_setup_tracing__mutmut_15, 
    'x_setup_tracing__mutmut_16': x_setup_tracing__mutmut_16, 
    'x_setup_tracing__mutmut_17': x_setup_tracing__mutmut_17, 
    'x_setup_tracing__mutmut_18': x_setup_tracing__mutmut_18, 
    'x_setup_tracing__mutmut_19': x_setup_tracing__mutmut_19, 
    'x_setup_tracing__mutmut_20': x_setup_tracing__mutmut_20, 
    'x_setup_tracing__mutmut_21': x_setup_tracing__mutmut_21, 
    'x_setup_tracing__mutmut_22': x_setup_tracing__mutmut_22, 
    'x_setup_tracing__mutmut_23': x_setup_tracing__mutmut_23, 
    'x_setup_tracing__mutmut_24': x_setup_tracing__mutmut_24, 
    'x_setup_tracing__mutmut_25': x_setup_tracing__mutmut_25, 
    'x_setup_tracing__mutmut_26': x_setup_tracing__mutmut_26, 
    'x_setup_tracing__mutmut_27': x_setup_tracing__mutmut_27, 
    'x_setup_tracing__mutmut_28': x_setup_tracing__mutmut_28, 
    'x_setup_tracing__mutmut_29': x_setup_tracing__mutmut_29, 
    'x_setup_tracing__mutmut_30': x_setup_tracing__mutmut_30, 
    'x_setup_tracing__mutmut_31': x_setup_tracing__mutmut_31, 
    'x_setup_tracing__mutmut_32': x_setup_tracing__mutmut_32, 
    'x_setup_tracing__mutmut_33': x_setup_tracing__mutmut_33, 
    'x_setup_tracing__mutmut_34': x_setup_tracing__mutmut_34, 
    'x_setup_tracing__mutmut_35': x_setup_tracing__mutmut_35, 
    'x_setup_tracing__mutmut_36': x_setup_tracing__mutmut_36, 
    'x_setup_tracing__mutmut_37': x_setup_tracing__mutmut_37, 
    'x_setup_tracing__mutmut_38': x_setup_tracing__mutmut_38, 
    'x_setup_tracing__mutmut_39': x_setup_tracing__mutmut_39, 
    'x_setup_tracing__mutmut_40': x_setup_tracing__mutmut_40, 
    'x_setup_tracing__mutmut_41': x_setup_tracing__mutmut_41, 
    'x_setup_tracing__mutmut_42': x_setup_tracing__mutmut_42, 
    'x_setup_tracing__mutmut_43': x_setup_tracing__mutmut_43, 
    'x_setup_tracing__mutmut_44': x_setup_tracing__mutmut_44, 
    'x_setup_tracing__mutmut_45': x_setup_tracing__mutmut_45, 
    'x_setup_tracing__mutmut_46': x_setup_tracing__mutmut_46, 
    'x_setup_tracing__mutmut_47': x_setup_tracing__mutmut_47, 
    'x_setup_tracing__mutmut_48': x_setup_tracing__mutmut_48, 
    'x_setup_tracing__mutmut_49': x_setup_tracing__mutmut_49, 
    'x_setup_tracing__mutmut_50': x_setup_tracing__mutmut_50, 
    'x_setup_tracing__mutmut_51': x_setup_tracing__mutmut_51, 
    'x_setup_tracing__mutmut_52': x_setup_tracing__mutmut_52, 
    'x_setup_tracing__mutmut_53': x_setup_tracing__mutmut_53, 
    'x_setup_tracing__mutmut_54': x_setup_tracing__mutmut_54, 
    'x_setup_tracing__mutmut_55': x_setup_tracing__mutmut_55, 
    'x_setup_tracing__mutmut_56': x_setup_tracing__mutmut_56, 
    'x_setup_tracing__mutmut_57': x_setup_tracing__mutmut_57, 
    'x_setup_tracing__mutmut_58': x_setup_tracing__mutmut_58, 
    'x_setup_tracing__mutmut_59': x_setup_tracing__mutmut_59, 
    'x_setup_tracing__mutmut_60': x_setup_tracing__mutmut_60, 
    'x_setup_tracing__mutmut_61': x_setup_tracing__mutmut_61, 
    'x_setup_tracing__mutmut_62': x_setup_tracing__mutmut_62, 
    'x_setup_tracing__mutmut_63': x_setup_tracing__mutmut_63, 
    'x_setup_tracing__mutmut_64': x_setup_tracing__mutmut_64, 
    'x_setup_tracing__mutmut_65': x_setup_tracing__mutmut_65, 
    'x_setup_tracing__mutmut_66': x_setup_tracing__mutmut_66, 
    'x_setup_tracing__mutmut_67': x_setup_tracing__mutmut_67, 
    'x_setup_tracing__mutmut_68': x_setup_tracing__mutmut_68, 
    'x_setup_tracing__mutmut_69': x_setup_tracing__mutmut_69, 
    'x_setup_tracing__mutmut_70': x_setup_tracing__mutmut_70, 
    'x_setup_tracing__mutmut_71': x_setup_tracing__mutmut_71, 
    'x_setup_tracing__mutmut_72': x_setup_tracing__mutmut_72, 
    'x_setup_tracing__mutmut_73': x_setup_tracing__mutmut_73, 
    'x_setup_tracing__mutmut_74': x_setup_tracing__mutmut_74, 
    'x_setup_tracing__mutmut_75': x_setup_tracing__mutmut_75, 
    'x_setup_tracing__mutmut_76': x_setup_tracing__mutmut_76, 
    'x_setup_tracing__mutmut_77': x_setup_tracing__mutmut_77, 
    'x_setup_tracing__mutmut_78': x_setup_tracing__mutmut_78, 
    'x_setup_tracing__mutmut_79': x_setup_tracing__mutmut_79, 
    'x_setup_tracing__mutmut_80': x_setup_tracing__mutmut_80, 
    'x_setup_tracing__mutmut_81': x_setup_tracing__mutmut_81, 
    'x_setup_tracing__mutmut_82': x_setup_tracing__mutmut_82, 
    'x_setup_tracing__mutmut_83': x_setup_tracing__mutmut_83, 
    'x_setup_tracing__mutmut_84': x_setup_tracing__mutmut_84, 
    'x_setup_tracing__mutmut_85': x_setup_tracing__mutmut_85, 
    'x_setup_tracing__mutmut_86': x_setup_tracing__mutmut_86, 
    'x_setup_tracing__mutmut_87': x_setup_tracing__mutmut_87
}
x_setup_tracing__mutmut_orig.__name__ = 'x_setup_tracing'
