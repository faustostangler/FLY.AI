import pytest
from pydantic import ValidationError
from src.companies.domain.entities.company import Company

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
            company_name="Petróleo Brasileiro S.A.",
            trading_name="PETROBRAS",
            segment="Exploração",
            sector="Petróleo",
            subsector="Petróleo"
        )
