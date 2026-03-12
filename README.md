# Pi Calculator MCP Server

This is a Model Context Protocol (MCP) server that calculates Pi to a given number of decimal places using the Machin-like formula and series expansion method.

It is built using `uv`, Python, and the `FastMCP` framework exposing a tool via Streamable HTTP transport.

## Features

- **calculate_pi**: Calculates $\pi$ up to the desired number of decimals using a rapidly converging series expansion.

## Local Development

### Prerequisites

- [uv](https://github.com/astral-sh/uv)
- Python 3.12+

### Running the Server

1. Initialize the environment and install dependencies:
   ```bash
   uv sync
   ```

2. Run the server using `uvicorn`:
   ```bash
   uvicorn server:app --host 0.0.0.0 --port 8080 --reload
   ```
   The server will be available at `http://localhost:8080/mcp`.

## Deployment to Google Cloud Run

This application is ready to be deployed to Google Cloud Run as a public unauthenticated service.

### Prerequisites

- [Google Cloud CLI](https://cloud.google.com/sdk/docs/install) installed and authenticated.
- A Google Cloud Project with Billing and Cloud Run API enabled.

### Deployment Script

Simply run the provided deployment script:

```bash
./deploy.sh
```

This will deploy the application from the local source to Cloud Run in the `us-central1` region. It sets the `FASTMCP_STATELESS_HTTP=true` environment variable, which is recommended for horizontal scaling behind a load balancer to run without stateful sessions in the streamable HTTP transport.
