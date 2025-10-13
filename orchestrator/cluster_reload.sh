CLUSTER_NAME="capstone"
IMAGE_TAG="capstone-api:latest"

docker build -t ${IMAGE_TAG} . --no-cache
k3d image import ${IMAGE_TAG} -c ${CLUSTER_NAME}
kubectl rollout restart deployment capstone-deployment