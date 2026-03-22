# Stage 1: deps — compile/install all Python dependencies
FROM python:3.13-slim AS deps

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Stage 2: runtime — lean final image
FROM python:3.13-slim AS runtime

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq5 \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Copy installed packages and scripts from the deps stage
COPY --from=deps /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=deps /usr/local/bin /usr/local/bin

WORKDIR /app

# Copy application source
COPY src/ src/
COPY api/ api/
COPY alembic/ alembic/
COPY alembic.ini .
COPY pyproject.toml .

# Install the package in editable mode so the src layout is importable
RUN pip install --no-cache-dir -e .

# Run as a non-root user for security
RUN useradd --create-home --shell /bin/bash parsify \
    && chown -R parsify:parsify /app
USER parsify

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
