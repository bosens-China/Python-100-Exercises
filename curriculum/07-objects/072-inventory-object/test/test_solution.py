# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    inventory = student.Inventory({"笔": 2})
    assert inventory.add("笔", 3) == 5
    assert inventory.add("本", 0) == 0
    assert inventory.snapshot() == {"笔": 5, "本": 0}


def test_case_02():
    original = {"a": 1}
    inventory = student.Inventory(original)
    original["a"] = 9
    assert inventory.snapshot() == {"a": 1}


def test_case_03():
    inventory = student.Inventory({"a": 1})
    copy = inventory.snapshot()
    copy["a"] = 100
    assert inventory.snapshot() == {"a": 1}
