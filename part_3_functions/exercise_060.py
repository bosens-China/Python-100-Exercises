"""
### 60. 编写一个排序函数

- **描述:** 不使用内置的 `sort()` 方法或 `sorted()` 函数，编写一个函数来实现一个简单的排序算法（如冒泡排序）来对一个数字列表进行升序排序。
- **提示:** 冒泡排序通过重复遍历列表，比较相邻元素并交换位置来实现。
- **期待:** 对于列表 `[5, 1, 4, 2, 8]`，函数返回 `[1, 2, 4, 5, 8]`。
"""
from typing import List

def bubble_sort(numbers: List[float]) -> List[float]:
    """
    使用冒泡排序算法对一个数字列表进行升序排序。
    :param numbers: 一个数字列表
    :return: 排序后的新列表（为了不修改原始列表）
    """
    # 创建一个列表副本以避免修改原始列表
    nums = numbers[:]
    n = len(nums)
    
    # 冒泡排序逻辑
    # 在这里写下你的代码
    for i in range(n):
        # 标志位，用于优化：如果在一轮中没有发生交换，说明列表已经有序
        swapped = False
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                # 交换元素
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
            
    return nums

if __name__ == '__main__':
    my_list = [5, 1, 4, 2, 8]
    sorted_list = bubble_sort(my_list)
    print(f"原始列表: {my_list}")
    print(f"排序后的列表: {sorted_list}")
    
    another_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"原始列表: {another_list}")
    print(f"排序后的列表: {bubble_sort(another_list)}") 