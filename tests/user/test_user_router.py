from pytest import fixture
from fastapi.testclient import TestClient
from app.main import app
from app.user.user_service import UserService

client = TestClient(app)

@fixture
def mock_user_service(monkeypatch):

    mock_instance = UserService()
    monkeypatch.setattr("app.user.user_router.UserService", lambda: mock_instance)

    return mock_instance

def test_create_user():
    user_data = {
        "username": "testuser",
        "password": "testpassword",
        "email" : "luan"
    }
    response = client.post("/api/users/", json=user_data)
    assert response.status_code == 201
    assert response.json()["message"] == "User created successfully"
    assert "user" in response.json()
