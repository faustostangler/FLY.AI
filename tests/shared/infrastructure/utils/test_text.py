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
