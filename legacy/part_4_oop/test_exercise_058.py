import pytest

def test_repository_structure():
    try:
        from part_4_oop.main import TodoRepository
        repo = TodoRepository()
        assert hasattr(repo, 'get_all')
        assert hasattr(repo, 'get_by_id')
        assert hasattr(repo, 'create')
        assert hasattr(repo, 'update')
        assert hasattr(repo, 'delete')
    except ImportError:
        pytest.fail("Could not import TodoRepository from main.py")
    except Exception as e:
        pytest.fail(f"Failed to instantiate or inspect TodoRepository: {e}")
