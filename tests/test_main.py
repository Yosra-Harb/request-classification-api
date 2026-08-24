from fastapi.testclient import TestClient

from app.config import settings
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": f"{settings.app_name} is running"}


def test_classify_endpoint_returns_classification():
    response = client.post(
        "/classify",
        json={
            "text": "I cannot login to my account",
            "source": "web",
        },
    )

    assert response.status_code == 200

    assert response.json() == {
        "category": "technical",
        "priority": "normal",
        "normalized_text": "I cannot login to my account",
    }


def test_classify_endpoint_rejects_invalid_source():
    response = client.post(
        "/classify",
        json={
            "text": "I cannot login",
            "source": "telegram",
        },
    )

    assert response.status_code == 422


def test_classify_endpoint_rejects_missing_text():
    response = client.post(
        "/classify",
        json={
            "source": "web",
        },
    )

    assert response.status_code == 422


def test_classify_endpoint_rejects_whitespace_only_text():
    response = client.post(
        "/classify",
        json={
            "text": "     ",
            "source": "web",
        },
    )

    assert response.status_code == 422


def test_health_check():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "version": settings.app_version,
        "environment": settings.environment.value,
    }


def test_middleware_does_not_break_request_flow():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_health_endpoint_still_works_with_logging_middleware():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
