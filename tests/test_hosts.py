def test_create_host(client):
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


def test_list_hosts(client):
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


def test_host_not_found(client):
    response = client.get("/api/v1/hosts/999")

    assert response.status_code == 404


def test_duplicate_hostname(client):
    host_data = {
        "hostname": "server-01",
        "ip_address": "192.168.1.100",
        "operating_system": "Debian 13",
    }

    first = client.post("/api/v1/hosts", json=host_data)
    second = client.post("/api/v1/hosts", json=host_data)

    assert first.status_code == 201
    assert second.status_code == 409


def test_delete_host(client):
    response = client.post(
        "/api/v1/hosts",
        json={
            "hostname": "server-01",
            "ip_address": "192.168.1.100",
            "operating_system": "Debian 13",
        },
    )

    host_id = response.json()["id"]

    delete_response = client.delete(
        f"/api/v1/hosts/{host_id}"
    )

    assert delete_response.status_code == 204

    get_response = client.get(
        f"/api/v1/hosts/{host_id}"
    )

    assert get_response.status_code == 404