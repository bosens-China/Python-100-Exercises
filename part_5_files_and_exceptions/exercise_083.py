"""
### 83. `else` 和 `finally` 子句

- **描述:** 修改第 82 题的函数。使用 `else` 块在没有发生异常时打印 "计算成功"。使用 `finally` 块无论是否发生异常都打印 "计算结束"。
- **提示:** `else` 块在 `try` 块成功执行后执行。`finally` 块总是最后执行。
- **期待:**
  - `divide(10, 2)` 会打印 "计算成功" 和 "计算结束"。
  - `divide(10, 0)` 会打印错误信息和 "计算结束"。
"""

def divide_with_else_finally(a, b):
    """
    计算 a / b 的商，并使用 else 和 finally 子句。
    :param a: 被除数
    :param b: 除数
    :return: 商（浮点数），如果发生错误则返回 None。
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    print("--- 正常计算 ---")
    divide_with_else_finally(10, 2)
        
    print("\n--- 除以零 ---")
    divide_with_else_finally(10, 0)

    print("\n--- 类型错误 ---")
    divide_with_else_finally(10, "a") 