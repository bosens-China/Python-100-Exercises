# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    task = student.Task("学习")
    assert task.to_dict() == {"title": "学习", "done": False}
    assert task.complete() is None
    task.complete()
    assert task.to_dict() == {"title": "学习", "done": True}


def test_case_02():
    task = student.Task("A")
    data = task.to_dict()
    data["done"] = True
    assert task.done is False


def test_case_03():
    a = student.Task("A")
    b = student.Task("B")
    a.complete()
    assert b.done is False
