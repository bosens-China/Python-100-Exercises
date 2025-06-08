from part_2_control_flow.exercise_039 import find_max

def test_find_max_positive():
    """测试正数列表"""
    assert find_max([1, 5, 2, 8, 3]) == 8

def test_find_max_negative():
    """测试负数列表"""
    assert find_max([-1, -5, -2, -8, -3]) == -1

def test_find_max_mixed():
    """测试混合数列表"""
    assert find_max([-2, 0, 5, -8, 3]) == 5

def test_find_max_single_element():
    """测试单元素列表"""
    assert find_max([42]) == 42

def test_find_max_at_start():
    """测试最大值在开头的列表"""
    assert find_max([10, 1, 2, 3]) == 10

def test_find_max_empty_list():
    """测试空列表"""
    assert find_max([]) is None 