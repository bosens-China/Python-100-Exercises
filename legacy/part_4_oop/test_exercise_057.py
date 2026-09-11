import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app, db, Todo

client = TestClient(app)

def test_delete_todo_found():
    db.append(Todo(id=10, title="To Be Deleted", completed=False))
    
    response = client.delete("/todos/10")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo deleted"}
    assert not any(t.id == 10 for t in db)

def test_delete_todo_not_found():
    response = client.delete("/todos/999")
    assert response.status_code == 404
