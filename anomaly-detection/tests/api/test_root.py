from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["application"] == "KRONOS"
    assert data["version"] == "1.0.0"
    assert data["status"] == "running"
