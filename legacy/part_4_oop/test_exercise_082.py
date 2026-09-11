import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app

client = TestClient(app)

def test_unauthenticated_create_todo():
    response = client.post("/todos/", json={"title": "test", "completed": False})
    assert response.status_code == 401
