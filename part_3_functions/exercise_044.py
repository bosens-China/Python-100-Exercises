"""
### 44. 关键字参数

- **描述:** 编写一个函数 `describe_pet`，接受 `animal_type` 和 `pet_name` 两个参数，并打印一句话。在调用时使用关键字参数，并且顺序可以和定义时不同。
- **提示:** 调用时使用 `function(key=value)` 的形式。
- **期待:** 调用 `describe_pet(pet_name="Harry", animal_type="hamster")` 输出 `I have a hamster named Harry.`。
"""

def describe_pet(animal_type, pet_name):
    """
    根据动物类型和名字描述宠物。
    为了方便测试，函数将返回字符串而不是直接打印。
    :param animal_type: 动物的种类
    :param pet_name: 宠物的名字
    :return: 描述宠物的字符串
    """
    # 在这里写下你的代码
    return f"I have a {animal_type} named {pet_name}."

if __name__ == '__main__':
    # 使用关键字参数调用，顺序与定义时不同
    description = describe_pet(pet_name="Harry", animal_type="hamster")
    print(description)
    
    # 使用位置参数调用
    description2 = describe_pet("dog", "Willie")
    print(description2) 