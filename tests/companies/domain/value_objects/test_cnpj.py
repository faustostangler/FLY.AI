import pytest
from pydantic import ValidationError
from companies.domain.value_objects.cnpj import CNPJ

def test_cnpj_valid():
    # Apple Computer Brasil Ltda
    valid_cnpj = "00.623.904/0001-73"
    cnpj = CNPJ(valid_cnpj)
    assert cnpj.root == "00623904000173"
    assert cnpj.format() == "00.623.904/0001-73"

def test_cnpj_valid_unformatted():
    valid_cnpj = "00623904000173"
    cnpj = CNPJ(valid_cnpj)
    assert cnpj.root == "00623904000173"

def test_cnpj_invalid_length():
    with pytest.raises(ValidationError) as exc:
        CNPJ("123")
    assert "CNPJ must have exactly 14 digits" in str(exc.value)

def test_cnpj_invalid_all_same_digits():
    with pytest.raises(ValidationError) as exc:
        CNPJ("11111111111111")
    assert "CNPJ has invalid format" in str(exc.value)

def test_cnpj_invalid_check_digits():
    with pytest.raises(ValidationError) as exc:
        CNPJ("00.623.904/0001-74")  # Last digit changed
    assert "CNPJ has invalid check digits" in str(exc.value)

def test_cnpj_empty():
    with pytest.raises(ValidationError) as exc:
        CNPJ("")
    assert "CNPJ cannot be empty" in str(exc.value)
