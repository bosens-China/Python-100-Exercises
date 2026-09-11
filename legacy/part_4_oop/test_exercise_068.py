import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app

client = TestClient(app)

def test_update_todo_db():
    create_response = client.post("/todos", json={"title": "Original DB", "completed": False})
    new_id = create_response.json()["id"]

    response = client.put(f"/todos/{new_id}", json={"title": "Updated DB", "completed": True})
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated DB"
    assert data["completed"] is True
