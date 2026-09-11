# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.new_task(1, " 学习 ") == {"id": 1, "title": "学习", "done": False}


def test_case_02():
    for title in [None, 1, " ", "a" * 81]:
        with raises(ValueError):
            student.new_task(1, title)


def test_case_03():
    for identifier in [0, -1, True, "1", 1.0]:
        with raises(ValueError):
            student.new_task(identifier, "A")


def test_case_04():
    assert student.normalize_title("a" * 80) == "a" * 80
    a = student.new_task(1, "A")
    b = student.new_task(1, "A")
    a["done"] = True
    assert b["done"] is False
