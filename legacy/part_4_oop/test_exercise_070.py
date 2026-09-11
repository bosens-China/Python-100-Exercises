import pytest

def test_schemas_file_structure():
    try:
        from part_4_oop.schemas import Todo, TodoCreate
        from pydantic import BaseModel

        assert issubclass(Todo, BaseModel)
        assert issubclass(TodoCreate, BaseModel)
        assert 'id' in Todo.model_fields
        assert 'id' not in TodoCreate.model_fields

    except ImportError:
        pytest.fail("Could not import schemas from schemas.py")
    except Exception as e:
        pytest.fail(f"Schema definition test failed: {e}")
