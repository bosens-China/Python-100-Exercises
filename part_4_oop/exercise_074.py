"""
### 74. 多重继承

- **描述:** 创建一个 `Flyable` 类（有 `fly` 方法）和一个 `Swimmable` 类（有 `swim` 方法）。然后创建一个 `Duck` 类，它同时继承这两个类。
- **提示:** `class Duck(Flyable, Swimmable):`
- **期待:** `duck = Duck()`，`duck.fly()` 和 `duck.swim()` 都能被成功调用。
"""

class Flyable:
    """一个代表能飞的Mixin类。"""
    # 在这里写下你的代码
    pass

class Swimmable:
    """一个代表能游泳的Mixin类。"""
    # 在这里写下你的代码
    pass


if __name__ == '__main__':
    # 当你定义好 Duck 类后，下面的代码应该可以正常运行
    donald = Duck()
    
    print("Donald the Duck's abilities:")
    donald.fly()
    donald.swim()
    # 如果你添加了 quack 方法，也可以在这里调用
    # donald.quack() 