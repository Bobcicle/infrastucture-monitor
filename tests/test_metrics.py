from unittest.mock import patch, Mock

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


@patch("app.services.metrics_service.psutil.cpu_count")
@patch("app.services.metrics_service.psutil.cpu_percent")
def test_cpu_metrics(mock_cpu_percent, mock_cpu_count):
    mock_cpu_percent.return_value = 25.0
    mock_cpu_count.side_effect = [8, 4]

    response = client.get("/api/v1/metrics")

    assert response.status_code == 200

    data = response.json()

    assert data["cpu"]["usage_percent"] == 25.0
    assert data["cpu"]["logical_cores"] == 8
    assert data["cpu"]["physical_cores"] == 4


@patch("app.services.metrics_service.psutil.virtual_memory")
def test_memory_metrics(mock_memory):
    mock_memory.return_value = Mock(
        total=16000,
        available=8000,
        used=8000,
        percent=50.0,
    )

    response = client.get("/api/v1/metrics")

    assert response.status_code == 200

    data = response.json()

    assert data["memory"]["total"] == 16000
    assert data["memory"]["usage_percent"] == 50.0


def test_metrics_response_structure():
    response = client.get("/api/v1/metrics")

    assert response.status_code == 200

    data = response.json()

    assert "cpu" in data
    assert "memory" in data
    assert "disk" in data
    assert "system" in data