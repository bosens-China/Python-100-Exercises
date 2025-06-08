"""
### 62. 给类添加方法

- **描述:** 在 `Dog` 类中添加一个名为 `bark` 的方法，调用时会打印出 "Woof! Woof!"。
- **提示:** 在 `class Dog:` 内部定义 `def bark(self):`。
- **期待:** `my_dog.bark()` 会在控制台输出 `Woof! Woof!`。
"""

class Dog:
    """
    一个代表狗的简单类。
    """
    def __init__(self, name: str, age: int):
        """
        初始化 Dog 对象。
        :param name: 狗的名字
        :param age: 狗的年龄
        """
        self.name = name
        self.age = age

    def bark(self) -> str:
        """
        狗发出叫声。
        为了方便测试，此方法将返回字符串而不是直接打印。
        """
        # 在这里写下你的代码
        print("Woof! Woof!") # 保持题目要求的打印行为
        return "Woof! Woof!"

if __name__ == '__main__':
    my_dog = Dog("Fido", 5)
    print(f"{my_dog.name} says:")
    my_dog.bark() 