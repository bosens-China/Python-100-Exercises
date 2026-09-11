# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.task_id("/tasks/007") == 7


def test_case_02():
    for path in ["/tasks/", "/tasks/0", "/tasks/-1", "/tasks/1/", "/tasks/1/edit"]:
        assert student.task_id(path) is None, path


def test_case_03():
    for path in ["/users/1", "/tasks/1?x=2", "/tasks/１２"]:
        assert student.task_id(path) is None, path
