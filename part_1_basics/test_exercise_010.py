import pytest
from part_1_basics.exercise_010 import celsius_to_fahrenheit

def test_celsius_to_fahrenheit():
    """测试摄氏度到华氏度的转换"""
    # 冰点
    assert celsius_to_fahrenheit(0) == pytest.approx(32.0)
    # 沸点
    assert celsius_to_fahrenheit(100) == pytest.approx(212.0)
    # 题目中的例子
    assert celsius_to_fahrenheit(20) == pytest.approx(68.0)
    # 负数温度
    assert celsius_to_fahrenheit(-10) == pytest.approx(14.0) 