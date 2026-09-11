"""
题目 046: 编写一个简单的日志记录装饰器

要求:
编写一个名为 `log_call` 的装饰器。
当它被应用到一个函数上时，在函数执行前打印 `Calling function '[function_name]'...`，
在函数执行后打印 `Function '[function_name]' finished.`。
装饰器必须能正确处理原函数的参数和返回值。

提示:
你需要使用 `functools.wraps` 来保持原函数的信息。
装饰器内部的包装函数需要能接受 `*args` 和 `**kwargs`。
"""
import functools

def log_call(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 在这里写下你的代码
        pass
    return wrapper

# 这是一个带参数的示例函数，你可以用它来测试你的装饰器
@log_call
def add(a, b):
    return a + b
