# Use the official Python image
FROM python:3.12-slim

# Install uv for fast dependency management
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Set working directory
WORKDIR /app

# Copy dependency files
COPY requirements.txt .

# Install dependencies into the system environment
RUN uv pip install --system -r requirements.txt

# Copy application source
COPY server.py .

# Expose the port Cloud Run expects
EXPOSE 8080

# Cloud Run sets the PORT environment variable to 8080
# We use FastMCP stateless_http via environment variable (FASTMCP_STATELESS_HTTP) in deployment
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8080", "--workers", "1"]
