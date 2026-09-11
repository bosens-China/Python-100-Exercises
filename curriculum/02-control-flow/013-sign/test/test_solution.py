# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.sign(5) == "正数"


def test_case_02():
    assert student.sign(-3) == "负数"


def test_case_03():
    assert student.sign(0) == "零"
