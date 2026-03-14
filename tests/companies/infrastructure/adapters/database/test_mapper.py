import json
import pytest
from companies.domain.entities.company import Company
from companies.domain.value_objects.cnpj import CNPJ
from companies.infrastructure.adapters.database.models import CompanyModel
from companies.infrastructure.adapters.database.mapper import CompanyDataMapper

def test_company_mapper_to_model_json_serialization():
    """Test if lists are correctly serialized to JSON strings in the model."""
    company = Company(
        ticker="PETR4",
        cvm_code="9512",
        company_name="PETROLEO BRASILEIRO SA PETROBRAS",
        ticker_codes=["PETR3", "PETR4"],
        isin_codes=["BRPETRACNPR6"]
    )
    
    model = CompanyDataMapper.to_model(company)
    
    assert isinstance(model.ticker_codes, str)
    assert json.loads(model.ticker_codes) == ["PETR3", "PETR4"]
    assert json.loads(model.isin_codes) == ["BRPETRACNPR6"]

def test_company_mapper_to_entity_json_deserialization():
    """Test if JSON strings from the model are correctly deserialized to lists in the entity."""
    model = CompanyModel(
        ticker="PETR4",
        cvm_code="9512",
        company_name="PETROBRAS",
        ticker_codes='["PETR3", "PETR4"]',
        isin_codes='["BRPETRACNPR6"]',
        cnpj="33000167000101"
    )
    
    entity = CompanyDataMapper.to_entity(model)
    
    assert isinstance(entity.ticker_codes, list)
    assert entity.ticker_codes == ["PETR3", "PETR4"]
    assert entity.isin_codes == ["BRPETRACNPR6"]
    assert isinstance(entity.cnpj, CNPJ)
    assert entity.cnpj.root == "33000167000101"

def test_company_mapper_persistence_dict_cleansing():
    """Test if the generated dictionary for persistence is clean (no 'id' or ORM state)."""
    company = Company(
        ticker="PETR4",
        cvm_code="9512",
        company_name="PETROBRAS"
    )
    
    persist_dict = CompanyDataMapper.to_persistence_dict(company)
    
    assert "ticker" in persist_dict
    assert "cvm_code" in persist_dict
    assert "id" not in persist_dict
    assert "_sa_instance_state" not in persist_dict
    assert persist_dict["ticker"] == "PETR4"

def test_company_mapper_to_entity_handles_malformed_json():
    """Test resilience when database contains malformed JSON strings."""
    model = CompanyModel(
        ticker="PETR4",
        cvm_code="9512",
        company_name="PETROBRAS",
        ticker_codes="[invalid json",
        isin_codes=None
    )
    
    entity = CompanyDataMapper.to_entity(model)
    
    assert entity.ticker_codes == []
    assert entity.isin_codes == []
