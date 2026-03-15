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

    def test_parse_fallback_telemetry_metrics(self):
        """When telemetry is None, it should import and use the global Prometheus metric."""
        from unittest.mock import patch
        with patch("shared.infrastructure.monitoring.metrics.DATE_PARSING_FAILURES") as mock_metric:
            mock_labels = MagicMock()
            mock_metric.labels.return_value = mock_labels
            
            result = DateResilientParser.parse("invalid-date", "fallback_field")
            
            assert result is None
            mock_metric.labels.assert_called_once_with(field="fallback_field", source="B3")
            mock_labels.inc.assert_called_once()

    def test_mutmut_trampoline_fail(self):
        """Simulate mutmut fail programmatic exception to cover trampoline method lines."""
        from shared.infrastructure.utils.date_resilient import _mutmut_trampoline
        import os
        from unittest.mock import patch

        def mock_orig(): pass

        with patch.dict(os.environ, {"MUTANT_UNDER_TEST": "fail"}):
            with pytest.raises(Exception): # Catches MutmutProgrammaticFailException dynamically imported
                _mutmut_trampoline(mock_orig, {}, [], {})

    def test_mutmut_trampoline_stats(self):
        """Simulate mutmut stats telemetry logic to cover trampoline method lines."""
        from shared.infrastructure.utils.date_resilient import _mutmut_trampoline
        import os
        import sys
        from unittest.mock import patch, MagicMock
        
        mock_orig = MagicMock(return_value="Success")
        mock_orig.__module__ = "test"
        mock_orig.__name__ = "mock_orig"

        with patch.dict(os.environ, {"MUTANT_UNDER_TEST": "stats"}):
            mock_main_module = MagicMock()
            mock_record = MagicMock()
            mock_main_module.record_trampoline_hit = mock_record
            
            with patch.dict(sys.modules, {"mutmut": MagicMock(), "mutmut.__main__": mock_main_module}):
                result = _mutmut_trampoline(mock_orig, {}, [], {})
                assert result == "Success"
                mock_record.assert_called_once_with("test.mock_orig")

    def test_mutmut_trampoline_not_matching_prefix(self):
        """Cover lines for standard non-mutant pass-throughs."""
        from shared.infrastructure.utils.date_resilient import _mutmut_trampoline
        import os
        from unittest.mock import patch, MagicMock
        
        mock_orig = MagicMock(return_value="Original")
        mock_orig.__module__ = "test"
        mock_orig.__name__ = "mock_orig"

        with patch.dict(os.environ, {"MUTANT_UNDER_TEST": "other_module.mutant"}):
            result = _mutmut_trampoline(mock_orig, {}, [], {})
            assert result == "Original"

    def test_mutmut_trampoline_matching_prefix_bound(self):
        """Cover lines for bound method mutations."""
        from shared.infrastructure.utils.date_resilient import _mutmut_trampoline
        import os
        from unittest.mock import patch, MagicMock
        
        mock_orig = MagicMock()
        mock_orig.__module__ = "test"
        mock_orig.__name__ = "mock_orig"
        
        mock_mutant = MagicMock(return_value="Mutated")
        mutant_name = "test.mock_orig__mutmut_1".rpartition('.')[-1]
        mutants = {mutant_name: mock_mutant}

        with patch.dict(os.environ, {"MUTANT_UNDER_TEST": "test.mock_orig__mutmut_1"}):
            result = _mutmut_trampoline(mock_orig, mutants, [], {}, self_arg="Self")
            assert result == "Mutated"
            mock_mutant.assert_called_with("Self")

    def test_mutmut_trampoline_matching_prefix_unbound(self):
        """Cover line for unbound method mutations."""
        from shared.infrastructure.utils.date_resilient import _mutmut_trampoline
        import os
        from unittest.mock import patch, MagicMock
        
        mock_orig = MagicMock()
        mock_orig.__module__ = "test"
        mock_orig.__name__ = "mock_orig"
        
        mock_mutant = MagicMock(return_value="Mutated")
        mutant_name = "test.mock_orig__mutmut_1".rpartition('.')[-1]
        mutants = {mutant_name: mock_mutant} 

        with patch.dict(os.environ, {"MUTANT_UNDER_TEST": "test.mock_orig__mutmut_1"}):
            result = _mutmut_trampoline(mock_orig, mutants, [], {})
            assert result == "Mutated"
            mock_mutant.assert_called_with()
