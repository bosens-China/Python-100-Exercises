import pytest
from sqlalchemy.orm import Session

def test_get_db_dependency():
    try:
        from part_4_oop.main import get_db
        db_generator = get_db()
        db_session = next(db_generator)
        assert isinstance(db_session, Session)
        with pytest.raises(StopIteration):
            next(db_generator)
    except ImportError:
        pytest.fail("Could not import get_db from main.py")
    except Exception as e:
        pytest.fail(f"get_db dependency test failed: {e}")
