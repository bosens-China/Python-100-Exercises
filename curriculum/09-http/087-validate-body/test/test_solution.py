# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    body = {"title": " 学习 ", "done": True}
    assert student.validate_body(body) == {"title": "学习"}
    assert body["title"] == " 学习 "


def test_case_02():
    for body in [None, [], {}, {"title": 1}, {"title": " "}, {"title": "a" * 81}]:
        with raises(ValueError):
            student.validate_body(body)


def test_case_03():
    assert student.validate_body({"title": "a" * 80}) == {"title": "a" * 80}
