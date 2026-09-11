import pytest
from part_1_basics.exercise_006 import get_first_element

def test_get_first_element():
    assert get_first_element([1, 2, 3]) == 1
    assert get_first_element(["a", "b", "c"]) == "a"
    assert get_first_element([None, 1, 2]) == None
