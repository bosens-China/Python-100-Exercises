import pytest
from part_1_basics.exercise_019 import create_dictionary

def test_create_dictionary():
    keys = ["name", "age", "city"]
    values = ["Alice", 30, "New York"]
    assert create_dictionary(keys, values) == {"name": "Alice", "age": 30, "city": "New York"}
    assert create_dictionary(["a"], [1]) == {"a": 1}
    assert create_dictionary([], []) == {}
