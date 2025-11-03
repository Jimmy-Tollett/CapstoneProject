# Timeline

### PR 1

- [x] Map out process interdependencies, flow of data

- [x] Build Docker scaffold

- [x] Build k3d scaffold

### PR 2

- [ ] Set up dev containers

- [ ] Add all services into the orchestrator

- [x] Get minimal connectivity between two services

## PR 3

- [ ] Set up logging & monitoring

- [ ] Automate system-wide tests

- [ ] Add fault tolerance (restart services if they crash, catch bad data, graceful shutdown)

## Project End

- [ ] Smooth out deployment so everything can be spun up on fresh machines

- [ ] Produce final system documentation

k3d cluster create --api-port 6550 -p "8081:80@loadbalancer" --agents 2
kubectl create deployment nginx --image=nginx
kubectl create service clusterip nginx --tcp=80:80
kubectl apply -f deployment.yaml -l kind=Ingress
