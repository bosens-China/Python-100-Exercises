# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    left = {"笔": 2}
    right = {"笔": 3, "本": 1}
    assert student.merge_stock(left, right) == {"笔": 5, "本": 1}
    assert left == {"笔": 2}
    assert right == {"笔": 3, "本": 1}


def test_case_02():
    assert student.merge_stock({}, {}) == {}


def test_case_03():
    assert student.merge_stock({"a": 0}, {}) == {"a": 0}
