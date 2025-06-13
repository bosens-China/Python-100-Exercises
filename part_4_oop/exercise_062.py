"""
### 62. 给类添加方法

- **描述:** 在 `Dog` 类中添加一个名为 `bark` 的方法，调用时会打印出 "Woof! Woof!"。
- **提示:** 在 `class Dog:` 内部定义 `def bark(self):`。
- **期待:** `my_dog.bark()` 会在控制台输出 `Woof! Woof!`。
"""

class Dog:
    # 在这里写下你的代码
    pass


if __name__ == '__main__':
    my_dog = Dog("Fido", 5)
    bark_sound = my_dog.bark()
    print(f"{my_dog.name} says: {bark_sound}") 