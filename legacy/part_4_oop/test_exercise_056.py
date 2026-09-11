import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app, db, Todo

client = TestClient(app)

def test_update_todo_found():
    if not any(t.id == 1 for t in db):
        db.append(Todo(id=1, title="Original", completed=False))
    
    update_data = {"title": "Updated", "completed": True}
    response = client.put("/todos/1", json=update_data)
    
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated"
    assert data["completed"] is True

def test_update_todo_not_found():
    response = client.put("/todos/999", json={"title": "Doesn't matter"})
    assert response.status_code == 404
