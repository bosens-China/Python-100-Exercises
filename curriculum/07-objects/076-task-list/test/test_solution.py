# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    tasks = student.TaskList()
    assert tasks.add("A") == 0
    assert tasks.add("B") == 1
    assert tasks.complete(0) is None
    tasks.complete(0)
    assert tasks.pending() == ["B"]


def test_case_02():
    tasks = student.TaskList()
    assert tasks.pending() == []
    with raises(IndexError):
        tasks.complete(0)


def test_case_03():
    tasks = student.TaskList()
    tasks.add("A")
    for index in [-1, 1]:
        with raises(IndexError):
            tasks.complete(index)
    assert tasks.pending() == ["A"]


def test_case_04():
    a = student.TaskList()
    b = student.TaskList()
    a.add("A")
    assert b.pending() == []
