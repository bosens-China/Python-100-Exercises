import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app

client = TestClient(app)

def test_duplicate_user_registration():
    import time
    unique_email = f"duplicate_{int(time.time())}@example.com"
    client.post("/users/", json={"email": unique_email, "password": "secret"})
    
    response = client.post("/users/", json={"email": unique_email, "password": "secret"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Email already registered"}
