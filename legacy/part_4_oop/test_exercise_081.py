import pytest

def test_get_current_user_dependency_exists():
    try:
        from part_4_oop.auth import get_current_user
        assert callable(get_current_user)
    except ImportError:
        pytest.fail("Could not import get_current_user dependency.")
