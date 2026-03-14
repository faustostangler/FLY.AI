"""Root conftest — Shared DDD Test Factories & Fixtures.

Centralizes reusable test infrastructure for all Bounded Contexts.
Following the DDD testing strategy:
    - Domain tests: No mocks, pure entity/value object assertions.
    - Application tests: Mock external ports (repository, data source).
    - Infrastructure tests: Integration tests with real adapters.
    - Presentation tests: E2E/Integration via FastAPI TestClient.
"""

import pytest
from datetime import datetime
from unittest.mock import MagicMock, AsyncMock

from companies.domain.entities.company import Company
from companies.domain.value_objects.cnpj import CNPJ
from shared.domain.ports.telemetry_port import TelemetryPort


# ======================================================================
# Domain Factories — Pure Entity Construction (No Infrastructure)
# ======================================================================

class CompanyFactory:
    """Factory for creating Company domain entities with sensible defaults.

    Follows the Object Mother pattern to reduce test boilerplate
    while keeping entity construction explicit and DDD-compliant.
    """

    VALID_CNPJ_PETROBRAS = "33000167000101"
    VALID_CNPJ_VALE = "33592510000154"

    @staticmethod
    def create(
        ticker: str = "PETR4",
        cvm_code: str = "9512",
        company_name: str = "PETROLEO BRASILEIRO SA PETROBRAS",
        trading_name: str = "PETROBRAS",
        cnpj: str | None = "33000167000101",
        status: str = "ATIVO",
        sector: str = "PETROLEO GAS E BIOCOMBUSTIVEIS",
        **kwargs,
    ) -> Company:
        """Creates a valid Company entity with optional overrides."""
        return Company(
            ticker=ticker,
            cvm_code=cvm_code,
            company_name=company_name,
            trading_name=trading_name,
            cnpj=CNPJ(cnpj) if cnpj else None,
            status=status,
            sector=sector,
            **kwargs,
        )

    @staticmethod
    def create_minimal(
        ticker: str = "TEST3",
        cvm_code: str = "12345",
        company_name: str = "TEST COMPANY SA",
    ) -> Company:
        """Creates a Company with only the required invariant fields."""
        return Company(
            ticker=ticker,
            cvm_code=cvm_code,
            company_name=company_name,
        )


# ======================================================================
# Mock Factories — Port Doubles for Application Layer Tests
# ======================================================================

class MockTelemetryPort(TelemetryPort):
    """In-memory TelemetryPort double that records all calls.

    Useful for asserting that the Use Case emits the correct
    domain metrics without coupling tests to Prometheus internals.
    """

    def __init__(self):
        self.calls: list[tuple[str, dict]] = []

    def _record(self, method: str, **kwargs):
        self.calls.append((method, kwargs))

    def increment_active_sync_tasks(self) -> None:
        self._record("increment_active_sync_tasks")

    def decrement_active_sync_tasks(self) -> None:
        self._record("decrement_active_sync_tasks")

    def increment_companies_synced(self, count: int, status: str) -> None:
        self._record("increment_companies_synced", count=count, status=status)

    def set_companies_by_sector(self, sector: str, count: int) -> None:
        self._record("set_companies_by_sector", sector=sector, count=count)

    def set_companies_by_segment(self, segment: str, count: int) -> None:
        self._record("set_companies_by_segment", segment=segment, count=count)

    def observe_sync_duration(self, context: str, duration: float) -> None:
        self._record("observe_sync_duration", context=context, duration=duration)

    def increment_date_parsing_failures(self, field: str, source: str) -> None:
        self._record("increment_date_parsing_failures", field=field, source=source)

    def increment_b3_rate_limit_hits(self) -> None:
        self._record("increment_b3_rate_limit_hits")

    def increment_network_transmit_bytes(self, direction: str, context: str, payload_size: int) -> None:
        self._record("increment_network_transmit_bytes", direction=direction, context=context, payload_size=payload_size)

    def increment_data_validation_error(self, entity: str, field: str, reason: str) -> None:
        self._record("increment_data_validation_error", entity=entity, field=field, reason=reason)

    def increment_generic_sync_error(self, type: str) -> None:
        self._record("increment_generic_sync_error", type=type)

    def get_calls(self, method: str) -> list[dict]:
        """Returns all recorded calls for a specific telemetry method."""
        return [kwargs for name, kwargs in self.calls if name == method]


# ======================================================================
# Pytest Fixtures
# ======================================================================

@pytest.fixture
def company_factory():
    """Provides the CompanyFactory for test methods."""
    return CompanyFactory


@pytest.fixture
def mock_telemetry():
    """Provides a recording TelemetryPort double."""
    return MockTelemetryPort()


@pytest.fixture
def mock_repository():
    """Provides a MagicMock CompanyRepository port."""
    repo = MagicMock()
    repo.save = MagicMock()
    repo.save_batch = MagicMock()
    repo.get_by_ticker = MagicMock(return_value=None)
    repo.get_all = MagicMock(return_value=[])
    return repo


@pytest.fixture
def mock_data_source():
    """Provides an AsyncMock B3DataSource port."""
    ds = AsyncMock()
    ds.fetch_initial_companies = AsyncMock(return_value=[])
    ds.fetch_company_details = AsyncMock(return_value={})
    ds.fetch_company_financials = AsyncMock(return_value={})
    ds.__aenter__ = AsyncMock(return_value=ds)
    ds.__aexit__ = AsyncMock(return_value=None)
    return ds


@pytest.fixture
def sample_b3_basic_info():
    """Raw B3 initial listing payload for testing the ACL."""
    return {
        "issuingCompany": "PETR4",
        "codeCVM": 9512,
        "companyName": "PETROLEO BRASILEIRO S.A. PETROBRAS",
        "dateListing": "2002-06-21",
    }


@pytest.fixture
def sample_b3_detailed_info():
    """Raw B3 detail API payload for testing the ACL."""
    return {
        "issuingCompany": "PETR4",
        "companyName": "PETROLEO BRASILEIRO S.A. PETROBRAS",
        "tradingName": "PETROBRAS",
        "cnpj": "33.000.167/0001-01",
        "market": "Novo Mercado",
        "industryClassification": (
            "Petróleo, Gás e Biocombustíveis / "
            "Petróleo, Gás e Biocombustíveis / "
            "Exploração, Refino e Distribuição"
        ),
        "otherCodes": [
            {"code": "PETR3", "isin": "BRPETRACNOR9"},
            {"code": "PETR4", "isin": "BRPETRACNPR6"},
        ],
        "website": "www.petrobras.com.br",
        "status": "ATIVO",
        "dateListing": "2002-06-21",
        "lastDate": "2024-03-12",
        "dateQuotation": "2024-03-11",
        "hasQuotation": True,
        "hasEmissions": False,
        "hasBDR": "N",
    }
