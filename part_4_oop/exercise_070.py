"""
### 70. 特殊方法 (魔术方法) `__str__`

- **描述:** 在第 61 题的 `Dog` 类中实现 `__str__` 方法，使得 `print(my_dog)` 时能输出一条可读性好的描述信息。
- **提示:** `def __str__(self): return f"{self.name} is a {self.age}-year-old dog."`
- **期待:** `my_dog = Dog("Fido", 5)`，`print(my_dog)` 输出 `Fido is a 5-year-old dog.`。
"""

class Dog:
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    my_dog = Dog("Fido", 5)
    
    # 当 print() 函数作用于一个对象时，它会调用该对象的 __str__ 方法
    print(my_dog)
    
    # str() 函数也会调用 __str__ 方法
    dog_description = str(my_dog)
    print(f"The description is: '{dog_description}'") 