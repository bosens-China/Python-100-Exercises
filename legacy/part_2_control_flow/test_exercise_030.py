import pytest
from part_2_control_flow.exercise_030 import get_keys

def test_get_keys():
    d1 = {"a": 1, "b": 2, "c": 3}
    # We sort the keys to have a predictable order for testing
    assert sorted(get_keys(d1)) == ["a", "b", "c"]

    d2 = {"name": "Alice", "age": 30}
    assert sorted(get_keys(d2)) == ["age", "name"]

    assert get_keys({}) == []
