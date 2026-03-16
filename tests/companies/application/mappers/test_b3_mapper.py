import pytest
from datetime import datetime
from unittest.mock import MagicMock
from companies.application.mappers.b3_mapper import B3CompanyMapper


class TestB3CompanyMapper:
    @pytest.fixture
    def telemetry(self):
        return MagicMock()

    def test_to_domain_success(self, telemetry):
        # Arrange
        basic_info = {
            "issuingCompany": "PETR4",
            "codeCVM": 9512,
            "companyName": "PETROLEO BRASILEIRO S.A. PETROBRAS",
        }

        detailed_info = {
            "tradingName": "PETROBRAS",
            "cnpj": "33.000.167/0001-01",
            "market": "Novo Mercado",
            "industryClassification": "Petróleo, Gás e Biocombustíveis / Petróleo, Gás e Biocombustíveis / Exploração, Refino e Distribuição",
            "otherCodes": [
                {"code": "PETR3", "isin": "BRPETRACNOR9"},
                {"code": "PETR4", "isin": "BRPETRACNPR6"},
            ],
            "website": "www.petrobras.com.br",
            "status": "ATIVO",
        }

        # Act
        company = B3CompanyMapper.to_domain(basic_info, detailed_info, telemetry)

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

    def test_to_domain_with_missing_industry_classification(self, telemetry):
        # Arrange
        basic_info = {"issuingCompany": "TEST3", "codeCVM": 123, "companyName": "TEST"}
        detailed_info = {"industryClassification": "Setor Unico", "otherCodes": []}

        # Act
        company = B3CompanyMapper.to_domain(basic_info, detailed_info, telemetry)

        # Assert
        assert company.sector == "SETOR UNICO"
        assert company.subsector == "SETOR UNICO"
        assert company.segment == "SETOR UNICO"

    def test_to_domain_with_none_other_codes(self, telemetry):
        # Arrange
        basic_info = {"issuingCompany": "TEST3", "codeCVM": 123, "companyName": "TEST"}
        detailed_info = {"otherCodes": None}

        # Act
        company = B3CompanyMapper.to_domain(basic_info, detailed_info, telemetry)

        # Assert
        assert company.ticker_codes == []
        assert company.isin_codes == []

    def test_to_domain_with_dates(self, telemetry):
        # Arrange
        basic_info = {
            "issuingCompany": "VALE3",
            "codeCVM": 4170,
            "companyName": "VALE S.A.",
            "dateListing": "1943-10-25",
        }

        detailed_info = {
            "lastDate": "2024-03-12",
            "dateQuotation": "2024-03-11",
            "describleCategoryBVMF": "Categoria A",
            "marketIndicator": "1",
            "hasQuotation": True,
            "hasEmissions": False,
            "hasBDR": "N",
        }

        # Act
        company = B3CompanyMapper.to_domain(basic_info, detailed_info, telemetry)

        # Assert
        assert company.date_listing == datetime(1943, 10, 25)
        assert company.last_date == datetime(2024, 3, 12)
        assert company.date_quotation == datetime(2024, 3, 11)
        assert company.describle_category_bvmf == "CATEGORIA A"
        assert company.has_quotation is True
        assert company.has_emissions is False
        assert company.has_bdr is False

    def test_to_domain_with_institutional_info(self, telemetry):
        # Arrange
        basic_info = {"issuingCompany": "CBTC", "codeCVM": 123, "companyName": "TEMP"}
        detailed_info = {
            "issuingCompany": "BTC1",  # Should override
            "companyName": "BITCOIN ETP",  # Should override
            "institutionCommon": "BANCO A",
            "institutionPreferred": "BANCO B3 S.A.",
        }

        # Act
        company = B3CompanyMapper.to_domain(basic_info, detailed_info, telemetry)

        # Assert
        assert company.ticker == "BTC1"
        assert company.company_name == "BITCOIN ETP"
        assert company.registrar == "BANCO A"
        assert company.main_registrar == "BANCO B3 SA"
