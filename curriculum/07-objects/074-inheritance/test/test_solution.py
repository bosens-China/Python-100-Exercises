# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    member = student.MemberCustomer("Ada")
    assert isinstance(member, student.Customer)
    assert member.name == "Ada"
    assert member.payable(105) == 94


def test_case_02():
    assert student.MemberCustomer("A").payable(0) == 0


def test_case_03():
    assert student.Customer("A").payable(105) == 105
