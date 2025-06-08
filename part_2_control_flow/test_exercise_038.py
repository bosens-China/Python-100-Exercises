from part_2_control_flow.exercise_038 import deduplicate_list

def test_deduplicate_list_with_numbers():
    """测试数字列表去重"""
    assert deduplicate_list([1, 2, 2, 3, 4, 3]) == [1, 2, 3, 4]

def test_deduplicate_list_with_strings():
    """测试字符串列表去重"""
    assert deduplicate_list(["apple", "banana", "apple", "cherry"]) == ["apple", "banana", "cherry"]

def test_deduplicate_list_no_duplicates():
    """测试没有重复元素的列表"""
    assert deduplicate_list([10, 20, 30]) == [10, 20, 30]

def test_deduplicate_list_empty():
    """测试空列表"""
    assert deduplicate_list([]) == []

def test_deduplicate_list_mixed_types():
    """测试包含混合类型的列表"""
    assert deduplicate_list([1, "a", 1, "b", "a"]) == [1, "a", "b"] 