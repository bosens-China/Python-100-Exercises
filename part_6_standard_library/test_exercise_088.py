import pytest
import math
from part_6_standard_library.exercise_088 import get_sqrt_and_pi

def test_sqrt_and_pi():
    """测试函数能否正确返回平方根和 pi 的值。"""
    sqrt_val, pi_val = get_sqrt_and_pi(81)
    
    # 测试平方根
    assert sqrt_val == 9.0
    
    # 测试 pi 的值
    assert pi_val == math.pi
    
def test_with_another_number():
    """用另一个数字测试。"""
    sqrt_val, pi_val = get_sqrt_and_pi(16)
    assert sqrt_val == 4.0
    assert pi_val == math.pi

def test_with_float_number():
    """用浮点数测试。"""
    sqrt_val, pi_val = get_sqrt_and_pi(2.25)
    assert sqrt_val == 1.5
    assert pi_val == math.pi
    
def test_with_zero():
    """用 0 测试。"""
    sqrt_val, pi_val = get_sqrt_and_pi(0)
    assert sqrt_val == 0.0
    assert pi_val == math.pi
    
def test_with_negative_number():
    """测试负数输入会引发 ValueError。"""
    with pytest.raises(ValueError):
        get_sqrt_and_pi(-1) 