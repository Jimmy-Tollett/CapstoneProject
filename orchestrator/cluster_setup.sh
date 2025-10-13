#!/bin/bash

CLUSTER_NAME="capstone"
IMAGE_TAG="capstone-api:latest"
YAML_FILE="k8s-deployment.yaml"
NODE_PORT="30080"

echo "--- 1. Creating/Starting k3d Cluster ---"
k3d cluster create ${CLUSTER_NAME} --port "${NODE_PORT}:${NODE_PORT}@server:0"

echo "--- 2. Importing Docker image into k3d ---"
docker build -t ${IMAGE_TAG} . --no-cache
k3d image import ${IMAGE_TAG} -c ${CLUSTER_NAME}

echo "--- 3. Applying Kubernetes manifests ---"
kubectl apply -f ${YAML_FILE}