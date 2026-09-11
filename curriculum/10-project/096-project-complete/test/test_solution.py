# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    store = student.Store()
    store.add("A")
    store.add("B")
    expected = {"id": 1, "title": "A", "done": True}
    assert store.complete(1) == expected
    assert store.complete(1) == expected
    assert store.list(True) == [expected]
    assert store.list(False) == [{"id": 2, "title": "B", "done": False}]


def test_case_02():
    store = student.Store()
    store.add("A")
    for identifier in [999, True, "1"]:
        with raises(KeyError):
            store.complete(identifier)
    assert store.list()[0]["done"] is False


def test_case_03():
    store = student.Store()
    store.add("A")
    record = store.complete(1)
    record["done"] = False
    assert store.list()[0]["done"] is True
