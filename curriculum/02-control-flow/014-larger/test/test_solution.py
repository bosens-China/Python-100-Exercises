# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.larger(4, 9) == 9


def test_case_02():
    assert student.larger(-2, -8) == -2


def test_case_03():
    assert student.larger(5, 5) == 5
