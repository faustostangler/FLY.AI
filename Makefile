# FLY.AI Makefile
# SOTA Modular Orchestration

.PHONY: setup up down ps ps-format logs shell test sync help db-cli cache-cli

# --- Zero-Touch Modular Environment Loading ---
ENV_FILES := $(wildcard .envs/*.env)

# Load into Make context for variable expansion
include $(ENV_FILES)
export

# Centralized Docker Compose command with Explicit Env Matrix
DC := docker compose $(foreach file,$(ENV_FILES),--env-file $(file))

# --------------------------------------------

help:
	@echo "FLY.AI Modular Operations"
	@echo "-------------------------"
	@echo "Available Env Files: $(ENV_FILES)"
	@echo ""
	@echo "build      : Build core local images"
	@echo "rebuild    : Rebuild core local images"
	@echo "setup      : Initial environment setup (uv sync, pull images)"
	@echo "up         : Start Foundation (All Modular env)"
	@echo "up-worker  : Start ONLY the Worker + deps"
	@echo "up-admin   : Start Foundation + pgAdmin"
	@echo "up-obs     : Start Foundation + observability"
	@echo "sync       : Run a one-off synchronization task"
	@echo "ps         : List services"
	@echo "logs       : Tail logs"
	@echo "shell      : Open a shell in the API container"
	@echo "shell-work : Open a shell in the Worker container"
	@echo "down       : Stop all"
	@echo "down-force : Stop and remove all containers (force)"
	@echo "destroy-v  : Destroy all volumes"
	@echo "destroy-im : Destroy all images"
	@echo "destroy-all: Destroy all containers and volumes"

build:
	$(DC) build

rebuild:
	$(DC) build --no-cache

setup:
	uv sync
	$(DC) pull --ignore-buildable
	$(DC) build

up:
	$(DC) --profile "*" down
	$(DC) up -d

up-worker:
	$(DC) --profile "*" down
	$(DC) up -d worker

up-admin:
	$(DC) --profile "*" down
	COMPOSE_PROFILES=admin $(DC) up -d

up-obs:
	$(DC) --profile "*" down
	COMPOSE_PROFILES=observability $(DC) up -d

sync:
	$(DC) --profile "*" down
	$(DC) run --rm worker

ps:
	$(DC) ps

ps-format:
	$(DC) ps --format "table {{.Name}}\t{{.Status}}\t{{.Ports}}"

logs:
	$(DC) logs -f

shell:
	$(DC) exec api /bin/bash

shell-work:
	$(DC) exec worker /bin/bash

down:
	$(DC) down

down-force:
	$(DC) --profile "*" down

destroy-v:
	$(DC) --profile "*" down -v

destroy-im:
	$(DC) --profile "*" down -v --rmi all

destroy-all:
	$(DC) --profile "*" down -v --rmi all --remove-orphans
	docker system prune -a -f

restart-%:
	$(DC) restart $*

logs-%:
	$(DC) logs -f $*

exec-%:
	$(DC) exec $* /bin/bash

db-cli:
	$(DC) exec db psql -U user_stangler -d fly_b3

cache-cli:
	$(DC) exec cache redis-cli
