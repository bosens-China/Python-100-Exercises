import pytest
# `square` 是在 exercise_049.py 模块级别定义的 lambda 
from part_3_functions.exercise_049 import square

@pytest.mark.parametrize("x, expected", [
    (5, 25),
    (0, 0),
    (-3, 9),
    (10, 100),
    (1.5, 2.25)
])
def test_square_lambda(x, expected):
    """
    测试在模块级别定义的 square lambda 函数。
    """
    assert square(x) == expected 