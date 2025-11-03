# Run this script from within the orchestrator folder

CLUSTER_NAME="capstone"
API_IMAGE="api-image:latest"
PARSER_IMAGE="parser-image:latest"


# This exposes the cluster's ingress/LoadBalancer port (80) to port 8080 on your host machine.
# Your Electron client will talk to http://localhost:8080.
k3d cluster create ${CLUSTER_NAME} \
    --servers 1 \
    --agents 2 \
    -p "8080:30080@agent:0"

# Build & import docker images
# API container
cd ../backend
docker build --no-cache -t ${API_IMAGE} .
k3d image import ${API_IMAGE} -c ${CLUSTER_NAME}

# Parser container
# cd ../UPD_and_Parse
# docker build -t ${PARSER_IMAGE} .
# k3d image import ${PARSER_IMAGE} -c ${CLUSTER_NAME}

cd ../orchestrator
kubectl apply -f 01-database-pvc.yaml
kubectl apply -f 02-database-deployment.yaml
kubectl apply -f 03-api-deployment.yaml
#kubectl apply -f 04-parser-deployment.yaml

# Tear down:
# k3d cluster delete capstone