import pytest
from part_2_control_flow.exercise_025 import get_even_numbers

def test_get_even_numbers():
    assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert get_even_numbers([10, 21, 32, 43]) == [10, 32]
    assert get_even_numbers([1, 3, 5]) == []
    assert get_even_numbers([]) == []
    assert get_even_numbers([-2, -1, 0, 1, 2]) == [-2, 0, 2]
