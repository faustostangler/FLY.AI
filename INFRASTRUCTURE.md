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
| **PostgreSQL** | Managed Volume | `db-data` | `/var/lib/postgresql` |
| **Redis** | Managed Volume | `cache-data` | `/data` |
| **pgAdmin** | Managed Volume | `db-admin-data` | `/var/lib/pgadmin` |
| **Prometheus**| Managed Volume | `metrics-data` | `/prometheus` |
| **Grafana** | Managed Volume | `observability-data` | `/var/lib/grafana` |
| **Tempo**   | Managed Volume | `traces-data` | `/var/tempo` |
| **Alertmanager** | Managed Volume | `alertmanager-data` | `/alertmanager` |

> [!NOTE]
> **Bind Mounts** are exclusively used for local configuration files (e.g., `./monitoring/prometheus/prometheus.yml`) to allow immediate updates without rebuilding volumes.

## 3. Access, Endpoints, and URLs

### Infrastructure Services
- **PostgreSQL (`db`)**:
  - **Internal URL**: `postgresql://${DB__USER}:${DB__PASSWORD}@db:5432/${DB__NAME}`
  - **External Access**: `localhost:5432`
  - **Credentials**: User: `${DB__USER}` | Pass: `${DB__PASSWORD}` | DB: `${DB__NAME}`
- **Redis (`cache`)**:
  - **Internal URL**: `redis://cache:6379/0`
  - **External Access**: `localhost:6379`
- **pgAdmin (DB Dashboard)**:
  - **URL**: `http://localhost:5050`
  - **Login**: `${DB_ADMIN_EMAIL}` | **Password**: `${DB_ADMIN_PASSWORD}`

### Monitoring and Observability
- **Prometheus**:
  - **URL**: `http://localhost:9090`
  - **Scrape Target**: Monitors `api:8000`.
- **Grafana**:
  - **URL**: `http://localhost:3000`
  - **Credentials**: `admin` / `${OBSERVABILITY_PASSWORD}` (Automatically provisioned).
- **Grafana Tempo (Traces)**:
  - **URL**: `http://localhost:3200` (API) | **OTLP**: `4317` (gRPC) / `4318` (HTTP).
- **Alertmanager**:
  - **URL**: `http://localhost:9093`
  - **Status**: Monitors and routes alerts from Prometheus.

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

## 6. SRE Culture and Distributed Tracing (SOTA)

The project implements a full SRE stack for high reliability and rapid diagnosis:

### Distributed Tracing (OpenTelemetry)
- **Auto-Instrumentation**: FastAPI and SQLAlchemy are automatically instrumented. No tracing code in the Domain layer.
- **Backend**: Grafana Tempo stores spans for 48h (dev).
- **Correlation**: Logs in Loki include `trace_id`. Clicking a `trace_id` in Grafana takes you directly to the full distributed trace.

### Proactive Alerting
- **Golden Signals**: Alerts are based on Latency (P95/P99), Traffic anomalies, Error Rates (5xx), and Saturation.
- **Business SLIs**: Domain-specific alerts notify the team if the B3 Sync fails or if Rate Limits are hit.
- **Routing**: Alertmanager groups and routes alerts to avoid "alert fatigue", with inhibition rules for noise reduction.

