"""
### 56. 带参数的装饰器

- **描述:** 编写一个带参数的装饰器 `repeat(num_times)`，它会让被装饰的函数重复执行 `num_times` 次。
- **提示:** 需要三层函数嵌套。最外层函数接受装饰器参数，返回一个装饰器，该装饰器再返回包装函数。
- **期待:**

  ```python
  @repeat(num_times=3)
  def greet(name):
      print(f"Hello {name}")

  greet("World")
  # 输出:
  # Hello World
  # Hello World
  # Hello World
  ```
"""

def repeat(num_times):
    """
    带参数的装饰器，用于重复执行一个函数。
    :param num_times: 函数需要被执行的次数
    """
    # 在这里写下你的代码
    pass


if __name__ == '__main__':
    @repeat(num_times=3)
    def greet(name):
        print(f"Hello {name}")
    
    greet("World")
