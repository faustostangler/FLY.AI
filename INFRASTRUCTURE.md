# FLY.AI Infrastructure and Operations

This document summarizes the infrastructure, persistence, access, and operational procedures for the FLY.AI project.

## 1. Docker Architecture and Dockerfile

The project follows the "Single Source of Truth" principle, where the same Docker image is used for various roles (API and Workers).

- **Build Base**: `ghcr.io/astral-sh/uv:python3.12-bookworm-slim` (builder) and `python:3.12-slim` (runtime).
- **Dependency Management**: `uv` for ultra-fast and deterministic installations.
- **Service Roles**:
  - `api`: FastAPI server running via `uvicorn`.
  - `worker-companies`: CLI interface for background synchronization tasks.
- **Scraper**: Playwright (chromium) installed with all necessary dependencies in the runtime stage.

## 2. Storage and Volumes (Persistence)

The project adheres to SOTA practices by using **Managed Docker Volumes** for all databases and infrastructure data. This ensures high performance (optimized for the host OS), data security (protected within `/var/lib/docker/volumes`), and OS abstraction.

| Service | Volume Type | Host Source | Container Path |
| :--- | :--- | :--- | :--- |
| **PostgreSQL** | Managed Volume | `postgres-data` | `/var/lib/postgresql/data` |
| **Redis** | Managed Volume | `redis-data` | `/data` |
| **pgAdmin** | Managed Volume | `pgadmin-data` | `/var/lib/pgadmin` |
| **Prometheus**| Managed Volume | `prometheus-data` | `/prometheus` |
| **Grafana** | Managed Volume | `grafana-data` | `/var/lib/grafana` |

> [!NOTE]
> **Bind Mounts** are exclusively used for local configuration files (e.g., `./monitoring/prometheus/prometheus.yml`) to allow immediate updates without rebuilding volumes.

## 3. Access, Endpoints, and URLs

### Infrastructure Services
- **PostgreSQL (`db`)**:
  - **Internal URL**: `postgresql://postgres:postgres@db:5432/flyai_b3`
  - **External Access**: `localhost:5432`
  - **Credentials**: User: `postgres` | Pass: `postgres` | DB: `flyai_b3`
- **Redis (`redis`)**:
  - **Internal URL**: `redis://redis:6379/0`
  - **External Access**: `localhost:6379`
- **pgAdmin (DB Dashboard)**:
  - **URL**: `http://localhost:5050`
  - **Login**: `admin@fly.ai` | **Password**: `admin`

### Monitoring and Observability
- **Prometheus**:
  - **URL**: `http://localhost:9090`
  - **Scrape Target**: Monitors `api:8000`.
- **Grafana**:
  - **URL**: `http://localhost:3000`
  - **Credentials**: `admin` / `admin` (Automatically provisioned).

### Application (API)
- **Local Proxy URL**: `http://localhost:8001`
- **Swagger UI**: `http://localhost:8001/docs`
- **Container Port**: `8000`

## 4. Operational Commands (Getting Started)

### Environment Setup
To synchronize dependencies and ensure the environment is ready:
```bash
uv sync
```

### Starting the Infrastructure (Docker)
To start all services in detached mode:
```bash
docker-compose up -d
```
To view logs:
```bash
docker-compose logs -f
```

### Running the API Locally
To run the web server with hot-reload for development:
```bash
uv run uvicorn src.main:app --reload --port 8000
```

### Running CLI Tools
Example command to sync companies (runs within the local env):
```bash
uv run python -m src.shared.presentation.cli sync-companies
```

### Testing Strategy
**Standard Tests (Pytest)**:
Ensures core domain and infrastructure functionality.
```bash
uv run pytest
```

**Mutation Testing (Mutmut)**:
Verifies test suite effectiveness by mutating source code.
```bash
uv run mutmut run
```
To view results:
```bash
uv run mutmut show all
```

## 5. Application Configuration (Pydantic)

The system centralizes all configuration in `src/shared/infrastructure/config.py` using Pydantic V2.

- **Environment Injection**: Uses `pydantic-settings` to load `.env` files.
- **Nested Mapping**: Uses double underscores (`__`) in environment variables for nested class mapping. 
  - *Example*: `DB__URL` maps to `settings.db.url`.
- **Singleton**: The `settings` object is exported for use across the entire Domain and Infrastructure layers.
