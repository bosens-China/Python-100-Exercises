# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    account = student.Account(100)
    assert account.deposit(20) == 120
    assert account.withdraw(120) == 0
    assert account.balance == 0


def test_case_02():
    account = student.Account(50)
    for amount in [0, -1, 51]:
        with raises(ValueError):
            account.withdraw(amount)
        assert account.balance == 50


def test_case_03():
    account = student.Account()
    for amount in [0, -1]:
        with raises(ValueError):
            account.deposit(amount)
    assert account.balance == 0
    with raises(ValueError):
        student.Account(-1)


def test_case_04():
    a = student.Account()
    b = student.Account()
    a.deposit(1)
    assert b.balance == 0
