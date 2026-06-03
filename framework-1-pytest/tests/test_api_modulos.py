import requests


BASE_URL = "http://localhost:8000"


def test_endpoint_participantes_responde_correctamente():
    response = requests.get(f"{BASE_URL}/participantes/")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)


def test_endpoint_salas_responde_correctamente():
    response = requests.get(f"{BASE_URL}/salas/")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)


def test_endpoint_reservas_responde_correctamente():
    response = requests.get(f"{BASE_URL}/reservas/")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)