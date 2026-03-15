from fastapi import APIRouter, Depends, BackgroundTasks
from companies.application.use_cases.sync_b3_companies import SyncB3CompaniesUseCase
from companies.presentation.api.dependencies import get_sync_b3_companies_use_case

router = APIRouter(prefix="/companies", tags=["Companies"])

@router.post("/sync", status_code=202)
async def trigger_companies_sync(
    background_tasks: BackgroundTasks,
    use_case: SyncB3CompaniesUseCase = Depends(get_sync_b3_companies_use_case)
):
    """Triggers an asynchronous synchronization with the B3 market catalog.

    Synchronization is a high-latency I/O operation (scraping thousands 
    of issuers). We use FastAPI's BackgroundTasks to accept the request 
    immediately and process it off the main request-response cycle, 
    preventing timeouts and blocking the event loop.

    Returns:
        dict: A notification that the task has been accepted.
    """
    background_tasks.add_task(use_case.execute)
    
    return {
        "status": "accepted",  # pragma: no mutate
        "message": "B3 Company synchronization started in the background."  # pragma: no mutate
    }
