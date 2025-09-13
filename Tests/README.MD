# CAT-21 Parser & Mapping System – Integration & E2E Testing

## Overview

This project is a microservice-based system for parsing and visualizing CAT-21 flight data. It consists of several services:
* UDP Parser – Ingests and parses raw CAT-21 messages.
* Cluster Database – Stores parsed flight data.
* Service Orchestration / Manager – Coordinates service startup, health checks, and scaling.
* Map / Web API – Exposes flight data for visualization on a web-based map.

To ensure reliability and correctness, we plan to implement a hybrid test suite that combines unit tests, integration tests, and end-to-end (E2E) UI tests. A subset of these tests will also serve as health checks in production.



## Testing Strategy

1. Unit Tests (Fast, Local)
    * Tooling: pytest
    * Scope:
        * Parser logic (e.g., validate CAT-21 message parsing functions).
        * Database models, schema validation, and data access layer.
        * Orchestration/manager service behavior (e.g., correct container lifecycle handling).
    * Examples:
        * Test that a parsed message’s len field matches the actual byte length.
        * Test that database insertions and queries work as expected.
        * Test retry logic in orchestration.

2. Integration Tests (System-level in Docker)
    * Tooling: pytest + docker-compose (or testcontainers-python).
    * Scope:
        * Spin up the full stack: parser, database, orchestration, and web API.
        * Send sample CAT-21 UDP messages into the parser.
    * Verify:
        * Data is ingested and stored in the DB.
        * The web API returns the correct parsed flight data.
        * Services communicate correctly under load.
    * Examples:
        * Inject a known CAT-21 message via UDP socket and confirm corresponding JSON output from the API.
        * Scale multiple parser replicas in Kubernetes/Compose and ensure results remain consistent.
        * Verify database replication across cluster nodes.

3. End-to-End UI Tests (User Flows)
    * Tooling: Playwright
    * Scope:
        * Spin up the map/web service with test data available in the DB.
        * Use Playwright to open the browser and simulate controller workflows:
        * Load the map and check that aircraft markers appear at expected coordinates.
        * Interact with filters, zoom, and timeline playback.
        * Verify that API-backed updates reflect in the UI.
    * Examples:
        * Send a CAT-21 packet, wait for the API to update, then check that the map shows the correct aircraft position.
        * Verify UI elements (search box, layer toggles, legends) render and behave correctly.

4. Health Checks (Lightweight Continuous Tests)
    * Tooling: Simple pytest or requests-based checks, possibly scheduled by the orchestration manager.
    * Scope:
        * Ensure core services are alive and reachable.
        * Verify a basic CAT-21 packet can be ingested and retrieved through the API within a short time window.
    * Examples:
        * GET /health returns 200 and expected payload.
        * Ingest a minimal test packet and confirm DB/API update within N seconds.

## Proposed Repository Structure (Subject to Change)
```
tests/
  unit/
    test_parser.py
    test_db.py
    test_orchestrator.py
  integration/
    test_end_to_end.py
    test_health.py
  e2e_ui/
    test_map_ui.spec.ts
    playwright.config.ts
docker/
  docker-compose.test.yml
```

## Research Questions / Next Steps
1.	How to best integrate pytest with docker-compose or testcontainers for spinning up parser + DB + API during tests?
2.	Should we seed test data into the DB directly, or always inject through the UDP parser?
3.	What is the best way to structure Playwright tests for a map-based UI (e.g., verifying map markers reliably)?
4.	How to design lightweight health checks that can run periodically in production without overloading the system?
5.	How to integrate all three layers of testing (unit, integration, E2E) into the CI/CD pipeline? (GitLab CI + Docker)
6.	How do we handle test data and avoid polluting production databases? (Separate test DB, ephemeral containers, fixtures, etc.)
7.	How much test coverage is “enough” for FAA standards — should we target specific compliance metrics (e.g., DO-278B/DO-200B)?