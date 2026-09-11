import pytest
from part_1_basics.exercise_010 import is_list_empty

def test_is_list_empty():
    assert is_list_empty([]) == True
    assert is_list_empty([1, 2, 3]) == False
    assert is_list_empty(["a"]) == False
    assert is_list_empty([None]) == False
