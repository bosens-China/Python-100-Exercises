import pytest
from part_1_basics.exercise_014 import get_value

def test_get_value():
    d = {"name": "Alice", "age": 30}
    assert get_value(d, "name") == "Alice"
    assert get_value(d, "age") == 30
