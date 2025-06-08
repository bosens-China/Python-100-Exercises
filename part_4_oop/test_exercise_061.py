from part_4_oop.exercise_061 import Dog

def test_dog_creation():
    """
    测试 Dog 类的实例能否被成功创建，并且属性是否正确设置。
    """
    # 这行代码会因为 NotImplementedError 而失败
    my_dog = Dog("Fido", 5)
    
    assert my_dog.name == "Fido"
    assert my_dog.age == 5

def test_another_dog():
    """
    用不同的数据测试 Dog 类的创建。
    """
    # 这行代码会因为 NotImplementedError 而失败
    another_dog = Dog("Buddy", 2)
    
    assert another_dog.name == "Buddy"
    assert another_dog.age == 2

def test_attribute_types():
    """测试属性的类型是否正确。"""
    dog = Dog("Rex", 3)
    assert isinstance(dog.name, str)
    assert isinstance(dog.age, int) 