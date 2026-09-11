import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app

client = TestClient(app)

def test_get_only_own_todos():
    email1 = "user1@example.com"
    client.post("/users/", json={"email": email1, "password": "p1"})
    token1 = client.post("/login/token", data={"username": email1, "password": "p1"}).json()["access_token"]
    client.post("/todos/", json={"title": "U1 Todo", "completed": False}, headers={"Authorization": f"Bearer {token1}"})

    email2 = "user2@example.com"
    client.post("/users/", json={"email": email2, "password": "p2"})
    token2 = client.post("/login/token", data={"username": email2, "password": "p2"}).json()["access_token"]
    client.post("/todos/", json={"title": "U2 Todo", "completed": True}, headers={"Authorization": f"Bearer {token2}"})

    response = client.get("/todos/", headers={"Authorization": f"Bearer {token1}"})
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "U1 Todo"
