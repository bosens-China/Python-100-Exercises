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
    def decorator_repeat(func):
        # 使用 *args 和 **kwargs 使包装器可以接受任意参数
        def wrapper(*args, **kwargs):
            # 为了方便测试，我们将函数的结果收集到一个列表中返回
            results = []
            for _ in range(num_times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    """
    一个简单的问候函数，为了测试，它将返回字符串而不是直接打印。
    """
    print(f"Hello {name}") # 保留打印行为以符合题目描述
    return f"Hello {name}"

@repeat(num_times=2)
def add(a, b):
    """
    一个简单的加法函数，返回结果。
    """
    return a + b


if __name__ == '__main__':
    print("--- Calling greet('World') decorated with @repeat(num_times=3) ---")
    greet_results = greet("World")
    print(f"Function returned: {greet_results}")
    
    print("\n" + "="*40 + "\n")

    print("--- Calling add(5, 10) decorated with @repeat(num_times=2) ---")
    add_results = add(5, 10)
    print(f"Function returned: {add_results}") 