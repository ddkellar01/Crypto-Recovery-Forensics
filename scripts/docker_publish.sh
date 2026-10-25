#!/bin/bash
set -e

IMAGE_NAME="crypto-recovery-forensics-lab"
TAG="latest"

echo "[*] Building Docker image..."
docker build -t $IMAGE_NAME:$TAG .

echo "[*] Image built successfully: $IMAGE_NAME:$TAG"
# Optional: Tag and push to container registry (e.g., Docker Hub or GitHub Packages)
# docker tag $IMAGE_NAME:$TAG your-registry-username/$IMAGE_NAME:$TAG
# docker push your-registry-username/$IMAGE_NAME:$TAG
