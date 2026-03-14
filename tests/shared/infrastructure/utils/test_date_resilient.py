"""Tests for the DateResilientParser infrastructure utility.

Verifies the resilient date parsing strategy including multi-format
attempts, telemetry reporting on failures, and null/empty handling.
"""

import pytest
from datetime import datetime
from unittest.mock import MagicMock

from shared.infrastructure.utils.date_resilient import DateResilientParser


class TestDateResilientParser:
    """Unit tests for the DateResilientParser parsing strategy."""

    def test_parse_iso_format(self):
        """Standard ISO 8601 format must parse correctly."""
        result = DateResilientParser.parse("2024-03-12", "test_field")
        assert result == datetime(2024, 3, 12)

    def test_parse_brazilian_format(self):
        """Brazilian dd/mm/yyyy format must parse correctly."""
        result = DateResilientParser.parse("12/03/2024", "test_field")
        assert result == datetime(2024, 3, 12)

    def test_parse_brazilian_format_with_time(self):
        """Brazilian dd/mm/yyyy HH:MM:SS format must parse correctly."""
        result = DateResilientParser.parse("12/03/2024 14:30:00", "test_field")
        assert result == datetime(2024, 3, 12, 14, 30, 0)

    def test_parse_datetime_with_time(self):
        """Datetime with time component must parse correctly."""
        result = DateResilientParser.parse("2024-03-12T14:30:00", "test_field")
        assert result == datetime(2024, 3, 12, 14, 30, 0)

    def test_parse_iso_with_space_separator(self):
        """ISO format with space instead of T must parse correctly."""
        result = DateResilientParser.parse("2024-03-12 14:30:00", "test_field")
        assert result == datetime(2024, 3, 12, 14, 30, 0)

    def test_parse_datetime_with_microseconds(self):
        """Datetime with microseconds must parse correctly."""
        result = DateResilientParser.parse("2024-03-12T14:30:00.123456", "test_field")
        assert result == datetime(2024, 3, 12, 14, 30, 0, 123456)

    def test_parse_none_returns_none(self):
        """None input must return None without raising."""
        assert DateResilientParser.parse(None, "test_field") is None

    def test_parse_empty_string_returns_none(self):
        """Empty string must return None without raising."""
        assert DateResilientParser.parse("", "test_field") is None

    def test_parse_null_string_returns_none(self):
        """The literal string 'null' must return None."""
        assert DateResilientParser.parse("null", "test_field") is None

    def test_parse_whitespace_returns_none(self):
        """Whitespace-only strings must return None."""
        assert DateResilientParser.parse("   ", "test_field") is None

    def test_parse_invalid_format_returns_none(self):
        """Unparseable dates must return None."""
        assert DateResilientParser.parse("not-a-date", "test_field") is None

    def test_parse_invalid_format_increments_telemetry(self):
        """Unparseable dates must trigger telemetry port notification."""
        mock_telemetry = MagicMock()
        result = DateResilientParser.parse(
            "not-a-date", "test_field", source="TestSource", telemetry=mock_telemetry
        )
        assert result is None
        mock_telemetry.increment_date_parsing_failures.assert_called_once_with(
            field="test_field", source="TestSource"
        )

    def test_parse_default_source_is_b3(self):
        """Default source for telemetry should be 'B3'."""
        mock_telemetry = MagicMock()
        DateResilientParser.parse(
            "garbage", "test_field", telemetry=mock_telemetry
        )
        mock_telemetry.increment_date_parsing_failures.assert_called_once_with(
            field="test_field", source="B3"
        )

    def test_parse_strips_whitespace(self):
        """Leading/trailing whitespace should not break parsing."""
        result = DateResilientParser.parse("  2024-03-12  ", "test_field")
        assert result == datetime(2024, 3, 12)

    def test_parse_with_custom_formats(self):
        """Custom format list should override default formats."""
        result = DateResilientParser.parse(
            "12-Mar-2024", "test_field",
            formats=["%d-%b-%Y"]
        )
        assert result == datetime(2024, 3, 12)

    def test_parse_custom_format_failure_returns_none(self):
        """When custom formats all fail, must still return None."""
        mock_telemetry = MagicMock()
        result = DateResilientParser.parse(
            "2024-03-12", "test_field",
            formats=["%d-%b-%Y"],
            telemetry=mock_telemetry,
        )
        assert result is None
        mock_telemetry.increment_date_parsing_failures.assert_called_once()
