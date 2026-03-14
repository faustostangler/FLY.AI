# FLY.AI SOTA Makefile
# Automation for Modular Monolith Orchestration

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
	@echo "setup     : Initial environment setup (uv sync, pull images)"
	@echo "up        : Start services (respects COMPOSE_PROFILES in .env)"
	@echo "down      : Stop and remove containers"
	@echo "ps        : List running services"
	@echo "logs      : Tail all logs"
	@echo "shell     : Open a shell in the API container"
	@echo "sync      : Run the B3 company synchronization worker"
	@echo "build     : Rebuild core images"

setup:
	uv sync
	docker compose pull

up:
	docker compose up -d

down:
	docker compose down

ps:
	docker compose ps

logs:
	docker compose logs -f

shell:
	docker compose exec api /bin/bash

sync:
	docker compose run --rm worker

build:
	docker compose build
