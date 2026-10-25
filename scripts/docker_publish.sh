#!/bin/bash
set -e

# --- Configuration ---
IMAGE_NAME="crypto-recovery-forensics-lab"
# Fallback to organization/username if provided, otherwise standard repository namespace
DOCKERHUB_USERNAME="${DOCKERHUB_USERNAME}"
DOCKER_REPO="${DOCKERHUB_USERNAME}/${IMAGE_NAME}"
TAG="${1:-latest}"

# --- Environment Validation ---
if [ -z "$DOCKERHUB_USERNAME" ] || [ -z "$DOCKERHUB_TOKEN" ]; then
  echo "[-] Error: DOCKERHUB_USERNAME and DOCKERHUB_TOKEN environment variables must be set." >&2
  exit 1
fi

echo "[*] Authenticating with Docker Hub as user: $DOCKERHUB_USERNAME..."
# Securely pass the Docker Hub token via STDIN to avoid plain-text history leaks
echo "$DOCKERHUB_TOKEN" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin

echo "[*] Building Docker image for $DOCKER_REPO:$TAG..."
docker build -t "$DOCKER_REPO:$TAG" -t "$DOCKER_REPO:latest" .

echo "[*] Pushing image tags to Docker Hub registry..."
docker push "$DOCKER_REPO:$TAG"
docker push "$DOCKER_REPO:latest"

echo "[SUCCESS] Image successfully published: $DOCKER_REPO:$TAG"
