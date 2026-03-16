import datetime
import structlog

from shared.domain.ports.job_queue_port import JobQueuePort
from shared.infrastructure.queue.task_names import TaskNames

logger = structlog.get_logger().bind(bounded_context="companies")


class TriggerB3SyncUseCase:
    """Use Case to orchestrate the triggering of B3 synchronization process.
    
    Encapsulates the domain logic for idempotency (allowing only one sync per day),
    and decouples the presentation layer from the infrastructure queueing details.
    """

    def __init__(self, job_queue: JobQueuePort):
        self._job_queue = job_queue

    async def execute(self, reference_date: datetime.date) -> None:
        """Triggers the background B3 Sync job, enforcing daily idempotency.
        
        Args:
            reference_date (datetime.date): The logic-bounded date used for idempotency tracking.
        """
        # Domain rule for idempotency: one B3 sync per day
        day_id = reference_date.strftime("%Y-%m-%d")
        job_id = f"sync_b3_{day_id}"
        
        logger.info("Triggering B3 Sync job in background", job_id=job_id)
        
        await self._job_queue.enqueue(
            task_name=TaskNames.SYNC_B3_COMPANIES,
            job_id=job_id
        )
