from part_3_functions.exercise_052 import product_of_list
from functools import reduce

def test_basic_case():
    """测试基本情况"""
    assert product_of_list([1, 2, 3, 4]) == 24

def test_empty_list():
    """测试空列表，根据定义，空列表的乘积为1"""
    assert product_of_list([]) == 1

def test_single_item():
    """测试单个元素的列表"""
    assert product_of_list([10]) == 10

def test_with_zero():
    """测试包含零的列表"""
    assert product_of_list([1, 2, 0, 4, 5]) == 0

def test_with_negatives():
    """测试包含负数的列表"""
    assert product_of_list([-1, 2, -3, 4]) == 24
    assert product_of_list([-1, -2, -3]) == -6
    
def test_against_alternative_implementation():
    """与提供了初始值的 reduce 函数进行比较"""
    assert product_of_list([5, 5, 5]) == reduce(lambda x,y: x*y, [5, 5, 5], 1) 