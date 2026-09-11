# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.paginate([1, 2, 3, 4, 5], 1, 2) == [1, 2]


def test_case_02():
    assert student.paginate([1, 2, 3, 4, 5], 2, 2) == [3, 4]


def test_case_03():
    assert student.paginate([1, 2, 3, 4, 5], 3, 2) == [5]


def test_case_04():
    assert student.paginate([], 1, 2) == []
    assert student.paginate([1], 9, 2) == []
