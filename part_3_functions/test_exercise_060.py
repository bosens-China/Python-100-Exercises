from part_3_functions.exercise_060 import bubble_sort

def test_basic_case():
    """测试基本情况"""
    assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]

def test_already_sorted():
    """测试已排序的列表"""
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """测试反向排序的列表"""
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_with_duplicates():
    """测试包含重复元素的列表"""
    assert bubble_sort([5, 1, 4, 2, 8, 4, 1]) == [1, 1, 2, 4, 4, 5, 8]

def test_with_negatives():
    """测试包含负数的列表"""
    assert bubble_sort([-5, 1, -4, 2, 0]) == [-5, -4, 0, 1, 2]

def test_empty_list():
    """测试空列表"""
    assert bubble_sort([]) == []

def test_single_element():
    """测试单个元素的列表"""
    assert bubble_sort([100]) == [100]
    
def test_original_list_is_unchanged():
    """测试原始列表是否被修改"""
    original_list = [5, 1, 4, 2, 8]
    # 创建一个副本以进行比较
    original_list_copy = original_list[:]
    bubble_sort(original_list)
    assert original_list == original_list_copy 