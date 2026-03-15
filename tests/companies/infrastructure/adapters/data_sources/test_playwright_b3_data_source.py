import pytest
import json
import base64
from unittest.mock import AsyncMock, patch, MagicMock
from companies.infrastructure.adapters.data_sources.playwright_b3_data_source import (
    PlaywrightB3DataSource,
)


@pytest.fixture
def mock_playwright_infrastructure():
    """Mocks the playwright.async_api and the nested objects for the new session-based structure."""
    with patch(
        "companies.infrastructure.adapters.data_sources.playwright_b3_data_source.async_playwright"
    ) as mock_pw_entry:
        # 1. async_playwright() returns a context manager that must be awaited if NOT calling .start()
        # But in our code we do: await async_playwright().start()
        # So: mock_pw_entry.return_value is the object returned by async_playwright()

        mock_playwright_instance = AsyncMock()
        mock_pw_entry.return_value.start = AsyncMock(
            return_value=mock_playwright_instance
        )

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
    # Arrange
    companies_data = {
        "page": {"totalPages": -1},
        "results": [{"issuingCompany": "PETR", "companyName": "PETROBRAS"}],
    }
    mock_response = AsyncMock()
    mock_response.ok = True
    mock_response.status = 200
    mock_response.body = AsyncMock(
        return_value=json.dumps(companies_data).encode("utf-8")
    )

    mock_playwright_infrastructure.request.get = AsyncMock(return_value=mock_response)

    data_source = PlaywrightB3DataSource(telemetry=MagicMock(), headless=True)

    # Using the new Context Manager pattern required by the refactor
    async with data_source:
        results = await data_source.fetch_initial_companies()

    assert len(results) == 1
    assert results[0]["companyName"] == "PETROBRAS"


@pytest.mark.asyncio
async def test_fetch_company_details_success(mock_playwright_infrastructure):
    details_data = {"codeCVM": "9512", "sector": "Petróleo"}
    mock_response = AsyncMock()
    mock_response.ok = True
    mock_response.status = 200
    mock_response.body = AsyncMock(
        return_value=json.dumps(details_data).encode("utf-8")
    )
    mock_playwright_infrastructure.request.get = AsyncMock(return_value=mock_response)

    data_source = PlaywrightB3DataSource(telemetry=MagicMock(), headless=True)

    async with data_source:
        details = await data_source.fetch_company_details("9512")

    assert details["sector"] == "Petróleo"
    assert details["codeCVM"] == "9512"


def test_create_token():
    data_source = PlaywrightB3DataSource(telemetry=MagicMock())
    payload = {"test": "data"}
    token = data_source._create_token(payload)

    # Verify it can be decoded back
    decoded = json.loads(base64.b64decode(token).decode("utf-8"))
    assert decoded["test"] == "data"


@pytest.mark.asyncio
async def test_fetch_initial_companies_rate_limit(mock_playwright_infrastructure):
    from companies.domain.exceptions import B3RateLimitExceededError

    mock_response = AsyncMock()
    mock_response.status = 429
    mock_playwright_infrastructure.request.get = AsyncMock(return_value=mock_response)

    telemetry = MagicMock()
    data_source = PlaywrightB3DataSource(telemetry=telemetry, headless=True)

    with pytest.raises(B3RateLimitExceededError):
        async with data_source:
            await data_source.fetch_initial_companies()

    telemetry.increment_b3_rate_limit_hits.assert_called_once()


@pytest.mark.asyncio
async def test_fetch_initial_companies_http_error(mock_playwright_infrastructure):
    mock_response = AsyncMock()
    mock_response.ok = False
    mock_response.status = 500
    mock_playwright_infrastructure.request.get = AsyncMock(return_value=mock_response)

    data_source = PlaywrightB3DataSource(telemetry=MagicMock(), headless=True)

    with pytest.raises(
        Exception, match="Failed to fetch initial companies page -1: 500"
    ):
        async with data_source:
            await data_source.fetch_initial_companies()


@pytest.mark.asyncio
async def test_fetch_company_details_rate_limit(mock_playwright_infrastructure):
    from companies.domain.exceptions import B3RateLimitExceededError

    mock_response = AsyncMock()
    mock_response.status = 429
    mock_playwright_infrastructure.request.get = AsyncMock(return_value=mock_response)

    telemetry = MagicMock()
    data_source = PlaywrightB3DataSource(telemetry=telemetry, headless=True)

    with pytest.raises(B3RateLimitExceededError):
        async with data_source:
            await data_source.fetch_company_details("123")

    telemetry.increment_b3_rate_limit_hits.assert_called_once()


@pytest.mark.asyncio
async def test_fetch_company_details_http_error(mock_playwright_infrastructure):
    mock_response = AsyncMock()
    mock_response.ok = False
    mock_response.status = 502
    mock_playwright_infrastructure.request.get = AsyncMock(return_value=mock_response)

    data_source = PlaywrightB3DataSource(telemetry=MagicMock(), headless=True)

    with pytest.raises(Exception, match="Failed to fetch details for 123: 502"):
        async with data_source:
            await data_source.fetch_company_details("123")


