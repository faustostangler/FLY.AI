from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from shared.infrastructure.config import settings

# Initialize the SQLAlchemy Engine.
# Standardizing the connection lifecycle and timeouts ensures that the
# application doesn't hang indefinitely on network partitions.
engine = create_engine(
    settings.db.url, connect_args={"connect_timeout": settings.db.connection_timeout}
)

# Shared Session Factory for consistent persistence behavior across the system.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
from typing import Annotated
from typing import Callable
from typing import ClassVar

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


def get_db():
    args = []  # type: ignore
    kwargs = {}  # type: ignore
    return _mutmut_trampoline(
        x_get_db__mutmut_orig, x_get_db__mutmut_mutants, args, kwargs, None
    )


def x_get_db__mutmut_orig():
    """Provides a transactional scope for database operations.

    This generator ensures that every unit of work has its own
    isolated session, which is guaranteed to be closed after the
    request/operation completes, preventing connection leaks.

    Yields:
        Session: An active SQLAlchemy database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        # Guarantee closure to return the connection to the pool.
        db.close()


def x_get_db__mutmut_1():
    """Provides a transactional scope for database operations.

    This generator ensures that every unit of work has its own
    isolated session, which is guaranteed to be closed after the
    request/operation completes, preventing connection leaks.

    Yields:
        Session: An active SQLAlchemy database session.
    """
    db = None
    try:
        yield db
    finally:
        # Guarantee closure to return the connection to the pool.
        db.close()


x_get_db__mutmut_mutants: ClassVar[MutantDict] = {  # type: ignore
    "x_get_db__mutmut_1": x_get_db__mutmut_1
}
x_get_db__mutmut_orig.__name__ = "x_get_db"
