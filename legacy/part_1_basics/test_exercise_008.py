import pytest
from part_1_basics.exercise_008 import find_max

def test_find_max():
    assert find_max(1, 5) == 5
    assert find_max(-1, -5) == -1
    assert find_max(0, 0) == 0
    assert find_max(10, 10) == 10
