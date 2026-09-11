import pytest
from part_2_control_flow.exercise_038 import count_lines

def test_count_lines(tmp_path):
    p = tmp_path / "multiline.txt"
    p.write_text("line 1\nline 2\nline 3")
    assert count_lines(p) == 3

def test_count_lines_empty_file(tmp_path):
    p = tmp_path / "empty.txt"
    p.write_text("")
    assert count_lines(p) == 0

def test_count_lines_single_line(tmp_path):
    p = tmp_path / "singleline.txt"
    p.write_text("one line")
    assert count_lines(p) == 1
