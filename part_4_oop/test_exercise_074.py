import pytest
from part_4_oop.exercise_074 import Flyable, Swimmable, Duck

@pytest.fixture
def duck():
    """提供一个 Duck 实例"""
    return Duck()

def test_duck_can_fly(duck):
    """测试 Duck 实例是否从 Flyable 继承了 fly 方法。"""
    assert duck.fly() == "I am flying!"

def test_duck_can_swim(duck):
    """测试 Duck 实例是否从 Swimmable 继承了 swim 方法。"""
    assert duck.swim() == "I am swimming!"
    
def test_duck_can_quack(duck):
    """测试 Duck 实例是否有自己的 quack 方法。"""
    assert duck.quack() == "Quack! Quack!"
    
def test_duck_is_instance_of_all(duck):
    """测试 Duck 实例是否是所有父类的实例。"""
    assert isinstance(duck, Duck)
    assert isinstance(duck, Flyable)
    assert isinstance(duck, Swimmable)

if __name__ == '__main__':
    pytest.main() 