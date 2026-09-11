# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.receipt("笔", 150, 2) == "笔 × 2 = 300分"


def test_case_02():
    assert student.receipt("书", 2000, 0) == "书 × 0 = 0分"


def test_case_03():
    assert student.receipt("赠品", 0, 3) == "赠品 × 3 = 0分"
