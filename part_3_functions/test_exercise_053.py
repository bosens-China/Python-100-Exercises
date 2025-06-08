import pytest
from part_3_functions.exercise_053 import operate_on_numbers

# 定义一些用于测试的函数
def add(a, b):
    return a + b

def power(a, b):
    return a ** b

def test_with_add_function():
    """测试使用预定义的加法函数"""
    assert operate_on_numbers(10, 5, add) == 15

def test_with_lambda_subtract():
    """测试使用 lambda 定义的减法函数"""
    subtract = lambda x, y: x - y
    assert operate_on_numbers(10, 5, subtract) == 5

def test_with_inline_lambda_multiply():
    """测试使用内联的 lambda 乘法函数"""
    assert operate_on_numbers(10, 5, lambda x, y: x * y) == 50

def test_with_power_function():
    """测试使用预定义的幂函数"""
    assert operate_on_numbers(2, 3, power) == 8
    
def test_with_floats():
    """测试浮点数运算"""
    assert operate_on_numbers(2.5, 1.5, add) == pytest.approx(4.0)
    
def test_string_concatenation():
    """测试字符串拼接"""
    concat = lambda s1, s2: s1 + s2
    assert operate_on_numbers("hello", " world", concat) == "hello world"

if __name__ == '__main__':
    pytest.main() 