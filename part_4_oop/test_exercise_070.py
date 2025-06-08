from part_4_oop.exercise_070 import Dog

def test_str_output():
    """测试 __str__ 方法的输出是否符合预期格式。"""
    fido = Dog("Fido", 5)
    assert str(fido) == "Fido is a 5-year-old dog."
    
def test_print_output():
    """测试 print() 函数是否使用了 __str__ 方法。"""
    # 这个测试间接验证了 print 的行为，因为 print(obj) 内部会调用 str(obj)
    buddy = Dog("Buddy", 2)
    assert str(buddy) == "Buddy is a 2-year-old dog."

def test_different_dog():
    """测试不同实例的 __str__ 输出。"""
    lucy = Dog("Lucy", 10)
    assert str(lucy) == "Lucy is a 10-year-old dog." 