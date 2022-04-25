from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_read_main():
    """
        Test if the main endpoint is ok.
    """
    response = client.get("/")
    assert response.status_code == 200


def test_healthcheck():
    """
        Test if the healthcheck endpoint is ok
        and if return the status alive.
    """
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"status": "alive"}
