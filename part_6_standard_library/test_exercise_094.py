import unittest
from part_6_standard_library.exercise_094 import find_email_in_text

class TestRegexEmail(unittest.TestCase):
    def test_simple_email(self):
        """测试一个简单的电子邮件地址。"""
        text = "My email is test@example.com, please contact me."
        self.assertEqual(find_email_in_text(text), "test@example.com")

    def test_email_with_hyphen(self):
        """测试域名中包含连字符的电子邮件地址。"""
        text = "Contact us at support@my-company.co.uk for help."
        self.assertEqual(find_email_in_text(text), "support@my-company.co.uk")

    def test_email_with_numbers(self):
        """测试用户名和域名中包含数字的电子邮件地址。"""
        text = "My address is user123@123domain.net."
        self.assertEqual(find_email_in_text(text), "user123@123domain.net")
        
    def test_email_with_plus_symbol(self):
        """测试用户名中包含加号的电子邮件地址。"""
        text = "Please use this address: user+tag@gmail.com"
        self.assertEqual(find_email_in_text(text), "user+tag@gmail.com")

    def test_no_email_in_text(self):
        """测试不包含电子邮件地址的文本。"""
        text = "This is a string with no email address."
        self.assertIsNone(find_email_in_text(text))

    def test_invalid_email(self):
        """测试一些无效的电子邮件地址格式。"""
        self.assertIsNone(find_email_in_text("this is not an email @example.com"))
        self.assertIsNone(find_email_in_text("test@.com"))
        self.assertIsNone(find_email_in_text("test@domain"))
        
    def test_multiple_emails(self):
        """测试包含多个电子邮件地址的文本（应只返回第一个）。"""
        text = "My emails are first@example.com and second@example.org."
        self.assertEqual(find_email_in_text(text), "first@example.com")

if __name__ == '__main__':
    unittest.main() 