# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.transform_all([1, 2], lambda x: x * 2) == [2, 4]


def test_case_02():
    assert student.transform_all([2, 4], lambda x: str(x)) == ["2", "4"]


def test_case_03():
    calls = []
    assert student.transform_all([], lambda x: calls.append(x)) == []
    assert calls == []
