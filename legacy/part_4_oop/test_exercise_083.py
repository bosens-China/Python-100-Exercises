import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app

client = TestClient(app)

def test_authenticated_create_todo_and_association():
    import time
    email = f"assoc_test_{int(time.time())}@example.com"
    password = "password"
    client.post("/users/", json={"email": email, "password": password})
    login_res = client.post("/login/token", data={"username": email, "password": password})
    token = login_res.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    response = client.post("/todos/", json={"title": "My Todo", "completed": False}, headers=headers)
    assert response.status_code == 201
    new_todo = response.json()
    assert new_todo["title"] == "My Todo"
    assert "owner_id" in new_todo
