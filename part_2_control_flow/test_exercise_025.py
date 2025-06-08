from part_2_control_flow.exercise_025 import find_narcissistic_numbers

def test_find_narcissistic_numbers():
    """测试水仙花数的查找"""
    # 函数返回的可能是列表，转换为集合进行比较可以忽略元素的顺序
    result_set = set(find_narcissistic_numbers())
    expected_set = {153, 370, 371, 407}
    assert result_set == expected_set 