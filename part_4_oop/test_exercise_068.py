import pytest
import math
from part_4_oop.exercise_068 import Circle

def test_initialization():
    """测试 Circle 是否能用有效半径正确初始化。"""
    c = Circle(5)
    # 不鼓励直接测试私有变量，但在此为了与原测试保持一致
    assert c._radius == 5
    assert c.radius == 5

def test_initialization_with_negative_radius():
    """测试用负半径初始化时是否会引发 ValueError。"""
    with pytest.raises(ValueError):
        Circle(-5)

def test_setter():
    """测试 radius 的 setter 是否能正确更新值。"""
    c = Circle(5)
    c.radius = 10
    assert c._radius == 10
    assert c.radius == 10

def test_setter_with_negative_value():
    """测试给 radius 设置负值时是否会引发 ValueError。"""
    c = Circle(5)
    with pytest.raises(ValueError):
        c.radius = -10
    # 验证半径值没有被改变
    assert c.radius == 5

def test_area_property():
    """测试 area 属性是否能正确计算面积。"""
    c = Circle(10)
    expected_area = math.pi * 100
    assert c.area == pytest.approx(expected_area)

def test_area_is_readonly():
    """测试 area 属性是否是只读的。"""
    c = Circle(10)
    with pytest.raises(AttributeError):
        c.area = 500 