import requests


BASE_URL = "http://localhost:8000"


def test_backend_responde_correctamente():
    response = requests.get(BASE_URL)

    assert response.status_code == 200


def test_swagger_docs_disponible():
    response = requests.get(f"{BASE_URL}/docs")

    assert response.status_code == 200
    assert "Swagger UI" in response.text or "swagger" in response.text.lower()


def test_openapi_json_disponible():
    response = requests.get(f"{BASE_URL}/openapi.json")

    assert response.status_code == 200

    data = response.json()

    assert "openapi" in data
    assert "paths" in data
    assert isinstance(data["paths"], dict)