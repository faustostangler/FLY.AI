from shared.domain.utils.result import Result
from companies.domain.entities.company import Company
from companies.domain.exceptions import CompanyValidationError
from companies.domain.value_objects.cnpj import CNPJ


def test_company_creation_success():
    result = Company.create(
        ticker="PETR4",
        cvm_code="9512",
        company_name="PETROLEO BRASILEIRO SA PETROBRAS",
        trading_name="PETROBRAS",
        segment="PETROLEO GAS E BIOCOMBUSTIVEIS",
        sector="PETROLEO GAS E BIOCOMBUSTIVEIS",
        subsector="PETROLEO GAS E BIOCOMBUSTIVEIS",
        cnpj=CNPJ("33000167000101"),
    )
    
    assert isinstance(result, Result)
    assert result.is_success
    company = result.unwrap()
    assert company.ticker == "PETR4"
    assert company.cvm_code == "9512"
    assert company.cnpj.root == "33000167000101"


def test_company_invalid_ticker():
    result = Company.create(
        ticker="P",  # Too short (Domain rule: 2-12)
        cvm_code="9512",
        company_name="PETROLEO BRASILEIRO SA",
    )
    
    assert result.is_failure
    assert isinstance(result.error, CompanyValidationError)
    assert "ticker" in str(result.error).lower()


def test_company_invalid_cvm_code():
    result = Company.create(
        ticker="PETR4",
        cvm_code="abc",  # Must be digits
        company_name="PETROBRAS",
    )
    
    assert result.is_failure
    assert isinstance(result.error, CompanyValidationError)
    assert "cvm code" in str(result.error).lower()


def test_company_behavior_mark_as_delisted():
    from datetime import datetime

    company = Company(
        ticker="PETR4",
        cvm_code="9512",
        company_name="PETROBRAS",
        status="ATIVO",
        has_quotation=True,
    )

    delist_date = datetime(2024, 1, 1)
    company.mark_as_delisted(delist_date)

    assert company.status == "INATIVO"
    assert company.last_date == delist_date
    assert company.has_quotation is False


def test_company_behavior_add_security_codes():
    company = Company(ticker="PETR4", cvm_code="9512", company_name="PETROBRAS")

    company.add_security_codes("BRB3SAACNOR6", "B3SA3")
    assert "BRB3SAACNOR6" in company.isin_codes
    assert "B3SA3" in company.ticker_codes

    # Duplicate addition should be idempotent (per domain rule in method)
    company.add_security_codes("BRB3SAACNOR6", "B3SA3")
    assert len(company.isin_codes) == 1
    assert len(company.ticker_codes) == 1
