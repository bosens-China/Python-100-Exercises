from part_1_basics.exercise_015 import get_list_slice

def test_standard_case():
    """测试标准用例"""
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert get_list_slice(numbers) == [2, 3, 4, 5]

def test_different_list():
    """测试不同类型的列表"""
    assert get_list_slice(['a', 'b', 'c', 'd', 'e', 'f']) == ['c', 'd', 'e', 'f']
    assert get_list_slice([10, 20, 30, 40, 50, 60]) == [30, 40, 50, 60]

def test_edge_cases():
    """测试边界情况"""
    # 测试刚好满足切片条件的列表
    assert get_list_slice([0, 1, 2, 3, 4, 5]) == [2, 3, 4, 5]
    # 测试列表长度不足的情况
    assert get_list_slice([0, 1, 2, 3]) == [2, 3]
    # 测试列表长度小于切片起始索引的情况
    assert get_list_slice([0, 1]) == []
 