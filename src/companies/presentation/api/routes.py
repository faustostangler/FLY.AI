from fastapi import APIRouter, Depends, BackgroundTasks
from src.companies.application.use_cases.sync_b3_companies import SyncB3CompaniesUseCase
from src.companies.presentation.api.dependencies import get_sync_b3_companies_use_case

router = APIRouter(prefix="/companies", tags=["Companies"])

@router.post("/sync")
async def trigger_companies_sync(
    background_tasks: BackgroundTasks,
    use_case: SyncB3CompaniesUseCase = Depends(get_sync_b3_companies_use_case)
):
    """
    Triggers the background synchronization of B3 Companies.
    """
    background_tasks.add_task(use_case.execute)
    
    return {
        "status": "accepted", 
        "message": "B3 Company synchronization started in the background."
    }
