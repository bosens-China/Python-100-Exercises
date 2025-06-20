import pytest
from part_4_oop.exercise_062 import Dog

@pytest.fixture
def my_dog():
    """提供一个标准的 Dog 实例作为测试数据"""
    return Dog("Fido", 5)

def test_bark_return_value(my_dog):
    """测试 bark 方法的返回值。"""
    assert my_dog.bark() == "Woof! Woof!" 