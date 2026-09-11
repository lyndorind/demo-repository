from fastapi.testclient import TestClient

from backend_server import app

client = TestClient(app)


def test_get_timezone():
    response = client.get("/timezone/Kyiv")
    assert response.status_code == 200
    assert response.json() == {"timezone": "Europe/Kyiv"}
