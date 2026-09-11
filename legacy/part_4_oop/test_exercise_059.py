import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app

client = TestClient(app)

def test_create_todo_with_empty_title():
    response = client.post("/todos", json={"title": "", "completed": False})
    assert response.status_code == 422

def test_create_todo_with_valid_title():
    response = client.post("/todos", json={"title": "Valid", "completed": False})
    assert response.status_code in [200, 201]
