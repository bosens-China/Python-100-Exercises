# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.select([1, 2, 3], lambda n: n > 1) == [2, 3]


def test_case_02():
    assert student.select([2, 2, 3], lambda n: n % 2 == 0) == [2, 2]


def test_case_03():
    assert student.select([], lambda n: True) == []
