from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# Hardcoded for initial setup to test DB Locally.
# The user's goal is to move to CloudNativePG. We use local postgres container.
# Make sure to set these up in env vars eventually.
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/flyai_b3"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