@pytest.mark.asyncio
async def test_fetch_company_financials_success(mock_playwright_infrastructure):
    finance_data = {"revenue": 10000}
    mock_response = AsyncMock()
    mock_response.ok = True
    mock_response.status = 200
    mock_response.json = AsyncMock(return_value=finance_data)
    mock_playwright_infrastructure.request.get = AsyncMock(return_value=mock_response)

    data_source = PlaywrightB3DataSource(telemetry=MagicMock(), headless=True)

    async with data_source:
        data = await data_source.fetch_company_financials("123")

    assert data["revenue"] == 10000


@pytest.mark.asyncio
async def test_fetch_company_financials_error(mock_playwright_infrastructure):
    mock_response = AsyncMock()
    mock_response.ok = False
    mock_response.status = 404
    mock_playwright_infrastructure.request.get = AsyncMock(return_value=mock_response)

    data_source = PlaywrightB3DataSource(telemetry=MagicMock(), headless=True)

    with pytest.raises(Exception, match="Failed to fetch financials for 123"):
        async with data_source:
            await data_source.fetch_company_financials("123")


@pytest.mark.asyncio
async def test_unmanaged_fallback_context(mock_playwright_infrastructure):
    """Test the 'is_temp = True' branch when __aenter__ is not used."""
    mock_response = AsyncMock()
    mock_response.ok = True
    mock_response.json = AsyncMock(return_value={"fin": "data"})
    mock_playwright_infrastructure.request.get = AsyncMock(return_value=mock_response)

    # Calling fetch outside of 'async with' context block
    data_source = PlaywrightB3DataSource(telemetry=MagicMock(), headless=True)

    data = await data_source.fetch_company_financials("123")

    assert data["fin"] == "data"

    # Verify that the browser was cleanly closed during the finally block
    # mock_playwright_infrastructure here represents the context mock
    mock_playwright_infrastructure.browser.close.assert_called_once()


@pytest.mark.asyncio
async def test_unmanaged_fallback_context_initial_and_details(
    mock_playwright_infrastructure,
):
    """Test the 'is_temp = True' branch for the other two endpoints to cover browser.close() and page.goto()."""
    companies_data = {
        "page": {"totalPages": 1},
        "results": [{"issuingCompany": "PETR", "companyName": "P"}],
    }
    mock_response = AsyncMock()
    mock_response.ok = True
    mock_response.status = 200
    mock_response.body = AsyncMock(
        return_value=json.dumps(companies_data).encode("utf-8")
    )
    mock_playwright_infrastructure.request.get = AsyncMock(return_value=mock_response)

    data_source = PlaywrightB3DataSource(telemetry=MagicMock(), headless=True)

    # 1. Test fetch_initial_companies (will trigger page.goto and page_num=1)
    results = await data_source.fetch_initial_companies()
    assert len(results) == 1
    mock_playwright_infrastructure.new_page.assert_called_once()
    mock_playwright_infrastructure.browser.close.assert_called_once()

    # Reset mock for the next call
    mock_playwright_infrastructure.browser.close.reset_mock()

    # 2. Test fetch_company_details
    details = await data_source.fetch_company_details("123")
    assert "page" in details
    mock_playwright_infrastructure.browser.close.assert_called_once()


@pytest.mark.asyncio
async def test_fetch_initial_companies_pagination_branch(
    mock_playwright_infrastructure,
):
    """Test the logic inside the loop when page_num == -1 to extract totalPages from payload."""
    data_page_minus_one = {
        "page": {"totalPages": 0},
        "results": [{"issuingCompany": "A"}],
    }
    data_page_zero = {"page": {"totalPages": 0}, "results": [{"issuingCompany": "B"}]}

    def mock_get_side_effect(endpoint, **kwargs):
        resp = AsyncMock()
        resp.ok = True
        resp.status = 200
        token = endpoint.split("/")[-1]
        decoded = json.loads(base64.b64decode(token).decode("utf-8"))
        p_num = decoded.get("pageNumber")

        if p_num == -1:
            resp.body = AsyncMock(
                return_value=json.dumps(data_page_minus_one).encode("utf-8")
            )
        elif p_num == 0:
            resp.body = AsyncMock(
                return_value=json.dumps(data_page_zero).encode("utf-8")
            )

        return resp

    mock_playwright_infrastructure.request.get = AsyncMock(
        side_effect=mock_get_side_effect
    )

    data_source = PlaywrightB3DataSource(telemetry=MagicMock(), headless=True)
    async with data_source:
        results = await data_source.fetch_initial_companies()

    # Should get companies A and B
    assert len(results) == 1
