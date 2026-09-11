import pytest
from part_3_functions.exercise_050 import find_all_numbers

def test_find_all_numbers():
    assert find_all_numbers("There are 3 apples and 10 bananas.") == ["3", "10"]
    assert find_all_numbers("The price is $19.99") == ["19", "99"]
    assert find_all_numbers("No numbers here.") == []
    assert find_all_numbers("123 456") == ["123", "456"]
