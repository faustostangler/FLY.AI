from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch, MagicMock
from companies.presentation.api.dependencies import get_trigger_b3_sync_use_case

from main import app
from companies.infrastructure.adapters.database.models import Base
from sqlalchemy import create_engine

engine_test = create_engine(
    "sqlite:///:memory:", connect_args={"check_same_thread": False}
)
Base.metadata.create_all(bind=engine_test)

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"
def test_trigger_companies_sync():
    # Mock the new Trigger Use Case
    mock_use_case = MagicMock()
    mock_use_case.execute = AsyncMock()
    
    app.dependency_overrides[get_trigger_b3_sync_use_case] = lambda: mock_use_case

    response = client.post("/api/v1/companies/sync")
    
    assert response.status_code == 202
    assert response.json()["status"] == "accepted"
    
    # Assert Domain Use Case was executed with a reference date from presentation
    mock_use_case.execute.assert_called_once()
    args, kwargs = mock_use_case.execute.call_args
    import datetime
    assert isinstance(kwargs["reference_date"], datetime.date)
    
    # Cleanup override
    app.dependency_overrides.pop(get_trigger_b3_sync_use_case, None)
