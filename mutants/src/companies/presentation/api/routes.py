from fastapi import APIRouter, Depends, BackgroundTasks
from companies.application.use_cases.sync_b3_companies import SyncB3CompaniesUseCase
from companies.presentation.api.dependencies import get_sync_b3_companies_use_case

router = APIRouter(prefix="/companies", tags=["Companies"])
from typing import Annotated
from typing import Callable

MutantDict = Annotated[dict[str, Callable], "Mutant"]  # type: ignore


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg=None):  # type: ignore
    """Forward call to original or mutated function, depending on the environment"""
    import os  # type: ignore

    mutant_under_test = os.environ["MUTANT_UNDER_TEST"]  # type: ignore
    if mutant_under_test == "fail":  # type: ignore
        from mutmut.__main__ import MutmutProgrammaticFailException  # type: ignore

        raise MutmutProgrammaticFailException("Failed programmatically")  # type: ignore
    elif mutant_under_test == "stats":  # type: ignore
        from mutmut.__main__ import record_trampoline_hit  # type: ignore

        record_trampoline_hit(orig.__module__ + "." + orig.__name__)  # type: ignore
        # (for class methods, orig is bound and thus does not need the explicit self argument)
        result = orig(*call_args, **call_kwargs)  # type: ignore
        return result  # type: ignore
    prefix = orig.__module__ + "." + orig.__name__ + "__mutmut_"  # type: ignore
    if not mutant_under_test.startswith(prefix):  # type: ignore
        result = orig(*call_args, **call_kwargs)  # type: ignore
        return result  # type: ignore
    mutant_name = mutant_under_test.rpartition(".")[-1]  # type: ignore
    if self_arg is not None:  # type: ignore
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)  # type: ignore
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)  # type: ignore
    return result  # type: ignore


@router.post("/sync", status_code=202)
async def trigger_companies_sync(
    background_tasks: BackgroundTasks,
    use_case: SyncB3CompaniesUseCase = Depends(get_sync_b3_companies_use_case),
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
        "message": "B3 Company synchronization started in the background.",  # pragma: no mutate
    }
