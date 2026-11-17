import pytest

from fastapi.testclient import TestClient

from app.main import app
from app.services import host_service


client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_hosts():
    host_service.hosts.clear()
    host_service.next_host_id = 1


def test_create_host():
    response = client.post(
        "/api/v1/hosts",
        json={
            "hostname": "debian-server-01",
            "ip_address": "192.168.1.100",
            "operating_system": "Debian 13",
        },
    )

    assert response.status_code == 201

    data = response.json()

    assert data["hostname"] == "debian-server-01"
    assert data["status"] == "unknown"
    assert data["id"] == 1


def test_list_hosts():
    client.post(
        "/api/v1/hosts",
        json={
            "hostname": "server-01",
            "ip_address": "192.168.1.100",
            "operating_system": "Debian 13",
        },
    )

    response = client.get("/api/v1/hosts")

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_host_not_found():
    response = client.get("/api/v1/hosts/999")

    assert response.status_code == 404


def test_invalid_ip_address():
    response = client.post(
        "/api/v1/hosts",
        json={
            "hostname": "server-01",
            "ip_address": "invalid",
            "operating_system": "Debian 13",
        },
    )

    assert response.status_code == 422