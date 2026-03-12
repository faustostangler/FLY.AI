from contextlib import asynccontextmanager
from fastapi import FastAPI
from companies.presentation.api.routes import router as companies_router
from shared.infrastructure.database.connection import engine
from companies.infrastructure.adapters.database.models import Base

import logging
import os
from shared.infrastructure.config import settings

# --- Logic for Logging SOTA Configuration ---
os.makedirs(settings.app.log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(f"{settings.app.log_dir}/{settings.app.log_name}"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
# --------------------------------------------

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Ensure tables are created on startup 
    # (In a real scenario, use Alembic)
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title=settings.app.title,
    description="SOTA Finance Data Platform using DDD and Hexagonal Architecture",
    version=settings.app.version,
    lifespan=lifespan
)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "FLY.AI Core operational"}

# Register Domain Routers
app.include_router(companies_router, prefix="/api/v1")

# Future routers
# app.include_router(financials_router, prefix="/api/v1")
# app.include_router(market_data_router, prefix="/api/v1")
