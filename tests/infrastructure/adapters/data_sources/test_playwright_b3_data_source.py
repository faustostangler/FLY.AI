import pytest
import json
import base64
from unittest.mock import AsyncMock, patch, MagicMock
from infrastructure.adapters.data_sources.playwright_b3_data_source import PlaywrightB3DataSource


@pytest.fixture
def mock_playwright():
    """Mocks the playwright.async_api"""
    with patch("infrastructure.adapters.data_sources.playwright_b3_data_source.async_playwright") as mock_pw:
        mock_context_manager = AsyncMock()
        mock_pw.return_value = mock_context_manager

        mock_playwright_instance = AsyncMock()
        mock_context_manager.__aenter__.return_value = mock_playwright_instance

        mock_browser = AsyncMock()
        mock_playwright_instance.chromium.launch.return_value = mock_browser

        mock_context = AsyncMock()
        mock_browser.new_context.return_value = mock_context

        mock_page = AsyncMock()
        mock_context.new_page.return_value = mock_page

        yield mock_context


@pytest.mark.asyncio
async def test_fetch_initial_companies_success(mock_playwright):
    # Setup mock response for the context.request.get
    mock_response = AsyncMock()
    mock_response.ok = True

    # Simulating a 1-page return from B3
    mock_response.json.return_value = {
        "page": {"totalPages": 1},
        "results": [{"issuingCompany": "PETR", "companyName": "PETROBRAS"}]
    }

    mock_playwright.request.get.return_value = mock_response

    data_source = PlaywrightB3DataSource(headless=True)
    results = await data_source.fetch_initial_companies()

    assert len(results) == 1
    assert results[0]["companyName"] == "PETROBRAS"


@pytest.mark.asyncio
async def test_fetch_company_details_success(mock_playwright):
    mock_response = AsyncMock()
    mock_response.ok = True
    mock_response.json.return_value = {"codeCVM": "9512", "sector": "Petróleo"}
    mock_playwright.request.get.return_value = mock_response

    data_source = PlaywrightB3DataSource(headless=True)
    details = await data_source.fetch_company_details("9512")

    assert details["sector"] == "Petróleo"
    assert details["codeCVM"] == "9512"


def test_create_token():
    data_source = PlaywrightB3DataSource()
    payload = {"test": "data"}
    token = data_source._create_token(payload)

    # Verify it can be decoded back
    decoded = json.loads(base64.b64decode(token).decode("utf-8"))
    assert decoded["test"] == "data"
