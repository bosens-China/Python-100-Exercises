# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    cart = student.Cart()
    assert cart.add(student.Product("笔", 100), 2) is None
    cart.add(student.Product("本", 200))
    assert cart.total() == 400


def test_case_02():
    assert student.Cart().total() == 0


def test_case_03():
    a = student.Cart()
    b = student.Cart()
    a.add(student.Product("笔", 100))
    assert b.total() == 0


def test_case_04():
    cart = student.Cart()
    product = student.Product("赠品", 0)
    cart.add(product, 3)
    assert cart.total() == 0
