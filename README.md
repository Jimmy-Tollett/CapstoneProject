# Capstone Project

## Fall 2025 Capstone Project

### Description
This project is being developed as part of CS4273 - Fall 2025 in collaboration with the FAA. The goal is to design a system that can receive, parse, and manipulate incoming flight data streams in real time. The processed data will be used to generate interactive maps for air traffic controllers, improving situational awareness and operational safety.

### Technologies

* Python
    * Flask
    * PyQt (?)
    * Geoplotlib (?)
    * Pandas
    * Numpy
    * csv library
* Kubernetes
    * K3D
* Docker
    * Dev Containers
* Postgres DB

### Initial Focus
Data Parsing & Validation
* The system must ingest live flight data messages.
* Each message includes metadata (such as declared length).
* The parser will validate that the message length field matches the actual message length.

This feature is critical because it:
* Ensures incoming data integrity.
* Prevents malformed data from propagating through the system.
* Serves as the foundation for subsequent parsing, storage, and mapping.

### Goals and Progress Plan
* Technology Setup – Python, Flask environment established; repo initialized.
* Parsing Development – Implement parsing logic with validation checks.
* Testing – Write unit tests across Python, Java, and JavaScript for the validation feature.
* Future Expansion – Deploy parsing service as a Kubernetes workload; integrate with replica databases and mapping front-end.

### Learning Resources
Group members are actively researching and aligning on the following:
* Python/Flask Documentation – [Flask Docs](https://flask.palletsprojects.com/), [Python Docs](https://docs.python.org/3/)
* Kubernetes Deployment Guides – [Kubernetes Docs](https://kubernetes.io/docs/home/)
* PostgreSQL Documents - [PostgreSQL Docs](https://www.postgresql.org/docs/17/index.html)
* Data Parsing Patterns – Tutorials and references for network protocols and message validation
* Supplemental Resources – YouTube tutorials, articles, and example projects


### Team Members

Mathew Agron

Jason Huang

Hunter Merrill

Andrew Moore

Jimmy Tollett
