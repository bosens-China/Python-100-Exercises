import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app

client = TestClient(app)

def test_router_get_all_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
