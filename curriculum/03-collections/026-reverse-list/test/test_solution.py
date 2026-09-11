# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    items = [1, 2, 3]
    assert student.reversed_copy(items) == [3, 2, 1]
    assert items == [1, 2, 3]


def test_case_02():
    items = []
    result = student.reversed_copy(items)
    assert result == []
    assert result is not items


def test_case_03():
    assert student.reversed_copy([5]) == [5]
