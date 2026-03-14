# FLY.AI Makefile
# SOTA Modular Orchestration

.PHONY: setup up down ps logs shell test sync help

# --- Zero-Touch Modular Environment Loading ---
ENV_FILES := $(wildcard .env/*.env)

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
	@echo "up         : Start Foundation (All Modular env)"
	@echo "up-worker  : Start ONLY the Worker + deps"
	@echo "up-admin   : Start Foundation + pgAdmin"
	@echo "ps         : List services"
	@echo "logs       : Tail logs"
	@echo "down       : Stop all"

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
