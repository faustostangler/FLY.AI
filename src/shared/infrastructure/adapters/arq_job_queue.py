from typing import Any, Optional
from shared.domain.ports.job_queue_port import JobQueuePort
from shared.infrastructure.queue.connection import get_arq_redis_pool


class ArqJobQueueAdapter(JobQueuePort):
    """Secondary Adapter: Implements the JobQueuePort using ARQ (Redis)."""

    async def enqueue(self, task_name: str, job_id: Optional[str] = None, **kwargs: Any) -> None:
        """Enqueues the job into the ARQ Redis pool.
        
        Args:
            task_name (str): Task identifier.
            job_id (Optional[str]): Used for determining idempotency (preventing duplicate jobs).
        """
        redis_queue = await get_arq_redis_pool()
        
        enqueue_kwargs = {}
        if job_id:
            enqueue_kwargs["_job_id"] = job_id
            
        await redis_queue.enqueue_job(task_name, **enqueue_kwargs, **kwargs)
