# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    import csv

    assert student.write_people("out.csv", [{"name": "Lin, Yu", "age": 20}]) is None
    with open("out.csv", encoding="utf-8", newline="") as file:
        assert list(csv.reader(file)) == [["name", "age"], ["Lin, Yu", "20"]]


def test_case_02():
    import csv

    student.write_people("out.csv", [])
    with open("out.csv", encoding="utf-8", newline="") as file:
        assert list(csv.reader(file)) == [["name", "age"]]


def test_case_03():
    import csv

    student.write_people("out.csv", [{"name": "旧", "age": 1}])
    student.write_people("out.csv", [{"name": "新", "age": 0}])
    with open("out.csv", encoding="utf-8", newline="") as file:
        assert list(csv.DictReader(file)) == [{"name": "新", "age": "0"}]
