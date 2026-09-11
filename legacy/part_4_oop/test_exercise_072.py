import pytest

def test_get_repository_dependency():
    try:
        from part_4_oop.main import get_repository
        from part_4_oop.repositories import TodoRepository
        from fastapi import Depends
        assert get_repository is not None
        assert callable(get_repository)
    except ImportError as e:
        pytest.fail(f"Could not import required components for repository dependency: {e}")
    except Exception as e:
        pytest.fail(f"Repository dependency test failed: {e}")
