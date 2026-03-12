#!/bin/bash
set -e

# Default variables
PROJECT_ID=$(gcloud config get-value project 2>/dev/null || echo "")
SERVICE_NAME="pi-calculator-mcp"
REGION="us-central1"

echo "Deploying $SERVICE_NAME to Google Cloud Run in $REGION..."

# Deploy from source using Cloud Run's built-in buildpacks or Dockerfile
# We use --source . to let Cloud Build build the container.
gcloud run deploy "$SERVICE_NAME" \
  --source . \
  --region "$REGION" \
  --allow-unauthenticated \
  --set-env-vars FASTMCP_STATELESS_HTTP=true

echo "Deployment complete!"
