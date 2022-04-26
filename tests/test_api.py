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

def test_predict_early():
    payload = {
        "id": 1,
        "mana": 1,
        "attack": 1,
        "health": 1
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert response.json() == "early"

def test_predict_late():
    payload = {
        "id": 1,
        "mana": 9,
        "attack": 9,
        "health": 9
    }

    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert response.json() == "late"
