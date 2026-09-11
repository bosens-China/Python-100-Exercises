import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app

def test_user_login():
    import time
    unique_email = f"login_test_{int(time.time())}@example.com"
    password = "logmein"
    client.post("/users/", json={"email": unique_email, "password": password})
    
    response = client.post("/login/token", data={"username": unique_email, "password": password})
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_user_login_wrong_password():
    import time
    unique_email = f"login_fail_{int(time.time())}@example.com"
    password = "password123"
    client.post("/users/", json={"email": unique_email, "password": password})
    
    response = client.post("/login/token", data={"username": unique_email, "password": "wrongpassword"})
    assert response.status_code == 401
