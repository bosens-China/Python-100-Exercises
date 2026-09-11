import pytest
from part_1_basics.exercise_018 import find_min

def test_find_min():
    assert find_min([1, 2, 3, 4, 5]) == 1
    assert find_min([-5, 0, 5]) == -5
    assert find_min([10, 1, 100]) == 1
    assert find_min([7]) == 7
