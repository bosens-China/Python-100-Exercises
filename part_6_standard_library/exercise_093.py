"""
### 93. `collections` 模块

- **描述:** 使用 `collections.Counter` 快速统计一个字符串中每个字符的出现次数。
- **提示:** `from collections import Counter; Counter("abracadabra")`。
- **期待:** 返回一个类似 `Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})` 的对象。
"""
from collections import Counter

def count_character_frequency(s: str) -> Counter:
    """
    使用 collections.Counter 统计字符串中每个字符的出现次数。
    :param s: 输入字符串
    :return: 一个 Counter 对象
    """
    # 在这里写下你的代码
    return Counter(s)

if __name__ == '__main__':
    test_string = "abracadabra"
    frequency = count_character_frequency(test_string)
    
    print(f"字符串 '{test_string}' 的字符频率是:")
    print(frequency)
    
    # Counter 对象的行为很像字典
    print(f"字母 'a' 出现了 {frequency['a']} 次")
    print(f"字母 'z' 出现了 {frequency['z']} 次") # 不存在的键返回 0，而不是抛出 KeyError
    
    # most_common() 是一个很有用的方法
    print("出现频率最高的两个字符是:")
    print(frequency.most_common(2)) 