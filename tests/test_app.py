from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_home_page_is_available() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert "美心 AI 行政助手" in response.text
    assert "第一阶段：系统基础" in response.text


def test_liveness() -> None:
    response = client.get("/health/live")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_readiness_with_sqlite() -> None:
    response = client.get("/health/ready")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "database": "connected"}
