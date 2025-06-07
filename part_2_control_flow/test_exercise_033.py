import unittest
from part_2_control_flow.exercise_033 import password_checker

class TestExercise33(unittest.TestCase):
    def setUp(self):
        self.correct_password = "password123"

    def test_login_successful_on_first_try(self):
        inputs = ["password123"]
        self.assertEqual(password_checker(self.correct_password, inputs), "登录成功")

    def test_login_successful_on_third_try(self):
        inputs = ["wrong", "still_wrong", "password123"]
        self.assertEqual(password_checker(self.correct_password, inputs), "登录成功")

    def test_login_failed(self):
        inputs = ["wrong", "still_wrong", "wrong_again"]
        self.assertEqual(password_checker(self.correct_password, inputs), "尝试次数过多，账户已锁定")
    
    def test_login_failed_with_more_inputs(self):
        # 即使提供了多于3个的错误输入，也应该在3次后锁定
        inputs = ["wrong", "still_wrong", "wrong_again", "password123"]
        self.assertEqual(password_checker(self.correct_password, inputs), "尝试次数过多，账户已锁定")

    def test_login_successful_with_fewer_inputs(self):
        # 如果在两次内成功，不应该继续消耗输入
        inputs = ["wrong", "password123"]
        self.assertEqual(password_checker(self.correct_password, inputs), "登录成功")

if __name__ == '__main__':
    unittest.main() 