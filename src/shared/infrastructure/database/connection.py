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


def get_db():
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
