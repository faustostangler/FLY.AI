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
	@echo "build      : Build core local images"
	@echo "rebuild    : Rebuild core local images"
	@echo "setup      : Initial environment setup (uv sync, pull images)"
	@echo "up         : Start Universal Foundation (API, Worker, DB, Cache)"
	@echo "up-worker  : Start ONLY the Worker + dependencies (Scale-Out/Staging mode)"
	@echo "up-admin   : Start Foundation + db-admin (pgAdmin)"
	@echo "up-obs     : Start Foundation + observability (Prometheus & Grafana)"
	@echo "sync       : Run a one-off synchronization task"
	@echo "ps         : List running services"
	@echo "logs       : Tail all logs"
	@echo "shell      : Open a shell in the API container"
	@echo "shell-work : Open a shell in the Worker container"
	@echo "down       : Stop and remove all containers"
	@echo "down-force : Stop and remove all containers (force)"
	@echo "destroy-v  : Destroy all volumes"
	@echo "destroy-im : Destroy all images"
	@echo "destroy-all: Destroy all containers and volumes"


build:
	docker compose build

rebuild:
	docker compose build --no-cache

setup:
	uv sync
	docker compose pull --ignore-buildable
	docker compose build

up:
	docker compose --profile "*" down
	docker compose up -d

up-worker:
	docker compose --profile "*" down
	docker compose up -d worker

up-admin:
	docker compose --profile "*" down
	COMPOSE_PROFILES=admin docker compose up -d

up-obs:
	docker compose --profile "*" down
	COMPOSE_PROFILES=observability docker compose up -d

sync:
	docker compose --profile "*" down
	docker compose run --rm worker

ps:
	docker compose ps

logs:
	docker compose logs -f

shell:
	docker compose exec api /bin/bash

shell-work:
	docker compose exec worker /bin/bash

down:
	docker compose down

down-force:
	docker compose --profile "*" down

destroy-v:
	docker compose --profile "*" down -v

destroy-im:
	docker compose --profile "*" down -v --rmi all

destroy-all:
	docker compose --profile "*" down -v --rmi all --remove-orphans
	docker system prune -a -f
