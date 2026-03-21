from companies.application.dtos.b3_company_dto import B3CompanyPayloadDTO
from companies.domain.entities.company import Company
from companies.domain.value_objects.cnpj import CNPJ


def test_dto_sanitization_and_resilience():
    raw_data = {
        "ticker": "  petr4  ",
        "cvm_code": "9512",
        "company_name": "Petróleo Brasileiro S.A.  -  Petrobras   EM LIQUIDACAO",
        "trading_name": "petrobras",
        "cnpj": "33.000.167/0001-01",
        "has_quotation": "ATIVO",
        "has_emissions": "0",
        "has_bdr": "S",
        "registrar": "  BANCO DO BRASIL  ",
    }

    dto = B3CompanyPayloadDTO(**raw_data)

    assert dto.ticker == "PETR4"
    assert dto.company_name == "PETROLEO BRASILEIRO SA PETROBRAS"
    assert dto.has_quotation is True
    assert dto.has_emissions is False
    assert dto.has_bdr is True
    assert dto.registrar == "BANCO DO BRASIL"


from shared.domain.utils.result import Result


def test_dto_to_domain_conversion():
    raw_data = {
        "ticker": "PETR4",
        "cvm_code": "9512",
        "company_name": "PETROBRAS",
        "cnpj": "33000167000101",
    }

    dto = B3CompanyPayloadDTO(**raw_data)
    result = dto.to_domain()

    assert isinstance(result, Result)
    assert result.is_success
    company = result.unwrap()
    assert isinstance(company, Company)
    assert company.ticker == "PETR4"
    assert isinstance(company.cnpj, CNPJ)
    assert company.cnpj.root == "33000167000101"


def test_dto_ignores_extra_fields():
    raw_data = {
        "ticker": "PETR4",
        "cvm_code": "9512",
        "company_name": "PETROBRAS",
        "something_garbage": "totally ignore me",
    }
    # Should not raise exception because ConfigDict(extra='ignore')
    dto = B3CompanyPayloadDTO(**raw_data)
    assert not hasattr(dto, "something_garbage")
