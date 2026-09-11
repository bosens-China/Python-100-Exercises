import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app, db, Todo

client = TestClient(app)

def test_create_todo():
    from pydantic import BaseModel
    class TodoCreate(BaseModel):
        title: str
        completed: bool

    new_todo_data = {"title": "New Todo", "completed": False}
    response = client.post("/todos", json=new_todo_data)
    
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "New Todo"
    assert not data["completed"]
    assert "id" in data
    assert any(t.id == data["id"] for t in db)
