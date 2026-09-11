# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.check_shipping(lambda amount: 0 if amount >= 9900 else 800) is None


def test_case_02():
    with raises(AssertionError):
        student.check_shipping(lambda amount: 0 if amount > 9900 else 800)


def test_case_03():
    with raises(AssertionError):
        student.check_shipping(lambda amount: 0)


def test_case_04():
    with raises(AssertionError):
        student.check_shipping(lambda amount: 800)
