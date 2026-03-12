from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, BackgroundTasks

from application.use_cases.sync_b3_companies import SyncB3CompaniesUseCase
from presentation.api.dependencies import get_sync_b3_companies_use_case
from infrastructure.database.connection import engine
from infrastructure.database.models import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Ensure tables are created on startup (in a real app, use Alembic via CD)
    Base.metadata.create_all(bind=engine)
    yield
    # clean up here if needed

app = FastAPI(
    title="FLY.AI B3 Data Source API",
    description="Clean Architecture implementation of B3 Market Data Source",
    version="0.1.0",
    lifespan=lifespan
)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API and Domain Core operational"}

@app.post("/api/v1/sync/companies")
async def trigger_companies_sync(
    background_tasks: BackgroundTasks,
    use_case: SyncB3CompaniesUseCase = Depends(get_sync_b3_companies_use_case)
):
    """
    Triggers the background synchronization of B3 Companies.
    """
    # Run the data source fetch and DB operations in the background
    background_tasks.add_task(use_case.execute)
    
    return {
        "status": "accepted", 
        "message": "B3 Company synchronization started in the background."
    }
