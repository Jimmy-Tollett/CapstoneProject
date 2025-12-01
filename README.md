# Capstone Project

## Fall 2025 Capstone Project

### Description

This project is being developed as part of CS4273 - Fall 2025 in collaboration with the FAA. The goal is to design a system that can receive, parse, and manipulate incoming flight data streams in real time. The processed data will be used to generate interactive maps for air traffic controllers, improving situational awareness and operational safety.

### Technologies

- Python
  - Flask
  - PyQt (?)
  - Geoplotlib (?)
- Kubernetes
  - K3D
- Docker
  - Dev Containers
- Postgres DB

### Initial Focus

Data Parsing & Validation

- The system must ingest live flight data messages.
- Each message includes metadata (such as declared length).
- The parser will validate that the message length field matches the actual message length.

This feature is critical because it:

- Ensures incoming data integrity.
- Prevents malformed data from propagating through the system.
- Serves as the foundation for subsequent parsing, storage, and mapping.

### Goals and Progress Plan

- Technology Setup – Python, Flask environment established; repo initialized.
- Parsing Development – Implement parsing logic with validation checks.
- Testing – Write unit tests across Python, Java, and JavaScript for the validation feature.
- Future Expansion – Deploy parsing service as a Kubernetes workload; integrate with replica databases and mapping front-end.

### Learning Resources

Group members are actively researching and aligning on the following:

- Python/Flask Documentation – [Flask Docs](https://flask.palletsprojects.com/), [Python Docs](https://docs.python.org/3/)
- Kubernetes Deployment Guides – [Kubernetes Docs](https://kubernetes.io/docs/home/)
- PostgreSQL Documents - [PostgreSQL Docs](https://www.postgresql.org/docs/17/index.html)
- Data Parsing Patterns – Tutorials and references for network protocols and message validation
- Supplemental Resources – YouTube tutorials, articles, and example projects

### Team Members

Mathew Agron

Jason Huang

Hunter Merrill

Andrew Moore

Jimmy Tollett

## Demo Guide

###### As of PR 2

> #### Spin up the cluster

This contains all of the business logic—namely the parser, database, and API.

- Navigate to `CapstoneProject/orchestrator/`
- Run `./cluster_setup.sh`
- Wait for pods to start
- - Run `kubectl get pods` until all report `READY 1/1` and `STATUS Running`
- - If kubectl times out, switch to the default kubernetes context
- - Then delete the stale capstone context: `kubectl config delete-context k3d-capstone`

> #### Start the Electron app

This runs on the host machine, independently of the cluster.

- Navigate to `CapstoneProject/app/frontend/electron/`
- Run `build_setup.sh`

> #### Health check

##### API

This is the only outward-facing endpoint. It's used by the Electron app to query the database.

- In your browser, navigate to `http://localhost:8080/health`
- - If the NodePort isn't properly exposed (error "localhost didn’t send any data"), manually forward the internal port:
    `kubectl get pods`
    `kubectl port-forward pod/<API POD NAME> 8000:8000` (note the port has changed from 8080 to 8000)
- - Navigate to `http://localhost:8000/health`

A healthy response indicates that the API service has successfully connected to the database.

```
{
  "database": {
    "error": null,
    "resolved_ip": "10.43.45.89",
  "url": "db:5432"
  },
  "status": "ok"
}
```

##### Parser

This endpoint exists only within the cluster; it's used to verify that the parser can access the database.

- The parser reports to the cluster's internal port 8001. Manually forward the port:
  `kubectl get pods`
  `kubectl port-forward pod/<PARSER POD NAME> 8001:8001`

- In your browser, navigate to `http://localhost:8001/health`

A healthy response indicates that the parser service has successfully connected to the database.

```
{
  "database": {
    "error": null,
    "resolved_ip": "10.43.45.89",
    "url": "db:5432"
  },
  "status": "ok"
}
```

##### Electron app

The desktop app exposes this endpoint in order to indicate whether it's able to communicate with the cluster.

- In your browser, navigate to `http://localhost:5001/health`

A healthy response indicates that the Electron app is able to make requests to the API service.

```
{
  "api_status": "success",
  "data": "{\"database\":{\"error\":null,\"resolved_ip\":\"10.43.45.89\",\"url\":\"db:5432\"},\"status\":\"ok\"}\n",
  "service": "atc-frontend",
  "status": "ok"
}
```

> #### Tearing down

- To terminate the Electron app, simply close the window.
- To tear down the cluster, run `k3d cluster delete capstone`

For referencing documents from FAA, here's [the SharePoint](https://onedrive.live.com/?redeem=aHR0cHM6Ly8xZHJ2Lm1zL2YvYy9jNGJhNDVjYTlmM2IxN2E2L0V0UDIydS1BSklaUHBvR0xrMHVJaXVVQkludVB6ZzhSMk1yeDlQUmt4YmZDV0E%5FZT1sVlg5dWg&id=C4BA45CA9F3B17A6%21sefdaf6d324804f86a6818b934b888ae5&cid=C4BA45CA9F3B17A6)
