# FLY.AI B3 Data Source

A SOTA implementation of the FLY.AI data platform using a **Modular Monolith** pattern, **Domain-Driven Design (DDD)**, and **Hexagonal Architecture**. This project gathers financial documents and market data from companies listed on the B3 stock exchange.

## Core Features (System Capabilities)

The system is designed to automate the entire lifecycle of financial data ingestion:

1.  **Company Data Scraping**: Automatic discovery of company names, tickers, sectors, and registration data (CNPJs).
2.  **Financial Reports Processing**: Extraction and standardization of company financial statements (ITR/DFP).
3.  **NSD (Document Number) Tracking**: Intelligent tracking of financial disclosure sequences to ensure no data is missed.
4.  **Market & Corporate Events**: Integration with stock prices, splits, and dividend information (Aggregated through Bounded Contexts).
5.  **High-Performance Ingestion**: Concurrent processing using Playwright with persistent sessions and headless/headful optimization.

## System Architecture

### Modular Monolith Structure
The project is organized into Bounded Contexts to maintain high cohesion and low coupling:

- **`src/shared`**: The Shared Kernel. Contains base classes, Pydantic configuration, monitoring (Prometheus), and infrastructure utilities.
- **`src/companies`**: (**Migrated**) Manages company metadata, B3 scraping, and repository persistence.
- **`src/financials`**: (**Future**) Focused on financial statements extraction and parsing.
- **`src/market_data`**: (**Future**) Integration with tickers, prices, and external market APIs.

### Hexagonal Layers (Internal)
Each module follows a strict Hexagonal Architecture:
- `domain/`: Pure business logic (Entities, Value Objects, Ports). Framework agnostic.
- `application/`: Use cases, orchestrators, and application services.
- `infrastructure/`: Adapters (PostgreSQL, Playwright Scrapers, Redis Cache).
- `presentation/`: Entry points including FastAPI Routers (REST API) and CLI tools.

## System Services

Services are the main entry points for data operations. Currently, migration from the legacy system is in progress:

- `sync-companies`: (**Active**) Discover and synchronize company listings from B3.
- `sync-nsd`: (*Planned*) Retrieve sequential document disclosure information.
- `fetch-statements`: (*Planned*) Download raw financial statement pages.
- `parse-statements`: (*Planned*) Convert raw data into structured financial records.

## Quick Start

### 1. Environment Setup
The project uses `uv` for lightning-fast dependency management.
```bash
uv sync
```

### 2. Infrastructure & Services
To start the database (PostgreSQL), cache (Redis), and observability stack (Prometheus/Grafana):
```bash
docker compose up -d
```

### 3. Execution
- **Web API**: `uv run uvicorn src.main:app --reload`
- **CLI Sync**: `uv run python -m src.shared.presentation.cli sync-companies`
- **Tests**: `uv run pytest`
- **Mutation Analysis**: `uv run mutmut run`

---

## Documentation & Observability

- **[Infrastructure Guide](INFRASTRUCTURE.md)**: Deep dive into volumes, networking, and docker roles.
- **API Docs**: `http://localhost:8001/docs` (when running).
- **Monitoring**: Grafana (`:3000`, creds: `admin` / `${OBSERVABILITY_PASSWORD}`) and Prometheus (`:9090`).

## Technologies

- **Python 3.12**
- **FastAPI**: Presentation Layer / BFF.
- **SQLAlchemy 2.0 + Pydantic V2**: Modern data modeling and validation.
- **Playwright**: Resilient browser automation for scraping.
- **Postgres 16 + Redis 7**: Robust persistence and caching.
- **uv**: Rust-based package and environment management.
- **Prometheus + Grafana**: Infrastructure and Business metrics (Golden Signals).

## License

This project is licensed under the MIT License.

---
"Inspired by the Pampas and crafted with yerba mate in South America: an authentic gaucho product."
