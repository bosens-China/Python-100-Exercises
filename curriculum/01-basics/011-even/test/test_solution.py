# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.is_even(-4) is True


def test_case_02():
    assert student.is_even(0) is True


def test_case_03():
    assert student.is_even(7) is False
