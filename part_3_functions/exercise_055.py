"""
### 55. 装饰器

- **描述:** 编写一个简单的装饰器 `my_decorator`，它在被装饰的函数执行前后各打印一条消息。
- **提示:** 装饰器是一个接受函数作为参数并返回一个新函数的函数。
- **期待:**

  ```python
  @my_decorator
  def say_hello():
      print("Hello!")

  say_hello()
  # 输出:
  # Something is happening before the function is called.
  # Hello!
  # Something is happening after the function is called.
  ```
"""

def my_decorator(func):
    """
    一个简单的装饰器，在函数执行前后打印消息。
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    @my_decorator
    def say_hello():
        print("Hello!")
    
    say_hello()