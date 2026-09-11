# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    store = student.Store()
    store.add("A")
    store.add("B")
    assert store.delete(2) is True
    assert store.delete(2) is False
    assert store.add("C")["id"] == 3
    assert [row["id"] for row in store.list()] == [1, 3]


def test_case_02():
    store = student.Store()
    store.add("A")
    for identifier in [999, True, "1"]:
        assert store.delete(identifier) is False
    assert len(store.list()) == 1


def test_case_03():
    store = student.Store()
    store.add("A")
    store.delete(1)
    assert store.list() == []
    assert store.add("B")["id"] == 2
