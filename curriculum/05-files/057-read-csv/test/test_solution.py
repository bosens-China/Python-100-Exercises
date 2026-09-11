# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    from pathlib import Path

    Path("people.csv").write_text("name,age\nAda,20\n", encoding="utf-8")
    assert student.read_people("people.csv") == [{"name": "Ada", "age": 20}]


def test_case_02():
    from pathlib import Path

    Path("people.csv").write_text('name,age\n"Lin, Yu",0\n', encoding="utf-8")
    assert student.read_people("people.csv") == [{"name": "Lin, Yu", "age": 0}]


def test_case_03():
    from pathlib import Path

    Path("people.csv").write_text("name,age\n", encoding="utf-8")
    assert student.read_people("people.csv") == []
