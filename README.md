# FLY.AI B3 Data Source

A SOTA implementation of the FLY.AI data platform using a **Modular Monolith** pattern, **Domain-Driven Design (DDD)**, and **Hexagonal Architecture**.

## Architecture Overview

- **`src/shared`**: Shared kernel (base classes, infrastructure setup, utilities).
- **`src/companies`**: Bounded Context for company metadata and B3 scraping.
- **`src/financials`**: (Placeholder) Bounded Context for financial statements.
- **`src/market_data`**: (Placeholder) Bounded Context for external market APIs.

Each domain context follows **Hexagonal Architecture**:
- `domain/`: Pure business logic (Entities, Ports, Value Objects).
- `application/`: Use cases and orchestrators.
- `infrastructure/`: Adapters (DB, Scrapers, External APIs).
- `presentation/`: Entry points (FastAPI Routers, CLI).

## Principles
- **TDD First**: Strict Red-Green-Refactor cycle.
- **Container as SSOT**: A single Docker image for API, Workers, and Cron jobs.
- **KISS**: Focused on high cohesion and low coupling without microservice overhead.

## Development

### Setup
```bash
uv sync
```

### Running Tests
```bash
uv run pytest
```

### Running with Docker (SOTA)
```bash
docker compose up
```

## Technologies
- **Python 3.12**
- **FastAPI** (Presentation/BFF)
- **SQLAlchemy 2.0 + Pydantic V2**
- **Playwright** (Scraping)
- **Postgres 16**
- **uv** (Package Management)
