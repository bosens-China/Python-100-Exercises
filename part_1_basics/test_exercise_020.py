from part_1_basics.exercise_020 import get_types_of_variables

def test_get_types_of_variables():
    """测试函数是否能返回一组变量的正确类型"""
    # 假设函数按顺序返回 int, float, str, list, dict, tuple, set 的类型
    types = get_types_of_variables()
    expected_types = [int, float, str, list, dict, tuple, set]
    
    # 直接比较整个列表
    assert types == expected_types 