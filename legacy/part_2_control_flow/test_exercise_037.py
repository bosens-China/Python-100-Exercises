import pytest
from part_2_control_flow.exercise_037 import write_to_file

def test_write_to_file(tmp_path):
    p = tmp_path / "output.txt"
    content_to_write = "This is the content."

    write_to_file(p, content_to_write)

    assert p.read_text() == content_to_write

def test_overwrite_file(tmp_path):
    p = tmp_path / "overwrite.txt"
    p.write_text("Initial content.")
    new_content = "New content."

    write_to_file(p, new_content)

    assert p.read_text() == new_content
