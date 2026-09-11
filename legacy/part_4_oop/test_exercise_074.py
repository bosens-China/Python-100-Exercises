import pytest
from sqlalchemy.orm import relationship

def test_model_relationships():
    try:
        from part_4_oop.models import Todo, User

        assert hasattr(Todo, 'owner')
        assert hasattr(User, 'todos')

        assert 'owner_id' in Todo.__table__.columns
        fk = list(Todo.__table__.columns['owner_id'].foreign_keys)[0]
        assert fk.column.table.name == 'users'
        assert fk.column.name == 'id'

    except ImportError as e:
        pytest.fail(f"Failed to import models for relationship test: {e}")
    except Exception as e:
        pytest.fail(f"Relationship test failed: {e}")
