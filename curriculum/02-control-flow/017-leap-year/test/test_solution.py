# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.is_leap(2000) is True


def test_case_02():
    assert student.is_leap(1900) is False


def test_case_03():
    assert student.is_leap(2024) is True
    assert student.is_leap(2023) is False
