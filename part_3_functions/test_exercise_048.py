import pytest
from part_3_functions.exercise_048 import factorial

def test_factorial_of_5():
    """测试 5 的阶乘"""
    assert factorial(5) == 120

def test_factorial_of_0():
    """测试 0 的阶乘（基本情况）"""
    assert factorial(0) == 1

def test_factorial_of_1():
    """测试 1 的阶乘"""
    assert factorial(1) == 1
    
def test_factorial_of_10():
    """测试 10 的阶乘"""
    assert factorial(10) == 3628800

def test_negative_input():
    """测试无效输入（负数），应引发 ValueError"""
    with pytest.raises(ValueError):
        factorial(-1)
        
def test_non_integer_input():
    """测试无效输入（非整数），应引发 ValueError"""
    with pytest.raises(ValueError):
        factorial(1.5) 