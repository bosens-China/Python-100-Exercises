import pytest
from part_4_oop.exercise_067 import Person

@pytest.fixture
def person_instance():
    """提供一个 Person 类的实例用于测试。"""
    return Person("Alice", 30, "123-456-789")

def test_public_attribute_access(person_instance):
    """测试公有属性 'name' 可以被直接访问和修改。"""
    assert person_instance.name == "Alice"
    person_instance.name = "Bob"
    assert person_instance.name == "Bob"

def test_protected_attribute_access(person_instance):
    """测试受保护属性 '_age' 可以被直接访问和修改。"""
    assert person_instance._age == 30
    person_instance._age = 31
    assert person_instance._age == 31

def test_private_attribute_access_fails(person_instance):
    """测试直接访问私有属性 '__bank_account' 会引发 AttributeError。"""
    with pytest.raises(AttributeError):
        person_instance.__bank_account

def test_name_mangled_attribute_access(person_instance):
    """测试可以通过名称改写后的名字来访问私有属性。"""
    # 这个测试验证了名称改写的机制
    assert person_instance._Person__bank_account == "123-456-789"

def test_display_info_method(person_instance):
    """测试 display_info 方法可以访问所有属性。"""
    # 假设 display_info 返回一个包含所有信息的字符串
    info = person_instance.display_info()
    assert "Alice" in info
    assert "30" in info
    assert "123-456-789" in info 