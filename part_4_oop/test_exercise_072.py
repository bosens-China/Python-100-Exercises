import pytest
from part_4_oop.exercise_072 import Rectangle

def test_integer_dimensions():
    """测试整数尺寸的矩形。"""
    rect = Rectangle(10, 5)
    assert rect.area() == 50
    assert rect.perimeter() == 30

def test_float_dimensions():
    """测试浮点数尺寸的矩形。"""
    rect = Rectangle(3.5, 7.2)
    assert rect.area() == pytest.approx(25.2)
    assert rect.perimeter() == pytest.approx(21.4)

def test_square():
    """测试正方形（宽和高相等）的情况。"""
    square = Rectangle(6, 6)
    assert square.area() == 36
    assert square.perimeter() == 24

def test_zero_dimension():
    """测试当某个尺寸为0时的情况。"""
    rect = Rectangle(10, 0)
    assert rect.area() == 0
    assert rect.perimeter() == 20
    
    rect2 = Rectangle(0, 0)
    assert rect2.area() == 0
    assert rect2.perimeter() == 0
    
def test_negative_dimension():
    """测试当某个尺寸为负数时，是否会引发 ValueError。"""
    with pytest.raises(ValueError):
        Rectangle(-10, 5)
        
    with pytest.raises(ValueError):
        Rectangle(10, -5)
        
    with pytest.raises(ValueError):
        Rectangle(-10, -5) 