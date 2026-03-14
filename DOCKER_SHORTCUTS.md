# FLY.AI Docker Quick Reference 🚀

Quick guide for orchestration, monitoring, and debugging the project infrastructure.

## 🛠 Project Lifecycle (via Makefile)

| Command | Action |
| :--- | :--- |
| `make setup` | Initial setup (Sync dependencies & Build images) |
| `make up` | Start Core services (API, DB, Cache) |
| `make up-admin` | Start Core + **pgAdmin** (DB Dashboard) |
| `make up-obs` | Start Core + **Observability** (Grafana/Prometheus) |
| `make build` | Build/Rebuild images |
| `make rebuild` | Force rebuild images **without cache** |
| `make down` | Stop and remove all containers |

---

## 🔍 Inspection & Monitoring

### Status and Ports
```bash
# General status, ports, and health
docker compose ps

# Table view with specific columns
docker compose ps --format "table {{.Name}}\t{{.Status}}\t{{.Ports}}"
```

### Logging
```bash
# Tail all logs
make logs

# Logs for a specific service
docker compose logs -f api
docker compose logs -f db
```

### Profile Status
```bash
# See which profiles are currently enabled in .env
docker compose config --profiles
```

---

## 💻 Interactive Access

| Target | Command |
| :--- | :--- |
| **API Shell** | `make shell` |
| **Worker Shell** | `make shell-work` |
| **Database (CLI)** | `docker compose exec db psql -U fly_user_stangler -d fly_b3` |
| **Redis (CLI)** | `docker compose exec cache redis-cli` |

---

## 🌐 Connectivity Map (Local Access)

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

## 🛣 API Endpoints Reference

All application routes are prefixed with `/api/v1` except for system endpoints.

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **GET** | `/health` | Service health status |
| **GET** | `/metrics` | Prometheus metrics scrape point |
| **POST** | `/api/v1/companies/sync` | Trigger background B3 company sync |

---

## 🧹 Maintenance & Cleanup

### Force Restart a Single Container
```bash
docker compose restart api
```

### Critical Reset (Delete Volumes & Data)
> [!CAUTION]
> This will erase your Database and Redis data. Use only if needed.
```bash
docker compose down -v
```

### Full System Cleanup (Prune)
```bash
# Removes unused images and data
docker system prune -a --volumes
```
