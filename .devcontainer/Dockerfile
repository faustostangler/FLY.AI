FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

# Install uv for fast Python package management
# Install ruff and mypy globally
RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
    && pip install ruff mypy pytest
    
ENV PATH="/root/.cargo/bin:${PATH}"

# Optional: Add any OS packages if you need them.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
