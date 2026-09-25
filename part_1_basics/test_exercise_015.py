import pytest
from part_1_basics.exercise_015 import square_list, filter_odd_numbers, sum_numbers

def test_square_list():
    assert square_list([1, 2, 3]) == [1, 4, 9]
    assert square_list([]) == []
    assert square_list([-2, 0]) == [4, 0]

def test_filter_odd_numbers():
    assert filter_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert filter_odd_numbers([2, 4, 6]) == []
    assert filter_odd_numbers([-3, -2, 0]) == [-3]

def test_sum_numbers():
    assert sum_numbers([1, 2, 3, 4, 5]) == 15
    assert sum_numbers([]) == 0
    assert sum_numbers([-3, 1]) == -2
