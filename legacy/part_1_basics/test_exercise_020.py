import pytest
from part_1_basics.exercise_020 import are_all_unique

def test_are_all_unique():
    assert are_all_unique([1, 2, 3, 4, 5]) == True
    assert are_all_unique([1, 2, 3, 3, 5]) == False
    assert are_all_unique(["a", "b", "c"]) == True
    assert are_all_unique(["a", "b", "a"]) == False
    assert are_all_unique([]) == True
