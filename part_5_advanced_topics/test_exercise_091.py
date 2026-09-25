from fastapi.testclient import TestClient
from part_4_oop.main import app

def test_rate_limiting():
    client = TestClient(app)
    statuses = [client.post("/login/token", data={"username": "missing@example.com", "password": "wrong"}).status_code for _ in range(8)]
    assert 429 in statuses, f"请求 8 次仍未触发 429：{statuses}"
