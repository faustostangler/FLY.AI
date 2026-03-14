# FLY.AI Makefile
# Automation for Orchestration

.PHONY: setup up down ps logs shell test sync help

# Load environment variables
ifneq (,$(wildcard .env))
    include .env
    export
endif

# Help command to list available targets
help:
	@echo "FLY.AI SOTA Operations"
	@echo "----------------------"
	@echo "setup      : Initial environment setup (uv sync, pull images)"
	@echo "up         : Start Universal Foundation (API, Worker, DB, Cache)"
	@echo "up-worker  : Start ONLY the Worker + dependencies (Scale-Out/Staging mode)"
	@echo "up-admin   : Start Foundation + db-admin (pgAdmin)"
	@echo "up-obs     : Start Foundation + observability (Prometheus & Grafana)"
	@echo "down       : Stop and remove all containers"
	@echo "ps         : List running services"
	@echo "logs       : Tail all logs"
	@echo "shell      : Open a shell in the API container"
	@echo "shell-work : Open a shell in the Worker container"
	@echo "sync       : Run a one-off synchronization task"
	@echo "build      : Rebuild core local images"


setup:
	uv sync
	docker compose pull --ignore-buildable
	docker compose build

up:
	docker compose up -d

up-worker:
	docker compose up -d worker

up-admin:
	COMPOSE_PROFILES=admin docker compose up -d

up-obs:
	COMPOSE_PROFILES=observability docker compose up -d

down:
	docker compose down

ps:
	docker compose ps

logs:
	docker compose logs -f

shell:
	docker compose exec api /bin/bash

shell-work:
	docker compose exec worker /bin/bash

sync:
	docker compose run --rm worker

build:
	docker compose build
