import pytest
from part_1_basics.exercise_013 import key_exists

def test_key_exists():
    d = {"a": 1, "b": 2}
    assert key_exists(d, "a") == True
    assert key_exists(d, "c") == False
    assert key_exists({}, "any") == False
