from part_3_functions.exercise_050 import square_list_with_map

def test_positive_numbers():
    """测试正数列表"""
    assert square_list_with_map([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25]

def test_empty_list():
    """测试空列表"""
    assert square_list_with_map([]) == []

def test_mixed_numbers():
    """测试混合数列表"""
    assert square_list_with_map([-1, -2, 0, 3]) == [1, 4, 0, 9]
    
def test_floats():
    """测试浮点数列表"""
    assert square_list_with_map([1.5, 2.0]) == [2.25, 4.0] 