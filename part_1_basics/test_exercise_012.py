from part_1_basics.exercise_012 import is_in_range

def test_is_in_range():
    """测试数字是否在指定范围内"""
    # 在范围内
    assert is_in_range(22) is True
    # 边界值
    assert is_in_range(18) is True
    assert is_in_range(30) is True
    # 在范围外
    assert is_in_range(17) is False
    assert is_in_range(31) is False
    assert is_in_range(10) is False 