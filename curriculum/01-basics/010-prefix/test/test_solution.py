# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.preview("Python", 3) == "Pyt"


def test_case_02():
    assert student.preview("你好", 10) == "你好"


def test_case_03():
    assert student.preview("abc", 0) == ""


def test_case_04():
    assert student.preview("", 4) == ""
