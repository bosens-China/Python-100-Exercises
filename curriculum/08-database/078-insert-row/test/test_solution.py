# student 是本次执行的 main.py 模块；raises 用于验证异常类型。

import sqlite3
from contextlib import closing


def make_db():
    db = sqlite3.connect(":memory:")
    db.execute(
        "CREATE TABLE tasks (id INTEGER PRIMARY KEY, title TEXT NOT NULL, done INTEGER NOT NULL DEFAULT 0)"
    )
    db.executemany(
        "INSERT INTO tasks VALUES (?, ?, ?)", [(1, "A", 0), (2, "B", 1), (3, "C", 0)]
    )
    db.commit()
    return db


def test_case_01():
    with closing(make_db()) as db:
        identifier = student.add_task(db, "阅读")
        assert type(identifier) is int
        assert db.execute(
            "SELECT title, done FROM tasks WHERE id = ?", (identifier,)
        ).fetchone() == ("阅读", 0)
        assert db.in_transaction is False


def test_case_02():
    with closing(make_db()) as db:
        title = "x'); DROP TABLE tasks; --"
        identifier = student.add_task(db, title)
        assert db.execute(
            "SELECT title FROM tasks WHERE id = ?", (identifier,)
        ).fetchone() == (title,)
        assert db.execute("SELECT COUNT(*) FROM tasks").fetchone()[0] == 4


def test_case_03():
    with closing(make_db()) as db:
        first = student.add_task(db, "A")
        second = student.add_task(db, "A")
        assert first != second
