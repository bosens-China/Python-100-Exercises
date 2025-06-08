"""
### 82. 处理特定类型的异常

- **描述:** 编写一个函数，接受两个数并返回它们的商。使用 `try-except` 来分别处理 `ZeroDivisionError` 和 `TypeError`（例如当输入不是数字时）。
- **提示:** 可以有多个 `except` 块来捕获不同类型的异常。
- **期待:**
  - `divide(10, 2)` 返回 `5.0`。
  - `divide(10, 0)` 打印 "错误：除数不能为零！"。
  - `divide(10, "a")` 打印 "错误：输入必须是数字！"。
"""
from typing import Union

def divide(a, b) -> Union[float, str]:
    """
    计算 a / b 的商。
    - 如果成功，返回浮点数结果。
    - 如果发生 ZeroDivisionError，返回 "错误：除数不能为零！"。
    - 如果发生 TypeError，返回 "错误：输入必须是数字！"。
    
    :param a: 被除数。
    :param b: 除数。
    :return: 计算结果或错误消息。
    """
    # 在这里写下你的代码
    raise NotImplementedError 