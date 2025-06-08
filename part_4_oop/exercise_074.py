"""
### 74. 多重继承

- **描述:** 创建一个 `Flyable` 类（有 `fly` 方法）和一个 `Swimmable` 类（有 `swim` 方法）。然后创建一个 `Duck` 类，它同时继承这两个类。
- **提示:** `class Duck(Flyable, Swimmable):`
- **期待:** `duck = Duck()`，`duck.fly()` 和 `duck.swim()` 都能被成功调用。
"""

class Flyable:
    """一个代表能飞的Mixin类。"""
    def fly(self) -> str:
        message = "I am flying!"
        print(message)
        return message

class Swimmable:
    """一个代表能游泳的Mixin类。"""
    def swim(self) -> str:
        message = "I am swimming!"
        print(message)
        return message

# 在这里写下你的代码
class Duck(Flyable, Swimmable):
    """
    一个鸭子类，通过多重继承获得了飞行和游泳的能力。
    """
    def quack(self) -> str:
        message = "Quack! Quack!"
        print(message)
        return message

if __name__ == '__main__':
    donald = Duck()
    
    print("Donald the Duck's abilities:")
    donald.fly()
    donald.swim()
    donald.quack() 