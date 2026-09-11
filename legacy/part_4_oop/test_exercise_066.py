import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app

client = TestClient(app)

def test_get_all_todos_db():
    client.post("/todos", json={"title": "Test Get All", "completed": True})
    
    response = client.get("/todos")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[-1]["title"] == "Test Get All"
