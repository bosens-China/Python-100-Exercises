"""
### 71. 特殊方法 `__repr__`

- **描述:** 在 `Dog` 类中实现 `__repr__` 方法，它应该返回一个可以用来重新创建该对象的官方字符串表示。
- **提示:** `def __repr__(self): return f"Dog(name='{self.name}', age={self.age})"`。
- **期待:** 在 Python 解释器中直接输入 `my_dog` 对象，会显示 `Dog(name='Fido', age=5)`。
"""

class Dog:
    # 在这里写下你的代码
    pass

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
 