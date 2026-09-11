# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    tasks = [
        {"id": 1, "title": "A", "done": False},
        {"id": 2, "title": "B", "done": True},
    ]
    assert student.filter_tasks(tasks, "false") == [tasks[0]]
    assert student.filter_tasks(tasks, "true") == [tasks[1]]
    assert student.filter_tasks(tasks) == tasks


def test_case_02():
    with raises(ValueError):
        student.filter_tasks([], "False")
    with raises(ValueError):
        student.filter_tasks([], "")


def test_case_03():
    tasks = [{"id": 1, "title": "A", "done": False}]
    result = student.filter_tasks(tasks)
    result[0]["title"] = "changed"
    assert tasks[0]["title"] == "A"
    assert student.filter_tasks([]) == []
