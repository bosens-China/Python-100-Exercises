from part_4_oop.exercise_071 import Dog

def test_repr_output():
    """测试 __repr__ 方法的输出是否是官方、明确的格式。"""
    fido = Dog("Fido", 5)
    assert repr(fido) == "Dog(name='Fido', age=5)"

def test_repr_in_container():
    """测试在容器中对象的 __repr__ 是否被正确调用。"""
    buddy = Dog("Buddy", 2)
    dog_list = [buddy]
    assert str(dog_list) == "[Dog(name='Buddy', age=2)]"

def test_eval_repr():
    """测试 eval(repr(obj)) 是否能创建一个等效的对象。"""
    lucy = Dog("Lucy", 10)
    repr_string = repr(lucy)
    
    # 使用 eval 重新创建对象
    # 注意：eval() 有安全风险，这里仅用于测试 repr 的有效性
    recreated_lucy = eval(repr_string)
    
    assert isinstance(recreated_lucy, Dog)
    assert recreated_lucy.name == lucy.name
    assert recreated_lucy.age == lucy.age
    # 验证两个对象的 __str__ 输出也相同
    assert str(recreated_lucy) == str(lucy) 