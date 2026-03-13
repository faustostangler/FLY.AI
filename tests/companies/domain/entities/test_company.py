import pytest
from pydantic import ValidationError
from companies.domain.entities.company import Company

def test_company_creation_success():
    company = Company(
        ticker="PETR4",
        cvm_code="9512",
        company_name="Petróleo Brasileiro S.A. - Petrobras",
        trading_name="PETROBRAS",
        segment="Exploraçãso, Refino e Distribuição",
        sector="Petróleo, Gás e Biocombustíveis",
        subsector="Petróleo, Gás e Biocombustíveis",
        cnpj="33.000.167/0001-01"
    )
    assert company.ticker == "PETR4"
    assert company.cvm_code == "9512"
    assert company.cnpj.format() == "33.000.167/0001-01"

def test_company_invalid_ticker():
    with pytest.raises(ValidationError):
        Company(
            ticker="P",  # Too short
            cvm_code="9512",
            company_name="Petróleo Brasileiro S.A.",
            trading_name="PETROBRAS",
            segment="Exploração",
            sector="Petróleo",
            subsector="Petróleo"
        )

def test_company_invalid_cvm_code():
    with pytest.raises(ValidationError):
        Company(
            ticker="PETR4",
            cvm_code="abc",  # Must be digits
            company_name="Petrobras",
            trading_name="PETROBRAS"
        )

def test_company_text_cleaning_on_creation():
    company = Company(
        ticker="petr4",  # Should be uppercased/cleaned
        cvm_code="9512",
        company_name="Petróleo Brasileiro S.A.  -  Petrobras   EM LIQUIDACAO",
        trading_name="petrobras",
        registrar="  BANCO DO BRASIL  ",
        main_registrar=" BANCO B3  "
    )
    assert company.ticker == "PETR4"
    assert company.company_name == "PETROLEO BRASILEIRO SA PETROBRAS"
    assert company.trading_name == "PETROBRAS"
    assert company.registrar == "BANCO DO BRASIL"
    assert company.main_registrar == "BANCO B3"

def test_company_bool_resilient_validation():
    company = Company(
        ticker="PETR4",
        cvm_code="9512",
        company_name="Petrobras",
        has_quotation="ATIVO", # Should be True
        has_emissions="0",     # Should be False
        has_bdr="S"            # Should be True
    )
    assert company.has_quotation is True
    assert company.has_emissions is False
    assert company.has_bdr is True
