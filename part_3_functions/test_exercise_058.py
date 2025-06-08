from part_3_functions.exercise_058 import add
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300)
])
def test_add(a, b, expected):
    """
    测试 add 函数能否正确计算两个整数的和。
    """
    assert add(a, b) == expected

def test_add_has_type_hints():
    """
    测试 add 函数是否有正确的类型提示。
    """
    import inspect
    sig = inspect.signature(add)
    assert sig.parameters['a'].annotation is int
    assert sig.parameters['b'].annotation is int
    assert sig.return_annotation is int 