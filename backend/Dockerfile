FROM python:3.12-slim AS base

WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy source
COPY . .

# Install Python deps
RUN pip install --no-cache-dir .

# Default port (Render overrides via $PORT env var)
ENV PORT=8000
EXPOSE ${PORT}

# Health check
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
    CMD curl -f http://localhost:${PORT}/health || exit 1

# Run with uvicorn — use shell form so $PORT is expanded at runtime
CMD uvicorn src.main:app --host 0.0.0.0 --port ${PORT} --workers 1
