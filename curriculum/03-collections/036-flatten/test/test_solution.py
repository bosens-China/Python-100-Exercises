# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.flatten([[1, 2], [], [3]]) == [1, 2, 3]


def test_case_02():
    assert student.flatten([]) == []


def test_case_03():
    assert student.flatten([[], []]) == []


def test_case_04():
    assert student.flatten([[1], [1]]) == [1, 1]
