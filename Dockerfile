# Stage 1: Base - System Dependencies
FROM python:3.12-slim AS base

WORKDIR /app
ENV PLAYWRIGHT_BROWSERS_PATH=/app/pw-browsers
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq5 \
    curl \
    # Playwright system dependencies
    libglib2.0-0 libnss3 libatk1.0-0 libatk-bridge2.0-0 libcups2 \
    libdrm2 libxkbcommon0 libxcomposite1 libxdamage1 libxext6 \
    libxfixes3 libxrandr2 libgbm1 libpango-1.0-0 libcairo2 libasound2 \
    && rm -rf /var/lib/apt/lists/*

# Stage 2: Builder - Artifact Preparation
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
ENV PLAYWRIGHT_BROWSERS_PATH=/app/pw-browsers
WORKDIR /app

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    uv sync --frozen --no-install-project --no-dev

# Install Playwright browsers in builder stage
RUN .venv/bin/python -m playwright install chromium

COPY src/ /app/src/
COPY pyproject.toml uv.lock README.md /app/
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# Stage 3: Runtime - Production Image
FROM base AS runtime

RUN useradd -m appuser && chown appuser:appuser /app

# Copy prepared artifacts from builder
COPY --from=builder --chown=appuser:appuser /app/.venv /app/.venv
COPY --from=builder --chown=appuser:appuser /app/pw-browsers /app/pw-browsers
COPY --from=builder --chown=appuser:appuser /app/src/ /app/src/
COPY --chown=appuser:appuser .envs/ /app/.envs/

ENV PATH="/app/.venv/bin:$PATH"
USER appuser

EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
