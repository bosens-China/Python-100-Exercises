import pytest
from part_1_basics.exercise_015 import square_list, filter_odd_numbers, sum_with_reduce

def test_square_list():
    assert square_list([1, 2, 3]) == [1, 4, 9]
    assert square_list([]) == []

def test_filter_odd_numbers():
    assert filter_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert filter_odd_numbers([2, 4, 6]) == []

def test_sum_with_reduce():
    assert sum_with_reduce([1, 2, 3, 4, 5]) == 15
    assert sum_with_reduce([]) == 0
