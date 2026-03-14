from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

from shared.infrastructure.config import settings

engine = create_engine(
    settings.db.url,
    connect_args={"connect_timeout": settings.db.connection_timeout}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
