from part_2_control_flow.exercise_034 import simple_login

CORRECT_USER = "admin"
CORRECT_PASS = "password123"

def test_login_success():
    """测试成功登录"""
    assert simple_login(CORRECT_USER, CORRECT_PASS, "admin", "password123") == "登录成功！"

def test_login_wrong_username():
    """测试用户名错误"""
    assert simple_login(CORRECT_USER, CORRECT_PASS, "user", "password123") == "用户名或密码错误！"

def test_login_wrong_password():
    """测试密码错误"""
    assert simple_login(CORRECT_USER, CORRECT_PASS, "admin", "wrongpass") == "用户名或密码错误！"

def test_login_wrong_both():
    """测试用户名和密码都错误"""
    assert simple_login(CORRECT_USER, CORRECT_PASS, "user", "wrongpass") == "用户名或密码错误！"