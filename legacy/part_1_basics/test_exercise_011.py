import pytest
from part_1_basics.exercise_011 import list_length

def test_list_length():
    assert list_length([1, 2, 3]) == 3
    assert list_length([]) == 0
    assert list_length(["a", "b", "c", "d"]) == 4
