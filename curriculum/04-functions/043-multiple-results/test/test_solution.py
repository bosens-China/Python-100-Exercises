# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.divide(7, 3) == (2, 1)


def test_case_02():
    assert student.divide(0, 4) == (0, 0)


def test_case_03():
    assert student.divide(8, 4) == (2, 0)
