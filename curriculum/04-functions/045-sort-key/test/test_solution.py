# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    tasks = [{"title": "B", "priority": 2}, {"title": "A", "priority": 1}]
    assert student.sort_tasks(tasks) == [tasks[1], tasks[0]]
    assert tasks[0]["title"] == "B"


def test_case_02():
    tasks = [{"title": "Z", "priority": 1}, {"title": "A", "priority": 1}]
    assert student.sort_tasks(tasks) == tasks


def test_case_03():
    assert student.sort_tasks([]) == []
