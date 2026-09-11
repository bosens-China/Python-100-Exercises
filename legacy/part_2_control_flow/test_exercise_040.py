import pytest
from part_2_control_flow.exercise_040 import find_second_largest

def test_find_second_largest():
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([10, 20, 5, 15]) == 15
    assert find_second_largest([-1, -5, -2, -10]) == -2
    assert find_second_largest([5, 5, 5, 5]) == None
    assert find_second_largest([10]) == None
    assert find_second_largest([]) == None
    assert find_second_largest([1, 1, 2, 2]) == 1
