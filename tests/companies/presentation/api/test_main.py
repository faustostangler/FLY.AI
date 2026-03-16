from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch

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


@patch("companies.presentation.api.routes.get_arq_redis_pool")
def test_trigger_companies_sync(mock_get_arq_redis_pool):
    # Mock ARQ enqueuer
    mock_redis = AsyncMock()
    mock_get_arq_redis_pool.return_value = mock_redis

    response = client.post("/api/v1/companies/sync")
    
    assert response.status_code == 202
    assert response.json()["status"] == "accepted"
    
    # Assert ARQ task was scheduled
    mock_redis.enqueue_job.assert_called_once()
    args, kwargs = mock_redis.enqueue_job.call_args
    assert args[0] == "run_sync_b3_companies"
    assert "_job_id" in kwargs
