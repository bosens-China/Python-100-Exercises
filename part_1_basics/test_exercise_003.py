import math
import pytest
from part_1_basics.exercise_003 import calculate_circle_area

def test_calculate_circle_area():
    """测试不同半径下圆面积的计算"""
    # 测试半径为 5 的情况
    assert calculate_circle_area(5) == pytest.approx(math.pi * 5 * 5)
    # 测试半径为 1 的情况
    assert calculate_circle_area(1) == pytest.approx(math.pi)
    # 测试半径为 0 的情况
    assert calculate_circle_area(0) == pytest.approx(0) 