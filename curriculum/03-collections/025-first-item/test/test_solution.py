# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.first_item([4, 8]) == 4


def test_case_02():
    assert student.first_item([]) is None


def test_case_03():
    assert student.first_item([0]) == 0
