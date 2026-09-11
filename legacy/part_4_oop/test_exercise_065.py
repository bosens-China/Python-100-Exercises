import pytest
from fastapi.testclient import TestClient
from part_4_oop.main import app, get_db
from part_4_oop.database import SessionLocal, engine, Base

@pytest.fixture(scope="module")
def test_db():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    yield db
    Base.metadata.drop_all(bind=engine)

app.dependency_overrides[get_db] = test_db

client = TestClient(app)

def test_create_todo_db():
    response = client.post("/todos", json={"title": "Test DB Create", "completed": False})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Test DB Create"
    assert "id" in data
