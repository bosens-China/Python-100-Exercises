import pytest
from part_3_functions.exercise_042 import add

def test_add():
    """测试 add 函数"""
    assert add(5, 3) == 8
    assert add(-5, 3) == -2
    assert add(0, 0) == 0
    assert add(1.5, 2.5) == pytest.approx(4.0) 