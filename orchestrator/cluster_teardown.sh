kubectl config delete-context k3d-capstone
kubectl config delete-cluster capstone
kubectl delete deployment api-deployment
kubectl delete deployment parser-deployment
kubectl delete deployment db-deployment
kubectl delete configmap db-schema
docker rm -f $(docker ps -a -q -f name=k3d-capstone)