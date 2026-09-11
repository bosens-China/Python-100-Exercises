# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.checkout(100, 2, 80) == 280


def test_case_02():
    assert student.subtotal(5, 3) == 15


def test_case_03():
    assert student.checkout(0, 2, 80) == 80
    assert student.checkout(9, 0, 0) == 0
