import pytest
from part_4_oop.exercise_066 import Cat

@pytest.fixture(autouse=True)
def reset_cat_species():
    """在每个测试运行后，自动重置 Cat 类的 species 变量。"""
    original_species = Cat.species
    yield
    Cat.species = original_species

def test_cat_instance_variables():
    """
    测试实例变量 `name` 是否为每个实例独有。
    """
    cat1 = Cat("Whiskers")
    cat2 = Cat("Tom")
    
    assert cat1.name == "Whiskers"
    assert cat2.name == "Tom"

def test_cat_class_variable():
    """
    测试类变量 `species` 是否在所有实例和类本身之间共享。
    """
    cat1 = Cat("Whiskers")
    
    assert Cat.species == "Felis catus"
    assert cat1.species == "Felis catus"
    
    # 验证如果修改类变量，所有实例都会受到影响
    # (为了测试隔离，我们改完后再改回去)
    original_species = Cat.species
    Cat.species = "A new species"
    
    cat2 = Cat("Tom")
    assert cat1.species == "A new species"
    assert cat2.species == "A new species"
    
    # 改回原样，避免影响其他测试
    Cat.species = original_species

def test_class_variable_access():
    """测试类变量可以被类和所有实例访问。"""
    cat1 = Cat("Garfield")
    # 通过类访问
    assert Cat.species == "Felis catus"
    # 通过实例访问
    assert cat1.species == "Felis catus"

def test_class_variable_modification():
    """测试修改类变量会影响所有实例。"""
    cat1 = Cat("Felix")
    cat2 = Cat("Sylvester")
    
    # 初始状态
    assert cat1.species == "Felis catus"
    assert cat2.species == "Felis catus"
    
    # 修改类变量
    Cat.species = "A new species"
    
    # 验证所有实例都受到了影响
    assert cat1.species == "A new species"
    assert cat2.species == "A new species"

def test_instance_shadowing_class_variable():
    """测试在实例上赋同名变量不会影响类变量。"""
    cat1 = Cat("Shadow")
    cat2 = Cat("No-Shadow")

    # 在 cat1 实例上创建一个名为 'species' 的实例变量
    cat1.species = "Panthera pardus"
    
    # cat1 的 'species' 是实例变量
    assert cat1.species == "Panthera pardus"
    
    # cat2 仍然访问的是类变量
    assert cat2.species == "Felis catus"
    
    # Cat 类的变量没有被改变
    assert Cat.species == "Felis catus" 