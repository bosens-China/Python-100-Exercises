from part_3_functions.exercise_044 import describe_pet

def test_keyword_arguments():
    """测试关键字参数调用，顺序与定义时不同"""
    result = describe_pet(pet_name="Harry", animal_type="hamster")
    assert result == "I have a hamster named Harry."

def test_positional_arguments():
    """测试位置参数调用"""
    result = describe_pet("dog", "Willie")
    assert result == "I have a dog named Willie."

def test_mixed_arguments():
    """测试混合使用位置和关键字参数"""
    result = describe_pet("cat", pet_name="Tom")
    assert result == "I have a cat named Tom."
