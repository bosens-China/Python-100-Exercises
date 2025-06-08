from part_2_control_flow.exercise_037 import get_even_numbers

def test_get_even_numbers():
    """测试筛选偶数的功能"""
    assert get_even_numbers([1, 2, 3, 4, 5, 6]) == [2, 4, 6]
    assert get_even_numbers([1, 3, 5, 7]) == []
    assert get_even_numbers([2, 4, 6, 8]) == [2, 4, 6, 8]
    assert get_even_numbers([-2, -1, 0, 1, 2]) == [-2, 0, 2]
    assert get_even_numbers([]) == [] 