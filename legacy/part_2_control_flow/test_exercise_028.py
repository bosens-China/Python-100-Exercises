import pytest
from part_2_control_flow.exercise_028 import remove_duplicates

def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
    assert remove_duplicates(["a", "b", "a", "c"]) == ["a", "b", "c"]
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    assert remove_duplicates([]) == []
