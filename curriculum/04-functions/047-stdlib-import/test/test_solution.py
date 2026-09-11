# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.square_side(15) == 3


def test_case_02():
    assert student.square_side(0) == 0
    assert student.square_side(16) == 4


def test_case_03():
    assert student.square_side(10**40 - 1) == 10**20 - 1
