# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    store = student.Store()
    a = store.add("A")
    b = store.add("B")
    assert store.list() == [a, b]
    assert store.list(False) == [a, b]
    assert store.list(True) == []


def test_case_02():
    store = student.Store()
    record = store.add("A")
    record["title"] = "changed"
    result = store.list()
    result[0]["done"] = True
    assert store.list() == [{"id": 1, "title": "A", "done": False}]


def test_case_03():
    store = student.Store()
    assert store.list() == []
    for done in [0, 1, "false"]:
        with raises(ValueError):
            store.list(done)
