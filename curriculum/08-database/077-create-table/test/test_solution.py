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
    with closing(sqlite3.connect(":memory:")) as db:
        assert student.create_tasks(db) is None
        db.execute("INSERT INTO tasks (title) VALUES (?)", ("A",))
        assert db.execute("SELECT id, title, done FROM tasks").fetchall() == [
            (1, "A", 0)
        ]


def test_case_02():
    with closing(sqlite3.connect(":memory:")) as db:
        student.create_tasks(db)
        db.execute("INSERT INTO tasks (title) VALUES (?)", ("A",))
        student.create_tasks(db)
        assert db.execute("SELECT COUNT(*) FROM tasks").fetchone()[0] == 1


def test_case_03():
    with closing(sqlite3.connect(":memory:")) as db:
        student.create_tasks(db)
        with raises(sqlite3.IntegrityError):
            db.execute("INSERT INTO tasks (title) VALUES (NULL)")
        with raises(sqlite3.IntegrityError):
            db.execute("INSERT INTO tasks (title, done) VALUES (?, NULL)", ("A",))
