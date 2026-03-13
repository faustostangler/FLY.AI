import pytest
from shared.infrastructure.utils.text import TextCleaner

def test_text_cleaner_removes_multiple_spaces():
    assert TextCleaner.clean("Hello   World") == "HELLO WORLD"

def test_text_cleaner_removes_liquidacao():
    assert TextCleaner.clean("PETROBRAS EM LIQUIDACAO") == "PETROBRAS"

def test_text_cleaner_removes_recuperacao_judicial():
    assert TextCleaner.clean("EMPRESA SA  EM RECUPERACAO JUDICIAL") == "EMPRESA SA"

def test_text_cleaner_handles_none():
    assert TextCleaner.clean(None) is None

def test_text_cleaner_removes_b3_specific_trash():
    assert TextCleaner.clean("TEST  EM REC JUDICIAL") == "TEST"
    assert TextCleaner.clean("TEST EM LIQUIDACAO EXTRAJUDICIAL") == "TEST"
