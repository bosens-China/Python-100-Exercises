import unittest
from part_1_basics.exercise_014 import modify_list

class TestExercise14(unittest.TestCase):
    def test_modify_list(self):
        fruits = ["apple", "banana", "cherry"]
        # 函数可能会修改原始列表，所以我们传递一个副本进行测试
        modified = modify_list(fruits[:])
        self.assertEqual(modified, ['apple', 'grape', 'banana', 'cherry', 'orange'])

        # 测试一个不同的列表
        items = ["a", "b", "c"]
        # 假设逻辑是添加到末尾和在第一个元素后插入
        # 这里我们假设添加的元素是固定的 "orange" 和 "grape"
        # 如果题目意图更通用，测试用例需要调整
        # 根据当前题目描述，我们硬编码测试这个特定操作
        items_modified = modify_list(["apple", "b", "c"])
        self.assertEqual(items_modified, ['apple', 'grape', 'b', 'c', 'orange'])


if __name__ == '__main__':
    unittest.main() 