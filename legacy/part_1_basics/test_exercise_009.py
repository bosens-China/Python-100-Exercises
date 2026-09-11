import pytest
from part_1_basics.exercise_009 import repeat_string

def test_repeat_string():
    assert repeat_string("a", 3) == "aaa"
    assert repeat_string("hello", 2) == "hellohello"
    assert repeat_string("test", 1) == "test"
    assert repeat_string("any", 0) == ""
