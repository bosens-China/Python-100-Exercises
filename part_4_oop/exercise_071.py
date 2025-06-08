"""
### 71. 特殊方法 `__repr__`

- **描述:** 在 `Dog` 类中实现 `__repr__` 方法，它应该返回一个可以用来重新创建该对象的官方字符串表示。
- **提示:** `def __repr__(self): return f"Dog(name='{self.name}', age={self.age})"`。
- **期待:** 在 Python 解释器中直接输入 `my_dog` 对象，会显示 `Dog(name='Fido', age=5)`。
"""

class Dog:
    """
    一个代表狗的类，实现了 __str__ 和 __repr__ 方法。
    """
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def __str__(self) -> str:
        """返回一个非正式的、适合给用户看的字符串表示。"""
        return f"{self.name} is a {self.age}-year-old dog."

    def __repr__(self) -> str:
        """
        返回一个官方的、明确的字符串表示。
        理想情况下，eval(repr(instance)) == instance。
        当直接在解释器中输入变量名时，或在容器（如列表）中打印对象时被触发。
        """
        # 在这里写下你的代码
        return f"Dog(name='{self.name}', age={self.age})"

if __name__ == '__main__':
    my_dog = Dog("Fido", 5)
    
    print("--- 比较 __str__ 和 __repr__ ---")
    print(f"str(my_dog):  {str(my_dog)}")
    print(f"repr(my_dog): {repr(my_dog)}")
    
    print("\n--- 在容器中打印对象 ---")
    dog_list = [my_dog]
    # 在容器中，对象的 __repr__ 会被调用
    print(dog_list)

    print("\n--- 演示 eval(repr(obj)) ---")
    # repr 的输出可以用来重新创建对象
    repr_str = repr(my_dog)
    recreated_dog = eval(repr_str)
    print(f"Recreated dog's name: {recreated_dog.name}")
 