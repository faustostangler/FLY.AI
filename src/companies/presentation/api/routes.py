import datetime
from fastapi import APIRouter, Depends
from shared.presentation.api.route_classes import SRETelemetryRoute
from companies.application.use_cases.trigger_b3_sync import TriggerB3SyncUseCase
from companies.presentation.api.dependencies import get_trigger_b3_sync_use_case

router = APIRouter(prefix="/companies", tags=["Companies"], route_class=SRETelemetryRoute)

@router.post("/sync", status_code=202)
async def trigger_companies_sync(
    use_case: TriggerB3SyncUseCase = Depends(get_trigger_b3_sync_use_case)
):
    """Triggers an asynchronous synchronization with the B3 market catalog.

    Synchronization is a high-latency I/O operation (scraping thousands
    of issuers). We use a domain Use Case interface which abstracts the Message Broker,
    acting as the starting boundary of the Application layer logic.

    Returns:
        dict: A notification that the task has been accepted.
    """
    await use_case.execute(reference_date=datetime.datetime.utcnow().date())

    return {
        "status": "accepted",  # pragma: no mutate
        "message": "B3 Company synchronization started in the background.",  # pragma: no mutate
    }
