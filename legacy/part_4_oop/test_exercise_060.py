import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app, db, Todo

client = TestClient(app)

@pytest.fixture(autouse=True)
def setup_db_for_filtering_tests():
    original_db = db.copy()
    db.clear()
    db.extend([
        Todo(id=1, title="Completed 1", completed=True),
        Todo(id=2, title="Incomplete 1", completed=False),
        Todo(id=3, title="Completed 2", completed=True),
    ])
    yield
    db.clear()
    db.extend(original_db)

def test_filter_todos_completed():
    response = client.get("/todos?completed=true")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert all(item['completed'] for item in data)

def test_filter_todos_incomplete():
    response = client.get("/todos?completed=false")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert not data[0]['completed']

def test_filter_todos_no_filter():
    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json()) == 3
