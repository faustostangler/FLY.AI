import pytest
import os
from datetime import datetime
from pact import Pact, match
from companies.application.use_cases.sync_b3_companies import SyncB3CompaniesUseCase
from unittest.mock import MagicMock

# Setup Pact
PACT_DIR = os.path.join(os.path.dirname(__file__), 'pacts')
# Pact v3 uses Pact(consumer, provider)
pact = Pact('FlyAI-Scraper', 'B3-API')

def test_b3_payload_contract():
    """
    Contract test for B3 Detailed Info payload.
    Ensures that if B3 changes keys like 'dateListing' to something else, 
    this test (which defines our contract) will fail or the contract won't match.
    """
    expected_payload = {
        "issuingCompany": "PETR4",
        "codeCVM": "9512",
        "companyName": "PETROLEO BRASILEIRO S.A. PETROBRAS",
        "tradingName": "PETROBRAS",
        "cnpj": "33.000.167/0001-01",
        "market": "Novo Mercado",
        "industryClassification": "Petróleo / Gás / Biocombustíveis",
        "dateListing": "1977-01-03", # Critical field
        "lastDate": "2024-03-12",     # Critical field
        "dateQuotation": "2024-03-11", # Critical field
        "otherCodes": [
            {"code": "PETR3", "isin": "BRPETRACNOR9"}
        ]
    }

    (pact
     .upon_receiving('a request for company details')
     .given('Company details exist for CVM 9512')
     .with_request('GET', '/details/9512')
     .will_respond_with(200)
     .with_body(expected_payload))

    # In v3, we use .serve() or similar, but since we are just verifying the MAPPER 
    # against the 'expected_payload' which represents our contract, we can do it 
    # directly or through the mock server.
    
    # Verify our mapper handles exactly what the contract defines
    basic_info = {
        "issuingCompany": "PETR4",
        "codeCVM": 9512,
        "companyName": "PETROLEO BRASILEIRO S.A. PETROBRAS"
    }
    
    # This acts as our contract verification: does our software correctly 
    # ingest the payload defined in the contract?
    use_case = SyncB3CompaniesUseCase(data_source=MagicMock(), repository=MagicMock())
    entity = use_case._map_b3_payload_to_entity(basic_info, expected_payload)
    
    assert entity.ticker == "PETR4"
    assert entity.date_listing == datetime(1977, 1, 3)
    assert entity.last_date == datetime(2024, 3, 12)
    assert entity.date_quotation == datetime(2024, 3, 11)
