import pytest
import json
from datetime import datetime
from unittest.mock import MagicMock
from companies.application.use_cases.sync_b3_companies import SyncB3CompaniesUseCase
from companies.domain.entities.company import Company

class TestSyncB3CompaniesUseCase:
    @pytest.fixture
    def use_case(self):
        data_source = MagicMock()
        repository = MagicMock()
        return SyncB3CompaniesUseCase(data_source, repository)

    def test_map_b3_payload_to_entity_success(self, use_case):
        # Arrange
        basic_info = {
            "issuingCompany": "PETR4",
            "codeCVM": 9512,
            "companyName": "PETROLEO BRASILEIRO S.A. PETROBRAS"
        }
        
        detailed_info = {
            "tradingName": "PETROBRAS",
            "cnpj": "33.000.167/0001-01",
            "market": "Novo Mercado",
            "industryClassification": "Petróleo, Gás e Biocombustíveis / Petróleo, Gás e Biocombustíveis / Exploração, Refino e Distribuição",
            "otherCodes": [
                {"code": "PETR3", "isin": "BRPETRACNOR9"},
                {"code": "PETR4", "isin": "BRPETRACNPR6"}
            ],
            "website": "www.petrobras.com.br",
            "status": "ATIVO"
        }

        # Act
        company = use_case._map_b3_payload_to_entity(basic_info, detailed_info)

        # Assert
        assert company.ticker == "PETR4"
        assert company.cvm_code == "9512"
        assert company.company_name == "PETROLEO BRASILEIRO SA PETROBRAS"
        assert company.sector == "PETROLEO GAS E BIOCOMBUSTIVEIS"
        assert company.subsector == "PETROLEO GAS E BIOCOMBUSTIVEIS"
        assert company.segment == "EXPLORACAO REFINO E DISTRIBUICAO"
        
        # Security identifiers
        assert "PETR3" in company.ticker_codes
        assert "PETR4" in company.ticker_codes
        assert "BRPETRACNOR9" in company.isin_codes
        assert "BRPETRACNPR6" in company.isin_codes

    def test_map_b3_payload_to_entity_with_missing_industry_classification(self, use_case):
        # Arrange
        basic_info = {"issuingCompany": "TEST3", "codeCVM": 123, "companyName": "TEST"}
        detailed_info = {
            "industryClassification": "Setor Unico",
            "otherCodes": []
        }

        # Act
        company = use_case._map_b3_payload_to_entity(basic_info, detailed_info)

        # Assert
        assert company.sector == "SETOR UNICO"
        assert company.subsector == "SETOR UNICO"
        assert company.segment == "SETOR UNICO"

    def test_map_b3_payload_to_entity_with_none_other_codes(self, use_case):
        # Arrange
        basic_info = {"issuingCompany": "TEST3", "codeCVM": 123, "companyName": "TEST"}
        detailed_info = {
            "otherCodes": None
        }

        # Act
        company = use_case._map_b3_payload_to_entity(basic_info, detailed_info)

        # Assert
        assert company.ticker_codes == []
        assert company.isin_codes == []
    def test_map_b3_payload_to_entity_with_dates(self, use_case):
        # Arrange
        basic_info = {
            "issuingCompany": "VALE3",
            "codeCVM": 4170,
            "companyName": "VALE S.A.",
            "dateListing": "1943-10-25"
        }
        
        detailed_info = {
            "lastDate": "2024-03-12",
            "dateQuotation": "2024-03-11",
            "describleCategoryBVMF": "Categoria A",
            "marketIndicator": "1",
            "hasQuotation": True,
            "hasEmissions": False,
            "hasBDR": "N"
        }

        # Act
        company = use_case._map_b3_payload_to_entity(basic_info, detailed_info)

        # Assert
        assert company.date_listing == datetime(1943, 10, 25)
        assert company.last_date == datetime(2024, 3, 12)
        assert company.date_quotation == datetime(2024, 3, 11)
        assert company.describle_category_bvmf == "CATEGORIA A"
        assert company.has_quotation is True
        assert company.has_emissions is False
        assert company.has_bdr is False
