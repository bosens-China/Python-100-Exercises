import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app

client = TestClient(app)

def test_background_task_endpoint():
    # This test only checks if the endpoint returns immediately.
    # Testing the background task itself is more complex.
    response = client.post("/send-welcome-email") # Assuming this is the endpoint
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome email will be sent in the background"}
