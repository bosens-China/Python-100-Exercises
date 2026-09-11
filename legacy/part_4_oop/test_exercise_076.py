import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app

client = TestClient(app)

def test_user_registration():
    import time
    unique_email = f"testuser_{int(time.time())}@example.com"
    response = client.post("/users/", json={"email": unique_email, "password": "secret"})
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == unique_email
    assert "id" in data
    assert "password" not in data
