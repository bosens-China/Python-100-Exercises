import unittest
from collections import Counter
from part_6_standard_library.exercise_093 import count_character_frequency

class TestCollectionsCounter(unittest.TestCase):
    def test_basic_string(self):
        """测试一个基本的字符串。"""
        s = "abracadabra"
        expected = Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
        self.assertEqual(count_character_frequency(s), expected)

    def test_string_with_spaces_and_cases(self):
        """测试包含空格和不同大小写的字符串。"""
        s = "Hello World"
        # Counter 是区分大小写的
        expected = Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})
        self.assertEqual(count_character_frequency(s), expected)

    def test_empty_string(self):
        """测试空字符串。"""
        s = ""
        expected = Counter()
        self.assertEqual(count_character_frequency(s), expected)
        
    def test_string_with_all_same_characters(self):
        """测试所有字符都相同的字符串。"""
        s = "aaaaa"
        expected = Counter({'a': 5})
        self.assertEqual(count_character_frequency(s), expected)

if __name__ == '__main__':
    unittest.main() 