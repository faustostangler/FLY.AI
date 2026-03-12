from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.companies.presentation.api.routes import router as companies_router
from src.shared.infrastructure.database.connection import engine
from src.companies.infrastructure.adapters.database.models import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Ensure tables are created on startup 
    # (In a real scenario, use Alembic)
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    title="FLY.AI Modular Monolith",
    description="SOTA Finance Data Platform using DDD and Hexagonal Architecture",
    version="0.2.0",
    lifespan=lifespan
)

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Modular Monolith Core operational"}

# Register Domain Routers
app.include_router(companies_router, prefix="/api/v1")

# Future routers
# app.include_router(financials_router, prefix="/api/v1")
# app.include_router(market_data_router, prefix="/api/v1")
