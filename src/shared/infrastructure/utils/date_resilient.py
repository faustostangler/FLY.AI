import logging
from datetime import datetime
from typing import Optional, List
from shared.infrastructure.monitoring.metrics import metrics

logger = logging.getLogger(__name__)

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
        formats: Optional[List[str]] = None
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
        # Uses the property name defined in MetricsProvider
        metrics.date_parsing_failures.labels(field=field_name, source=source).inc()
        return None
