from part_1_basics.exercise_020 import get_types_of_variables

def test_get_types_of_variables():
    """
    测试 get_types_of_variables 函数是否返回了正确的类型列表。
    用户需要在函数中创建指定类型的变量，并返回它们的类型。
    """
    # get_types_of_variables 应该返回一个包含 [int, float, str, list, dict] 的列表
    expected_types = [int, float, str, list, dict]
    
    actual_types = get_types_of_variables()
    
    # 确保返回的列表长度正确
    assert len(actual_types) == 5, f"函数应返回包含 5 个类型的列表，但返回了 {len(actual_types)} 个。"
    
    # 确保返回的类型与预期一致且顺序正确
    assert actual_types == expected_types, \
        f"返回的类型列表 {actual_types} 与预期的 {expected_types} 不符。请检查变量创建的顺序和类型是否正确。" 