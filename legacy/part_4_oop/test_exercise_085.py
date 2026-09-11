import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app

client = TestClient(app)

def test_cannot_modify_others_todos():
    email1 = "owner@example.com"
    client.post("/users/", json={"email": email1, "password": "p1"})
    token1 = client.post("/login/token", data={"username": email1, "password": "p1"}).json()["access_token"]
    todo_res = client.post("/todos/", json={"title": "Owner Todo", "completed": False}, headers={"Authorization": f"Bearer {token1}"})
    todo_id = todo_res.json()["id"]

    email2 = "attacker@example.com"
    client.post("/users/", json={"email": email2, "password": "p2"})
    token2 = client.post("/login/token", data={"username": email2, "password": "p2"}).json()["access_token"]
    
    response = client.put(f"/todos/{todo_id}", json={"title": "Hacked"}, headers={"Authorization": f"Bearer {token2}"})
    assert response.status_code == 403
