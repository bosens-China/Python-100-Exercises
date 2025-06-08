from part_3_functions.exercise_051 import filter_even_numbers

def test_mixed_list():
    """测试混合列表"""
    assert filter_even_numbers([1, 2, 3, 4, 5]) == [2, 4]

def test_all_evens():
    """测试全偶数列表"""
    assert filter_even_numbers([2, 4, 6, 8]) == [2, 4, 6, 8]

def test_all_odds():
    """测试全奇数列表"""
    assert filter_even_numbers([1, 3, 5, 7]) == []

def test_empty_list():
    """测试空列表"""
    assert filter_even_numbers([]) == []

def test_with_zero_and_negatives():
    """测试包含零和负数的列表"""
    assert filter_even_numbers([-2, -1, 0, 1, 2, 3, 4]) == [-2, 0, 2, 4] 