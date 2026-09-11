import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app

client = TestClient(app)

def test_delete_todo_db():
    create_response = client.post("/todos", json={"title": "To Delete DB", "completed": False})
    new_id = create_response.json()["id"]

    delete_response = client.delete(f"/todos/{new_id}")
    assert delete_response.status_code == 200

    get_response = client.get(f"/todos/{new_id}")
    assert get_response.status_code == 404
