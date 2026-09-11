import pytest
from part_2_control_flow.exercise_036 import robust_read_file
from io import StringIO
import sys

@pytest.fixture
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

def test_robust_read_file_exists(tmp_path, captured_output):
    p = tmp_path / "test.txt"
    p.write_text("Hello")
    
    content = robust_read_file(str(p))
    assert content == "Hello"
    assert "File operation finished." in captured_output[0].getvalue()

def test_robust_read_file_not_exists(captured_output):
    content = robust_read_file("non_existent_file.txt")
    assert content is None
    assert "File operation finished." in captured_output[0].getvalue()
