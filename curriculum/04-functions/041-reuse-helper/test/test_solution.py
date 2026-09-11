# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.line_total(100, 3) == 300
    assert student.line_total(0, 2) == 0


def test_case_02():
    assert student.cart_total([]) == 0


def test_case_03():
    assert (
        student.cart_total([{"price": 20, "quantity": 2}, {"price": 30, "quantity": 1}])
        == 70
    )
