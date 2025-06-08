import pytest
from part_4_oop.exercise_069 import Calculator

def test_instance_method():
    """测试实例方法 add。"""
    calc = Calculator(owner="TestBot")
    assert calc.add(10, 5) == 15
    # 验证实例方法可以访问 self.owner
    assert calc.owner == "TestBot"

def test_class_method():
    """测试类方法 info。"""
    # 通过类调用
    assert Calculator.info() == "This is a Calculator class."
    # 通过实例调用
    calc = Calculator(owner="TestBot")
    assert calc.info() == "This is a Calculator class."

def test_static_method():
    """测试静态方法 multiply。"""
    # 通过类调用
    assert Calculator.multiply(10, 5) == 50
    # 通过实例调用
    calc = Calculator(owner="TestBot")
    assert calc.multiply(10, 5) == 50
    
def test_calling_instance_method_on_class():
    """验证不能在类上直接调用实例方法（除非手动传递实例）。"""
    with pytest.raises(TypeError):
        Calculator.add(2, 3)

if __name__ == '__main__':
    pytest.main() 