"""
Shared fixtures and utilities for integration tests.
"""

import pytest
import requests
import socket
import json
import time
from datetime import datetime, timezone
import docker
import subprocess


@pytest.fixture(scope="session")
def docker_compose_system():
    """Fixture to start/stop the complete system using docker-compose"""
    # TODO: Start entire system for integration testing
    # Use docker-compose up for test environment
    pass


@pytest.fixture
def sample_cat21_messages():
    """Fixture providing multiple sample CAT-21 messages"""
    # TODO: Return list of real CAT-21 messages for testing
    return [
        b"\x15\x00\x3b...",  # Real message 1
        b"\x15\x00\x2a...",  # Real message 2
        b"\x15\x00\x45...",  # Real message 3
    ]


@pytest.fixture
def udp_client():
    """Fixture providing UDP client for sending test messages"""
    # TODO: Return configured UDP socket for testing
    pass


@pytest.fixture
def api_client():
    """Fixture providing HTTP client for API testing"""
    # TODO: Return configured requests session for API calls
    return requests.Session()


@pytest.fixture
def system_health_checker():
    """Fixture providing system health monitoring utilities"""
    # TODO: Return utility class for monitoring system health
    pass