import pytest
from unittest.mock import MagicMock
from part_4_oop.repositories import TodoRepository
from part_4_oop.models import Todo

def test_todo_repository_get_by_id_unit():
    mock_db = MagicMock()
    expected_todo = Todo(id=1, title="Unit Test Todo", owner_id=1)
    # Configure the mock's behavior
    mock_db.query.return_value.filter.return_value.first.return_value = expected_todo

    repo = TodoRepository(db=mock_db)
    result = repo.get_by_id(todo_id=1)

    assert result == expected_todo
    mock_db.query.assert_called_once_with(Todo)
