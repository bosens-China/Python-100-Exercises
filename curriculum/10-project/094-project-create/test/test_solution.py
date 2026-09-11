# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    store = student.Store()
    assert store.add(" A ") == {"id": 1, "title": "A", "done": False}
    assert store.add("B")["id"] == 2


def test_case_02():
    store = student.Store()
    with raises(ValueError):
        store.add(" ")
    assert store.add("A")["id"] == 1


def test_case_03():
    first = student.Store()
    second = student.Store()
    first.add("A")
    assert second.add("B")["id"] == 1


def test_case_04():
    store = student.Store()
    record = store.add("A")
    record["id"] = 99
    assert store.add("B")["id"] == 2
