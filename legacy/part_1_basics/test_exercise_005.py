import pytest
from part_1_basics.exercise_005 import is_even

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(0) == True
    assert is_even(-4) == True
    assert is_even(-5) == False
