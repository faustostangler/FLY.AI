# SOTA Dockerfile for FLY.AI Modular Monolith
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
WORKDIR /app

# Install system dependencies for Playwright and Postgres
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies first for caching
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    uv sync --frozen --no-install-project --no-dev

# Copy source code
COPY src/ /app/src/
COPY pyproject.toml uv.lock README.md /app/

# Install the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Runtime stage
FROM python:3.12-slim

WORKDIR /app

# Install runtime dependencies (libpq for psycopg2, and playwright deps)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy the virtualenv from the builder
COPY --from=builder /app/.venv /app/.venv

# Ensure we use the virtualenv
ENV PATH="/app/.venv/bin:$PATH"

# Install Playwright browsers (only chromium for now to keep it small)
RUN playwright install --with-deps chromium

# Copy the source code (in case some tools expect it outside venv)
COPY src/ /app/src/

# Default port
EXPOSE 8000

# Command will be overridden in docker-compose for different services
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
