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
FROM python:3.12-slim AS runtime

WORKDIR /app

# 1. Set Playwright path and Create User EARLY
ENV PLAYWRIGHT_BROWSERS_PATH=/app/pw-browsers
RUN useradd -m appuser && chown appuser:appuser /app

# Install runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 2. Optimized COPY: Ownership set during file transfer
COPY --from=builder --chown=appuser:appuser /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# 3. Switch to User BEFORE heavy installs
USER appuser

# Install Playwright browsers as non-root (faster, safer)
RUN playwright install chromium

# Copy the source code as appuser
COPY --chown=appuser:appuser src/ /app/src/

# ==============================================================================
# ARCHITECT ALERT: NON-ROOT USER & BIND MOUNTS (UID/GID CONFLICTS)
# ------------------------------------------------------------------------------
# We are enforcing the Principle of Least Privilege (PoLP) by running the app 
# as 'appuser' instead of 'root'. 
#
# FUTURE DEVS: If you use Docker Bind Mounts (e.g., mapping ./src:/app/src) 
# for live-reloading in local development, you might face permission denied 
# errors if 'appuser' tries to write files (like logs or sqlite dbs) to a 
# folder owned by your host OS user.
# ==============================================================================

EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
