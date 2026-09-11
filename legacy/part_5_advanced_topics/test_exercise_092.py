import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app

client = TestClient(app)

def test_cors_headers():
    response = client.options("/todos", headers={"Origin": "http://localhost:3000", "Access-Control-Request-Method": "GET"})
    assert response.status_code == 200
    assert response.headers["access-control-allow-origin"] == "http://localhost:3000"
