# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.countdown(3) == "3 2 1 开始"


def test_case_02():
    assert student.countdown(0) == "开始"


def test_case_03():
    assert student.countdown(1) == "1 开始"
