# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.can_edit(None, 1) is False


def test_case_02():
    assert student.can_edit({"id": 2, "role": "member"}, 2) is True


def test_case_03():
    assert student.can_edit({"id": 2, "role": "admin"}, 1) is True


def test_case_04():
    assert student.can_edit({"id": 2, "role": "member"}, 1) is False
