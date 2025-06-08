import unittest
from part_3_functions.exercise_059 import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_string_palindrome(self):
        self.assertTrue(is_palindrome("madam"))

    def test_string_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_number_palindrome(self):
        self.assertTrue(is_palindrome(12321))

    def test_number_not_palindrome(self):
        self.assertFalse(is_palindrome(12345))

    def test_case_sensitivity(self):
        # 回文检查通常是大小写敏感的
        self.assertFalse(is_palindrome("Madam"))

    def test_string_with_spaces(self):
        # "taco cat" 不是一个严格的回文
        # 如果需要处理空格，函数逻辑需要修改
        self.assertFalse(is_palindrome("taco cat"))
        self.assertTrue(is_palindrome("taco cat".replace(" ", "")))
        
    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome(7))
        
    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

if __name__ == '__main__':
    unittest.main() 