from part_3_functions.exercise_054 import make_multiplier_of
import pytest

@pytest.mark.parametrize("n, x, expected", [
    (3, 5, 15),
    (10, 10, 100),
    (0, 100, 0),
    (-1, 5, -5),
    (5, -5, -25)
])
def test_make_multiplier_of(n, x, expected):
    """
    测试闭包函数能否正确工作。
    """
    # times_n = make_multiplier_of(n)
    # assert times_n(x) == expected
    pass # 函数未实现，暂时跳过

def test_make_multiplier_of_returns_callable():
    """
    测试 make_multiplier_of 是否返回一个可调用对象（函数）。
    """
    # assert callable(make_multiplier_of(5))
    pass # 函数未实现，暂时跳过 