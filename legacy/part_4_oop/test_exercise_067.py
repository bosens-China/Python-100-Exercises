import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app

client = TestClient(app)

def test_get_single_todo_db():
    create_response = client.post("/todos", json={"title": "Find Me DB", "completed": False})
    new_id = create_response.json()["id"]

    response = client.get(f"/todos/{new_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Find Me DB"

    response_404 = client.get(f"/todos/{new_id + 99}")
    assert response_404.status_code == 404
