import pytest
from part_2_control_flow.exercise_027 import merge_dictionaries

def test_merge_dictionaries():
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}
    assert merge_dictionaries(d1, d2) == {"a": 1, "b": 2, "c": 3, "d": 4}

    d3 = {"a": 1, "b": 2}
    d4 = {"b": 3, "c": 4}
    assert merge_dictionaries(d3, d4) == {"a": 1, "b": 3, "c": 4}

    assert merge_dictionaries({}, {"x": 1}) == {"x": 1}
    assert merge_dictionaries({"y": 2}, {}) == {"y": 2}
    assert merge_dictionaries({}, {}) == {}
