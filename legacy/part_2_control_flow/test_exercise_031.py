import pytest
from part_2_control_flow.exercise_031 import Shape, Rectangle

def test_inheritance():
    rect = Rectangle(10, 5)
    assert isinstance(rect, Shape)

def test_rectangle_area():
    rect = Rectangle(width=10, height=5)
    assert rect.area() == 50

def test_shape_area():
    shape = Shape()
    assert shape.area() == 0
