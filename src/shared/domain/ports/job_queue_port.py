from abc import ABC, abstractmethod
from typing import Any, Optional


class JobQueuePort(ABC):
    """Port for enqueueing background jobs, adhering to Hexagonal Architecture.

    Abstracts away the underlying message broker (ARQ, Celery, SQS, etc.),
    ensuring the Application and Domain layers remain framework-agnostic.
    """

    @abstractmethod
    async def enqueue(self, task_name: str, job_id: Optional[str] = None, **kwargs: Any) -> None:
        """Enqueues a task for background processing.

        Args:
            task_name (str): The constant name of the task to be executed.
            job_id (Optional[str]): Optional unique identifier for idempotency.
            **kwargs: Additional parameters to pass to the task.
        """
        pass
