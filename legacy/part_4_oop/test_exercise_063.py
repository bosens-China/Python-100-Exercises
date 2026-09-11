import pytest
import os

def test_database_file_creation():
    try:
        from part_4_oop import main
        import time
        time.sleep(0.1)
        assert os.path.exists("./todos.db")
    except Exception as e:
        pytest.fail(f"Failed to import main or find db file: {e}")
    finally:
        if os.path.exists("./todos.db"):
            os.remove("./todos.db")
