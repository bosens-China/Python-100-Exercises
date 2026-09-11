import pytest
from part_4_oop.main import Todo, db

def test_todo_model():
    todo = Todo(id=1, title="Test", completed=False)
    assert todo.id == 1
    assert todo.title == "Test"
    assert not todo.completed

def test_in_memory_db_exists():
    assert isinstance(db, list)
    if db:
        assert isinstance(db[0], Todo)
