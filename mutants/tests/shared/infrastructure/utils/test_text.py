"""Tests for the TextCleaner shared infrastructure utility.

Verifies text normalization rules critical for maintaining
Domain integrity across all Bounded Contexts. These rules
directly affect the Anti-Corruption Layer (ACL) behavior.
"""

import pytest
from shared.infrastructure.utils.text import TextCleaner


class TestTextCleaner:
    """Unit tests for FLY.AI's TextCleaner normalization pipeline."""

    def test_clean_removes_accents(self):
        """Accented characters must be transliterated to ASCII (unidecode)."""
        assert TextCleaner.clean("Petróleo") == "PETROLEO"

    def test_clean_removes_punctuation(self):
        """Punctuation must be stripped from the output."""
        result = TextCleaner.clean("PETROLEO BRASILEIRO S.A. PETROBRAS")
        assert "." not in result
        assert result == "PETROLEO BRASILEIRO SA PETROBRAS"

    def test_clean_uppercases(self):
        """Output must be fully uppercased."""
        assert TextCleaner.clean("petrobras") == "PETROBRAS"

    def test_clean_normalizes_whitespace(self):
        """Multiple spaces must collapse to a single space."""
        result = TextCleaner.clean("Hello   World")
        assert "  " not in result
        assert result == "HELLO WORLD"

    def test_clean_strips_leading_trailing_whitespace(self):
        """Leading and trailing whitespace must be stripped."""
        result = TextCleaner.clean("  PETROBRAS  ")
        assert result == "PETROBRAS"

    def test_clean_none_returns_none(self):
        """None input must propagate as None (not crash)."""
        assert TextCleaner.clean(None) is None

    def test_clean_non_string_returns_input(self):
        """Non-string inputs must pass through unchanged."""
        assert TextCleaner.clean(42) == 42

    def test_clean_empty_string_returns_empty(self):
        """Empty strings should return empty after strip."""
        assert TextCleaner.clean("") == ""

    def test_clean_combined_accents_and_punctuation(self):
        """Full pipeline: accents + punctuation + whitespace + uppercase."""
        result = TextCleaner.clean("São Paulo S.A.")
        assert result == "SAO PAULO SA"

    def test_clean_removes_liquidacao(self):
        """Legal status 'EM LIQUIDACAO' must be removed."""
        assert TextCleaner.clean("PETROBRAS EM LIQUIDACAO") == "PETROBRAS"

    def test_clean_removes_recuperacao_judicial(self):
        """Legal status 'EM RECUPERACAO JUDICIAL' must be removed."""
        assert TextCleaner.clean("EMPRESA SA  EM RECUPERACAO JUDICIAL") == "EMPRESA SA"

    def test_clean_removes_liquidacao_extrajudicial(self):
        """Legal status 'EM LIQUIDACAO EXTRAJUDICIAL' must be removed."""
        assert TextCleaner.clean("TEST EM LIQUIDACAO EXTRAJUDICIAL") == "TEST"

    def test_clean_removes_rec_judicial_abbreviated(self):
        """Legal status 'EM REC JUDICIAL' must be removed."""
        assert TextCleaner.clean("TEST  EM REC JUDICIAL") == "TEST"

    def test_clean_removes_empresa_falida(self):
        """Legal status 'EMPRESA FALIDA' must be removed."""
        assert TextCleaner.clean("COMPANY EMPRESA FALIDA") == "COMPANY"

    def test_clean_exception_returns_original(self):
        """Should catch internal exceptions and fallback to returning the original string."""
        from unittest.mock import patch

        with patch(
            "shared.infrastructure.utils.text.unidecode.unidecode",
            side_effect=Exception("Mocked Error"),
        ):
            result = TextCleaner.clean("Company A")
            assert result == "Company A"

    def test_mutmut_trampoline_fail(self):
        """Simulate mutmut fail programmatic exception to cover trampoline method lines 15-19"""
        from shared.infrastructure.utils.text import _mutmut_trampoline
        import os
        from unittest.mock import patch

        def mock_orig():
            pass

        with patch.dict(os.environ, {"MUTANT_UNDER_TEST": "fail"}):
            with pytest.raises(
                Exception
            ):  # Catches MutmutProgrammaticFailException dynamically imported
                _mutmut_trampoline(mock_orig, {}, [], {})

    def test_mutmut_trampoline_stats(self):
        """Simulate mutmut stats telemetry logic to cover trampoline method lines 20-25"""
        from shared.infrastructure.utils.text import _mutmut_trampoline
        import os
        import sys
        from unittest.mock import patch, MagicMock

        mock_orig = MagicMock(return_value="Success")
        mock_orig.__module__ = "test"
        mock_orig.__name__ = "mock_orig"

        with patch.dict(os.environ, {"MUTANT_UNDER_TEST": "stats"}):
            # Create a mock module structure for mutmut.__main__
            mock_main_module = MagicMock()
            mock_record = MagicMock()
            mock_main_module.record_trampoline_hit = mock_record

            # Inject it into sys.modules so the from ... import works
            with patch.dict(
                sys.modules,
                {"mutmut": MagicMock(), "mutmut.__main__": mock_main_module},
            ):
                result = _mutmut_trampoline(mock_orig, {}, [], {})
                assert result == "Success"
                mock_record.assert_called_once_with("test.mock_orig")

    def test_mutmut_trampoline_not_matching_prefix(self):
        """Cover lines 26-29 for standard non-mutant pass-throughs."""
        from shared.infrastructure.utils.text import _mutmut_trampoline
        import os
        from unittest.mock import patch, MagicMock

        mock_orig = MagicMock(return_value="Original")
        mock_orig.__module__ = "test"
        mock_orig.__name__ = "mock_orig"

        with patch.dict(os.environ, {"MUTANT_UNDER_TEST": "other_module.mutant"}):
            result = _mutmut_trampoline(mock_orig, {}, [], {})
            assert result == "Original"

    def test_mutmut_trampoline_matching_prefix_bound(self):
        """Cover lines 30-36 for bound method mutations."""
        from shared.infrastructure.utils.text import _mutmut_trampoline
        import os
        from unittest.mock import patch, MagicMock

        mock_orig = MagicMock()
        mock_orig.__module__ = "test"
        mock_orig.__name__ = "mock_orig"

        mock_mutant = MagicMock(return_value="Mutated")
        # mutmut runtime splits by `__mutmut_` prefix but the right part of '.' partition usually is `test.mock_orig__mutmut_1` -> `test.mock_orig__mutmut_1` if no dots, or if standard `module.mock_orig__mutmut_1`
        mutant_name = "test.mock_orig__mutmut_1".rpartition(".")[-1]
        mutants = {mutant_name: mock_mutant}

        with patch.dict(os.environ, {"MUTANT_UNDER_TEST": "test.mock_orig__mutmut_1"}):
            result = _mutmut_trampoline(mock_orig, mutants, [], {}, self_arg="Self")
            assert result == "Mutated"
            mock_mutant.assert_called_with("Self")

    def test_mutmut_trampoline_matching_prefix_unbound(self):
        """Cover line 35 for unbound method mutations."""
        from shared.infrastructure.utils.text import _mutmut_trampoline
        import os
        from unittest.mock import patch, MagicMock

        mock_orig = MagicMock()
        mock_orig.__module__ = "test"
        mock_orig.__name__ = "mock_orig"

        mock_mutant = MagicMock(return_value="Mutated")
        mutant_name = "test.mock_orig__mutmut_1".rpartition(".")[-1]
        mutants = {mutant_name: mock_mutant}

        with patch.dict(os.environ, {"MUTANT_UNDER_TEST": "test.mock_orig__mutmut_1"}):
            result = _mutmut_trampoline(mock_orig, mutants, [], {})
            assert result == "Mutated"
            mock_mutant.assert_called_with()
