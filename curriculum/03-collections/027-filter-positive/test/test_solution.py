# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.positive_numbers([-1, 2, 0, 2]) == [2, 2]


def test_case_02():
    assert student.positive_numbers([]) == []


def test_case_03():
    assert student.positive_numbers([-3, 0]) == []
