import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app, db, Todo

client = TestClient(app)

def test_get_single_todo_found():
    if not any(t.id == 1 for t in db):
        db.append(Todo(id=1, title="Find Me", completed=False))

    response = client.get("/todos/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Find Me"

def test_get_single_todo_not_found():
    response = client.get("/todos/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Todo not found"}
