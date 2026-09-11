# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.greet() == "你好，朋友"


def test_case_02():
    assert student.greet("小王") == "你好，小王"


def test_case_03():
    assert student.greet(name="") == "你好，"
