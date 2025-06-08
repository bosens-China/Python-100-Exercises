import pytest
from part_4_oop.exercise_075 import Vector

def test_vector_addition():
    """测试向量加法。"""
    v1 = Vector(2, 3)
    v2 = Vector(3, 4)
    result = v1 + v2
    # 因为我们重载了 __eq__，所以可以直接比较 Vector 实例
    assert result == Vector(5, 7)

def test_addition_with_negatives():
    """测试包含负数的向量加法。"""
    v1 = Vector(-5, 10)
    v2 = Vector(3, -4)
    assert v1 + v2 == Vector(-2, 6)

def test_addition_with_zero_vector():
    """测试与零向量相加。"""
    v1 = Vector(5, 5)
    v0 = Vector(0, 0)
    assert v1 + v0 == v1

def test_equality():
    """直接测试 __eq__ 方法。"""
    assert (Vector(1, 2) == Vector(1, 2)) is True
    assert (Vector(1, 2) == Vector(2, 1)) is False
    
def test_addition_with_non_vector():
    """测试与非 Vector 类型相加时是否会引发 TypeError。"""
    v1 = Vector(1, 1)
    with pytest.raises(TypeError):
        v1 + 5 # v1.__add__(5) 返回 NotImplemented，这会导致 TypeError 