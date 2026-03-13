import pytest
from datetime import datetime
from unittest.mock import MagicMock
from shared.infrastructure.utils.date_resilient import DateResilientParser

def test_date_resilient_parser_success():
    assert DateResilientParser.parse("2024-03-12", "test_field") == datetime(2024, 3, 12)
    assert DateResilientParser.parse("12/03/2024", "test_field") == datetime(2024, 3, 12)

def test_date_resilient_parser_handles_none():
    assert DateResilientParser.parse(None, "test_field") is None
    assert DateResilientParser.parse("null", "test_field") is None
    assert DateResilientParser.parse("", "test_field") is None

def test_date_resilient_parser_failure_returns_none():
    # We don't want to crash on bad dates, just return None and log
    assert DateResilientParser.parse("not-a-date", "test_field") is None

def test_date_resilient_parser_with_iso_format():
    assert DateResilientParser.parse("2024-03-12T15:30:45", "test_field") == datetime(2024, 3, 12, 15, 30, 45)
