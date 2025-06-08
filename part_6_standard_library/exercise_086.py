"""
### 86. `random` 模块

- **描述:** 使用 `random` 模块生成一个包含 5 个随机整数的列表，整数范围在 1 到 20 之间。然后再从列表 `["apple", "banana", "cherry"]` 中随机选择一个水果。
- **提示:** 使用 `random.randint(a, b)` 和 `random.choice(sequence)`。
- **期待:** 每次运行都会得到不同的随机列表和水果。
"""
import random
from typing import List, Any

def generate_random_integer_list(n: int, min_val: int, max_val: int) -> List[int]:
    """
    生成一个包含 n 个在 [min_val, max_val] 范围内的随机整数的列表。
    """
    # 在这里写下你的代码
    raise NotImplementedError

def choose_random_item(items: List[Any]) -> Any:
    """
    从列表中随机选择一个元素。
    """
    # 在这里写下你的代码
    raise NotImplementedError

if __name__ == '__main__':
    # 生成随机整数列表
    random_integers = generate_random_integer_list(5, 1, 20)
    print(f"随机整数列表: {random_integers}")
    
    # 随机选择水果
    fruits = ["apple", "banana", "cherry"]
    random_fruit = choose_random_item(fruits)
    print(f"随机选择的水果: {random_fruit}") 