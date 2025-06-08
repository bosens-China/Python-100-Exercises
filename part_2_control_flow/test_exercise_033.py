from part_2_control_flow.exercise_033 import password_checker

CORRECT_PASSWORD = "password123"

def test_login_successful_on_first_try():
    """测试第一次就输入正确密码"""
    inputs = ["password123"]
    assert password_checker(CORRECT_PASSWORD, inputs) == "登录成功"

def test_login_successful_on_third_try():
    """测试第三次输入正确密码"""
    inputs = ["wrong", "still_wrong", "password123"]
    assert password_checker(CORRECT_PASSWORD, inputs) == "登录成功"

def test_login_failed():
    """测试三次均输入错误密码"""
    inputs = ["wrong", "still_wrong", "wrong_again"]
    assert password_checker(CORRECT_PASSWORD, inputs) == "尝试次数过多，账户已锁定"

def test_login_failed_with_more_inputs():
    """测试提供多于三次错误输入的情况"""
    # 即使提供了多于3个的错误输入，也应该在3次后锁定
    inputs = ["wrong", "still_wrong", "wrong_again", "password123"]
    assert password_checker(CORRECT_PASSWORD, inputs) == "尝试次数过多，账户已锁定"

def test_login_successful_with_fewer_inputs():
    """测试在两次内成功登录的情况"""
    # 如果在两次内成功，不应该继续消耗输入
    inputs = ["wrong", "password123"]
    assert password_checker(CORRECT_PASSWORD, inputs) == "登录成功" 