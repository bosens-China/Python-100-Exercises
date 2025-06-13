import random
from part_6_standard_library.exercise_086 import generate_random_integer_list, choose_random_item

def test_generate_random_integer_list():
    """测试生成的随机整数列表的属性。"""
    n = 5
    min_val = 1
    max_val = 20
    result = generate_random_integer_list(n, min_val, max_val)
    
    # 1. 测试列表长度是否正确
    assert len(result) == n
    
    # 2. 测试列表中的每个元素是否都在指定范围内
    for item in result:
        assert min_val <= item <= max_val

def test_choose_random_item_reproducibility():
    """通过设置随机种子来测试 choice 的可复现性。"""
    items = ["apple", "banana", "cherry", "orange", "grape"]
    
    # 设置一个固定的种子
    random.seed(42)
    choice1 = choose_random_item(items)
    
    # 重新设置相同的种子
    random.seed(42)
    choice2 = choose_random_item(items)
    
    # 两次选择的结果应该是相同的
    assert choice1 == choice2
    
    # 验证结果是列表中的一个成员
    assert choice1 in items

def test_choose_random_item_from_single_list():
    """测试从只包含一个元素的列表中选择。"""
    items = ["the_only_choice"]
    assert choose_random_item(items) == "the_only_choice" 