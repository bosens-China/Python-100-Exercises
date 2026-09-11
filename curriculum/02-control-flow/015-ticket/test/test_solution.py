# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.ticket_price(0) == 0
    assert student.ticket_price(5) == 0


def test_case_02():
    assert student.ticket_price(6) == 1000
    assert student.ticket_price(17) == 1000


def test_case_03():
    assert student.ticket_price(18) == 2000
    assert student.ticket_price(64) == 2000


def test_case_04():
    assert student.ticket_price(65) == 1000
