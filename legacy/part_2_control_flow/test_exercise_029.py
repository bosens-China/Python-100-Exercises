import pytest
from part_2_control_flow.exercise_029 import word_count

def test_word_count():
    assert word_count("Hello world hello") == {"hello": 2, "world": 1}
    assert word_count("this is a test this is only a test") == {
        "this": 2, "is": 2, "a": 2, "test": 2, "only": 1
    }
    assert word_count("") == {}
    assert word_count("one") == {"one": 1}
