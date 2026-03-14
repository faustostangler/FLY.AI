import pytest
from companies.domain.entities.company import Company
from companies.domain.exceptions import CompanyValidationError

def test_company_creation_success():
    # Note: CNPJ must be passed as a CNPJ object or wait... 
    # the repository used CNPJ(model.cnpj). 
    # In the entity, we use Optional[CNPJ]
    from companies.domain.value_objects.cnpj import CNPJ
    
    company = Company(
        ticker="PETR4",
        cvm_code="9512",
        company_name="PETROLEO BRASILEIRO SA PETROBRAS",
        trading_name="PETROBRAS",
        segment="PETROLEO GAS E BIOCOMBUSTIVEIS",
        sector="PETROLEO GAS E BIOCOMBUSTIVEIS",
        subsector="PETROLEO GAS E BIOCOMBUSTIVEIS",
        cnpj=CNPJ("33000167000101")
    )
    assert company.ticker == "PETR4"
    assert company.cvm_code == "9512"
    assert company.cnpj.root == "33000167000101"

def test_company_invalid_ticker():
    from companies.domain.value_objects.cnpj import CNPJ
    with pytest.raises(CompanyValidationError):
        Company(
            ticker="P",  # Too short (Domain rule: 2-12)
            cvm_code="9512",
            company_name="PETROLEO BRASILEIRO SA",
        )

def test_company_invalid_cvm_code():
    with pytest.raises(CompanyValidationError):
        Company(
            ticker="PETR4",
            cvm_code="abc",  # Must be digits
            company_name="PETROBRAS"
        )

def test_company_behavior_mark_as_delisted():
    from datetime import datetime
    company = Company(
        ticker="PETR4",
        cvm_code="9512",
        company_name="PETROBRAS",
        status="ATIVO",
        has_quotation=True
    )
    
    delist_date = datetime(2024, 1, 1)
    company.mark_as_delisted(delist_date)
    
    assert company.status == "INATIVO"
    assert company.last_date == delist_date
    assert company.has_quotation is False

def test_company_behavior_add_security_codes():
    company = Company(
        ticker="PETR4",
        cvm_code="9512",
        company_name="PETROBRAS"
    )
    
    company.add_security_codes("BRB3SAACNOR6", "B3SA3")
    assert "BRB3SAACNOR6" in company.isin_codes
    assert "B3SA3" in company.ticker_codes
    
    # Duplicate addition should be idempotent (per domain rule in method)
    company.add_security_codes("BRB3SAACNOR6", "B3SA3")
    assert len(company.isin_codes) == 1
    assert len(company.ticker_codes) == 1
