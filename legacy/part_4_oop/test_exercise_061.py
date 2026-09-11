import pytest

def test_database_setup():
    try:
        from part_4_oop.database import engine, SessionLocal, Base
        from sqlalchemy.orm import sessionmaker
        from sqlalchemy.ext.declarative import declarative_base

        assert engine is not None
        assert isinstance(SessionLocal, sessionmaker)
        assert isinstance(Base, type(declarative_base()))
    except ImportError as e:
        pytest.fail(f"Failed to import database components: {e}")
    except Exception as e:
        pytest.fail(f"An error occurred during database setup test: {e}")
