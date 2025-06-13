"""
### 61. 创建一个简单的 `Dog` 类

- **描述:** 创建一个名为 `Dog` 的类。在 `__init__` 方法中，为它设置 `name` 和 `age` 两个属性。
- **提示:** `class Dog:`，`def __init__(self, name, age): self.name = name`。
- **期待:** `my_dog = Dog("Fido", 5)` 创建一个实例，`my_dog.name` 是 `"Fido"`。
"""

class Dog:
    """
    一个简单的 Dog 类，用于表示一只狗。
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    # 你可以在这里创建 Dog 实例并测试你的代码
    my_dog = Dog("Fido", 5)
    print(f"我的狗叫 {my_dog.name}，它 {my_dog.age} 岁了。")
    
    # 验证属性是否正确设置
    assert my_dog.name == "Fido"
    assert my_dog.age == 5
    print("Dog 实例创建成功，属性已验证！") 