# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.summarize([2, 4]) == {"count": 2, "total": 6, "mean": 3.0}


def test_case_02():
    assert student.summarize([]) == {"count": 0, "total": 0, "mean": None}


def test_case_03():
    assert student.total([-1, 3]) == 2
    assert student.mean([1, 2]) == 1.5
