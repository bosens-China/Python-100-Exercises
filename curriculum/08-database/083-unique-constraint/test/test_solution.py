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
        db.execute(
            "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE)"
        )
        assert student.register(db, "Ada") is True
        assert student.register(db, "Ada") is False
        assert student.register(db, "Bob") is True
        assert db.execute("SELECT name FROM users ORDER BY id").fetchall() == [
            ("Ada",),
            ("Bob",),
        ]
        assert db.in_transaction is False


def test_case_02():
    with closing(sqlite3.connect(":memory:")) as db:
        db.execute(
            "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE)"
        )
        assert student.register(db, "Ada") is True
        assert student.register(db, "ada") is True


def test_case_03():
    with closing(sqlite3.connect(":memory:")) as db:
        db.execute(
            "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE)"
        )
        name = "O'Brien"
        assert student.register(db, name) is True
        assert db.execute("SELECT name FROM users").fetchone() == (name,)
