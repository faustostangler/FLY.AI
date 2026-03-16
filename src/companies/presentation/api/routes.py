import datetime
from fastapi import APIRouter
from shared.presentation.api.route_classes import SRETelemetryRoute
from shared.infrastructure.queue.connection import get_arq_redis_pool
from shared.infrastructure.queue.task_names import TaskNames

router = APIRouter(prefix="/companies", tags=["Companies"], route_class=SRETelemetryRoute)

@router.post("/sync", status_code=202)
async def trigger_companies_sync():
    """Triggers an asynchronous synchronization with the B3 market catalog.

    Synchronization is a high-latency I/O operation (scraping thousands
    of issuers). We use the ARQ redis job queue to process it off the 
    main API resources, protecting against OOM exceptions.
    
    Idempotent logic relies on job UUID tracking by Day.

    Returns:
        dict: A notification that the task has been accepted.
    """
    redis_queue = await get_arq_redis_pool()
    day_id = datetime.datetime.utcnow().strftime("%Y-%m-%d")
    
    await redis_queue.enqueue_job(
        TaskNames.SYNC_B3_COMPANIES,
        _job_id=f"sync_b3_{day_id}"
    )

    return {
        "status": "accepted",  # pragma: no mutate
        "message": "B3 Company synchronization started in the background via ARQ.",  # pragma: no mutate
    }
