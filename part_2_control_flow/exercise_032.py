"""
### 32. `for-else` 循环

- **描述:** 使用 `for-else` 循环在一个列表中查找一个数字。如果找到了，打印 "找到了"；如果循环正常结束（没有被 `break`），则打印 "没找到"。
- **提示:** `else` 子句在 `for` 循环正常执行完毕后执行。
- **期待:**
  - 在 `[1, 2, 3, 4]` 中查找 `3`，输出 `找到了`。
  - 在 `[1, 2, 3, 4]` 中查找 `5`，输出 `没找到`。
"""

def search_in_list(numbers, target):
    """
    在列表中查找一个数字，并根据结果返回不同消息。
    :param numbers: 数字列表
    :param target: 要查找的数字
    :return: 字符串 "找到了" 或 "没找到"
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    my_list = [1, 2, 3, 4]
    
    target1 = 3
    result1 = search_in_list(my_list, target1)
    print(f"在 {my_list} 中查找 {target1}: {result1}")
    
    target2 = 5
    result2 = search_in_list(my_list, target2)
    print(f"在 {my_list} 中查找 {target2}: {result2}") 