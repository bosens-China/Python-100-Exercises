# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.hello() == "Hello, Python!", (
        "预期返回 Hello, Python!，不是打印后返回 None"
    )


def test_case_02():
    assert type(student.hello()) is str
