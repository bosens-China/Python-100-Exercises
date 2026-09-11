import pytest
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

def test_user_model_and_schema():
    try:
        from part_4_oop.models import User
        from part_4_oop.schemas import User as UserSchema, UserCreate
        from part_4_oop.database import Base

        assert issubclass(User, Base)
        assert User.__tablename__ == "users"
        assert isinstance(User.email.property.columns[0].type, String)
        assert User.email.property.columns[0].unique

        assert issubclass(UserSchema, BaseModel)
        assert issubclass(UserCreate, BaseModel)
        assert 'email' in UserCreate.model_fields
        assert 'password' in UserCreate.model_fields
        assert 'password' not in UserSchema.model_fields

    except ImportError as e:
        pytest.fail(f"Failed to import User model/schemas: {e}")
