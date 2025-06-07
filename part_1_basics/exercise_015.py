"""
### 15. 列表切片

- **描述:** 给定一个列表 `numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`，提取索引从 2 到 6（不包含 6）的元素。
- **提示:** 使用列表切片 `numbers[start:end]`。
- **期待:** `print(sub_list)` 输出 `[2, 3, 4, 5]`。
"""

def get_list_slice(numbers):
    """
    获取列表从索引 2 到 6 (不含) 的切片
    :param numbers: 输入列表
    :return: 子列表
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    sub = get_list_slice(num_list)
    print(f"从 {num_list} 中切片的结果是: {sub}") 