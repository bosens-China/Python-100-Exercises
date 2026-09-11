import pytest
from part_2_control_flow.exercise_039 import flatten_list

def test_flatten_list():
    assert flatten_list([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
    assert flatten_list([["a"], ["b", "c"]]) == ["a", "b", "c"]
    assert flatten_list([[1], [], [2, 3]]) == [1, 2, 3]
    assert flatten_list([]) == []
