import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app, db, Todo

client = TestClient(app)

def test_get_all_todos():
    original_db = db.copy()
    db.clear()
    db.append(Todo(id=1, title="Test Todo", completed=False))
    
    response = client.get("/todos")
    assert response.status_code == 200
    assert response.json() == [
        {"id": 1, "title": "Test Todo", "completed": False}
    ]
    
    db.clear()
    db.extend(original_db)
