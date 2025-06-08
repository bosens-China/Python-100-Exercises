from part_2_control_flow.exercise_036 import simple_calculator

def test_addition():
    """测试加法"""
    assert simple_calculator(10, '+', 5) == 15

def test_subtraction():
    """测试减法"""
    assert simple_calculator(10, '-', 5) == 5

def test_multiplication():
    """测试乘法"""
    assert simple_calculator(10, '*', 5) == 50

def test_division():
    """测试除法"""
    assert simple_calculator(10, '/', 5) == 2.0

def test_division_by_zero():
    """测试除以零的情况"""
    assert simple_calculator(10, '/', 0) == "错误：除数不能为零！"

def test_invalid_operator():
    """测试无效运算符"""
    assert simple_calculator(10, '%', 5) is None # 或者返回特定的错误信息 