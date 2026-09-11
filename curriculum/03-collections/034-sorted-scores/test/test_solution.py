# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    scores = [70, 90, 70]
    assert student.rank_scores(scores) == [90, 70, 70]
    assert scores == [70, 90, 70]


def test_case_02():
    assert student.rank_scores([]) == []


def test_case_03():
    assert student.rank_scores([-1, 0, 2]) == [2, 0, -1]
