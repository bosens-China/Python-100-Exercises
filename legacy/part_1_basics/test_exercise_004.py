import pytest
from part_1_basics.exercise_004 import rectangle_area

def test_rectangle_area():
    assert rectangle_area(3, 4) == 12
    assert rectangle_area(5, 5) == 25
    assert rectangle_area(1, 100) == 100
