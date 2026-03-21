from typing import AsyncGenerator
from sqlalchemy import event
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from shared.infrastructure.config import settings
from shared.infrastructure.monitoring import metrics


# Initialize the SQLAlchemy Async Engine.
# Using asyncpg driver for high-performance, non-blocking I/O.
# Standardizing the connection lifecycle and timeouts ensures that the
# application doesn't hang indefinitely on network partitions.
engine = create_async_engine(
    settings.db.url, 
    connect_args={"timeout": settings.db.connection_timeout},
    pool_pre_ping=True,
    future=True
)

# Shared Async Session Factory for consistent persistence behavior across the system.
# Using expire_on_commit=False is a best practice for async sessions to prevent
# accidental I/O when accessing attributes after commit.
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
)


# --- SRE Instrumentation: Database Pool Saturation ---
# Injetamos listeners para rastrear o estado real do pool de conexões.
# Isso permite detectar vazamentos de conexão antes que causem um Incidente (OOM/Max Connections).
# Note: For AsyncEngine, we must attach listeners to the underlying sync_engine.
@event.listens_for(engine.sync_engine, "checkout")
def receive_checkout(dbapi_connection, connection_record, connection_proxy):
    """Increments metric when a connection is retrieved from the pool for use."""
    metrics.DB_CONNECTIONS_ACTIVE.labels(database="postgres").inc()


@event.listens_for(engine.sync_engine, "checkin")
def receive_checkin(dbapi_connection, connection_record):
    """Decrements metric when a connection returns to the pool (available)."""
    metrics.DB_CONNECTIONS_ACTIVE.labels(database="postgres").dec()
# ----------------------------------------------------


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Provides an asynchronous transactional scope for database operations.

    This generator ensures that every unit of work has its own
    isolated async session, which is guaranteed to be closed after the
    request/operation completes, preventing connection leaks.

    Yields:
        AsyncSession: An active SQLAlchemy async session.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            # Closure is handled by the context manager 'async with'.
            await session.close()
