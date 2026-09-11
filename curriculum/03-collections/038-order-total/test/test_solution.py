# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert (
        student.order_total(
            [{"price": 150, "quantity": 2}, {"price": 90, "quantity": 3}]
        )
        == 570
    )


def test_case_02():
    assert student.order_total([]) == 0


def test_case_03():
    items = [{"price": 0, "quantity": 9}, {"price": 3, "quantity": 0}]
    assert student.order_total(items) == 0
    assert items == [{"price": 0, "quantity": 9}, {"price": 3, "quantity": 0}]
