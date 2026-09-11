import pytest
from part_1_basics.exercise_012 import to_uppercase

def test_to_uppercase():
    assert to_uppercase("hello") == "HELLO"
    assert to_uppercase("Python") == "PYTHON"
    assert to_uppercase("123") == "123"
    assert to_uppercase("") == ""
