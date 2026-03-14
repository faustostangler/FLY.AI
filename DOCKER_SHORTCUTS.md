# FLY.AI Docker Quick Reference

Quick guide for orchestration, monitoring, and debugging the project infrastructure.

## Project Lifecycle (via Makefile)

| Command | Action |
| :--- | :--- |
| `make setup` | Initial setup (Sync dependencies & Build images) |
| `make up` | Start Foundation (Core + Active Profiles) |
| `make up-admin` | Start Core + pgAdmin |
| `make up-obs` | Start Core + Observability (Prometheus/Grafana) |
| `make up-worker`| Start ONLY the Worker + dependencies |
| `make build` | Build/Rebuild images |
| `make rebuild` | Force rebuild images (no-cache) |
| `make sync` | Run a one-off synchronization task |
| `make down` | Stop all active services |

---

## Inspection & Monitoring

### Status and Ports
```bash
# General status, ports, and health
make ps

# Detailed status with specific columns
make ps-format
```

### Logging
```bash
# Tail all logs
make logs

# Logs for a specific service
make logs-api
make logs-worker
make logs-db
```

### Profile Status
```bash
# Since we use modular environments, checking profiles is done by looking at the profile.env file:
cat .env/profile.env
```

---

## Interactive Access

| Target | Command |
| :--- | :--- |
| **API Shell** | `make shell` |
| **Worker Shell** | `make shell-work` |
| **Database (CLI)** | `make db-cli` |
| **Redis (CLI)** | `make cache-cli` |

---

## Connectivity Map (Local Access)

| Service | Port (Host) | Access URL |
| :--- | :--- | :--- |
| **BFF / API Swagger** | `8001` | [http://localhost:8001/docs](http://localhost:8001/docs) |
| **API Health** | `8001` | [http://localhost:8001/health](http://localhost:8001/health) |
| **API Metrics** | `8001` | [http://localhost:8001/metrics](http://localhost:8001/metrics) |
| **pgAdmin** | `5050` | [http://localhost:5050](http://localhost:5050) |
| **Grafana** | `3000` | [http://localhost:3000](http://localhost:3000) |
| **Prometheus** | `9090` | [http://localhost:9090](http://localhost:9090) |
| **PostgreSQL**| `5432` | `localhost:5432` |
| **Redis** | `6379` | `localhost:6379` |

---

## API Endpoints Reference

All application routes are prefixed with `/api/v1` except for system endpoints.

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/health` | Service health status |
| **GET** | `/metrics` | Prometheus metrics scrape point |
| **POST** | `/api/v1/companies/sync` | Trigger background B3 company sync |

---

## Maintenance & Cleanup

### Selective Reset
```bash
# Stop and remove all containers (force cleanup)
make down-force

# Restart a single container
make restart-api
make restart-worker
```

### Deep Cleanup (Destruction)
> [!CAUTION]
> Destroy commands are destructive. **destroy-v** and above will erase your Database and Redis data.

| Command | Scope |
| :--- | :--- |
| `make destroy-v` | Removes containers + named volumes (Erase DB data) |
| `make destroy-im` | Removes containers + volumes + images |
| `make destroy-all` | Full wipe + Docker system prune -a (The Nuclear Option) |

---

## Docker Daemon Hard Reset (System Level)

> [!WARNING]
> These commands affect the entire Docker engine on the host, not just this project.

```bash
# Stop Docker engine and its socket
sudo systemctl stop docker.socket
sudo systemctl stop docker

# Wipe ancient Docker structure on the D drive (Data Root)
sudo rm -rf /mnt/linux_d/docker

# Reload daemon configurations and restart engine
sudo systemctl daemon-reload
sudo systemctl start docker
```
