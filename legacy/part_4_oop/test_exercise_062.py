import pytest
from sqlalchemy import Column, Integer, String, Boolean

def test_todo_model_definition():
    try:
        from part_4_oop.models import Todo
        from part_4_oop.database import Base

        assert issubclass(Todo, Base)
        assert Todo.__tablename__ == "todos"
        assert isinstance(Todo.id.property.columns[0].type, Integer)
        assert Todo.id.property.columns[0].primary_key
        assert isinstance(Todo.title.property.columns[0].type, String)
        assert isinstance(Todo.completed.property.columns[0].type, Boolean)
    except ImportError as e:
        pytest.fail(f"Failed to import Todo model: {e}")
    except Exception as e:
        pytest.fail(f"An error occurred during model definition test: {e}")
