import unittest
from part_2_control_flow.exercise_034 import simple_login

class TestExercise34(unittest.TestCase):
    def setUp(self):
        self.correct_user = "admin"
        self.correct_pass = "password123"

    def test_login_success(self):
        self.assertEqual(simple_login(self.correct_user, self.correct_pass, "admin", "password123"), "登录成功！")

    def test_login_wrong_username(self):
        self.assertEqual(simple_login(self.correct_user, self.correct_pass, "user", "password123"), "用户名或密码错误！")

    def test_login_wrong_password(self):
        self.assertEqual(simple_login(self.correct_user, self.correct_pass, "admin", "wrongpass"), "用户名或密码错误！")

    def test_login_wrong_both(self):
        self.assertEqual(simple_login(self.correct_user, self.correct_pass, "user", "wrongpass"), "用户名或密码错误！")

if __name__ == '__main__':
    unittest.main() 