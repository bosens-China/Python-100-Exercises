# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.count_char("banana", "a") == 3


def test_case_02():
    assert student.count_char("AaA", "a") == 1


def test_case_03():
    assert student.count_char("", "x") == 0
