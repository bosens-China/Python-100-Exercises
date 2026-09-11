# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.active_names(
        [{"name": "Ada", "active": True}, {"name": "Bo", "active": False}]
    ) == ["Ada"]


def test_case_02():
    assert student.active_names([]) == []


def test_case_03():
    assert student.active_names(
        [{"name": "A", "active": True}, {"name": "A", "active": True}]
    ) == ["A", "A"]
