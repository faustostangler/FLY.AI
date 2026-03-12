import pytest
import json
import base64
from unittest.mock import AsyncMock, patch, MagicMock
from companies.infrastructure.adapters.data_sources.playwright_b3_data_source import PlaywrightB3DataSource


@pytest.fixture
def mock_playwright_infrastructure():
    """Mocks the playwright.async_api and the nested objects for the new session-based structure."""
    with patch("companies.infrastructure.adapters.data_sources.playwright_b3_data_source.async_playwright") as mock_pw_entry:
        
        # 1. async_playwright() returns a context manager that must be awaited if NOT calling .start()
        # But in our code we do: await async_playwright().start()
        # So: mock_pw_entry.return_value is the object returned by async_playwright()
        
        mock_playwright_instance = AsyncMock()
        mock_pw_entry.return_value.start = AsyncMock(return_value=mock_playwright_instance)
        
        # 2. Mock browser = await p.chromium.launch()
        mock_browser = AsyncMock()
        mock_playwright_instance.chromium.launch = AsyncMock(return_value=mock_browser)
        
        # 3. Mock context = await browser.new_context()
        mock_context = AsyncMock()
        mock_browser.new_context = AsyncMock(return_value=mock_context)
        
        # 4. Mock page = await context.new_page()
        mock_page = AsyncMock()
        mock_context.new_page = AsyncMock(return_value=mock_page)
        
        yield mock_context


@pytest.mark.asyncio
async def test_fetch_initial_companies_success(mock_playwright_infrastructure):
    # Setup mock response for the context.request.get
    mock_response = AsyncMock()
    mock_response.ok = True

    # Simulating a return after loop check (Note: -1 loop logic is active)
    mock_response.json = AsyncMock(return_value={
        "page": {"totalPages": -1},
        "results": [{"issuingCompany": "PETR", "companyName": "PETROBRAS"}]
    })

    mock_playwright_infrastructure.request.get = AsyncMock(return_value=mock_response)

    data_source = PlaywrightB3DataSource(headless=True)
    
    # Using the new Context Manager pattern required by the refactor
    async with data_source:
        results = await data_source.fetch_initial_companies()

    assert len(results) == 1
    assert results[0]["companyName"] == "PETROBRAS"


@pytest.mark.asyncio
async def test_fetch_company_details_success(mock_playwright_infrastructure):
    mock_response = AsyncMock()
    mock_response.ok = True
    mock_response.json = AsyncMock(return_value={"codeCVM": "9512", "sector": "Petróleo"})
    mock_playwright_infrastructure.request.get = AsyncMock(return_value=mock_response)

    data_source = PlaywrightB3DataSource(headless=True)
    
    async with data_source:
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
