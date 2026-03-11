import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, MagicMock
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from presentation.api.main import app
from presentation.api.dependencies import get_sync_b3_companies_use_case
from infrastructure.database.connection import get_db
from infrastructure.database.models import Base

# Setup in-memory SQLite for testing to avoid hitting Postgres layer during fast unit tests
engine_test = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)
Base.metadata.create_all(bind=engine_test)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

# Mock the Use Case
mock_use_case = MagicMock()
mock_use_case.execute = AsyncMock()

def override_get_use_case():
    return mock_use_case

app.dependency_overrides[get_sync_b3_companies_use_case] = override_get_use_case
app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_trigger_companies_sync():
    mock_use_case.reset_mock()
    response = client.post("/api/v1/sync/companies")
    assert response.status_code == 200
    assert response.json()["status"] == "accepted"
    # the execute method should be called as a background task
    mock_use_case.execute.assert_called_once()
