import logging
from datetime import datetime
from typing import Optional, List
from shared.domain.ports.telemetry_port import TelemetryPort

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

class DateResilientParser:
    """
    SOTA Resilient Date Parser.
    Attempts to parse dates using multiple formats and reports failures to telemetry.
    """
    
    DEFAULT_FORMATS = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%d/%m/%Y %H:%M:%S",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%S.%f",
        "%Y-%m-%d %H:%M:%S",
    ]

    @staticmethod
    def parse(
        date_str: Optional[str], 
        field_name: str, 
        source: str = "B3",
        formats: Optional[List[str]] = None,
        telemetry: Optional[TelemetryPort] = None
    ) -> Optional[datetime]:
        """
        Parses a date string and returns a datetime object.
        Increments prometheus counter on failure.
        """
        if not date_str or str(date_str).lower() == "null" or not str(date_str).strip():
            return None
            
        date_str = str(date_str).strip()
        search_formats = formats or DateResilientParser.DEFAULT_FORMATS
        
        for fmt in search_formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        
        # If we reach here, parsing failed
        logger.warning(f"Failed to parse date '{date_str}' for field '{field_name}' from source '{source}'")
        if telemetry:
            telemetry.increment_date_parsing_failures(field=field_name, source=source)
        else:
            from shared.infrastructure.monitoring.metrics import DATE_PARSING_FAILURES
            DATE_PARSING_FAILURES.labels(field=field_name, source=source).inc()
        return None
