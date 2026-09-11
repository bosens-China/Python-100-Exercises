import pytest
from part_2_control_flow.exercise_026 import find_index

def test_find_index():
    assert find_index([1, 2, 3, 4, 5], 3) == 2
    assert find_index(["a", "b", "c"], "a") == 0
    assert find_index(["apple", "banana", "cherry"], "date") == -1
    assert find_index([], 1) == -1
    assert find_index([1, 2, 2, 3], 2) == 1
