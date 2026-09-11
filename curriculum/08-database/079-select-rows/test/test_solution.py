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
        assert student.pending_tasks(db) == [(1, "A"), (3, "C")]
        assert db.execute("SELECT COUNT(*) FROM tasks").fetchone()[0] == 3


def test_case_02():
    with closing(make_db()) as db:
        db.execute("UPDATE tasks SET done = 1")
        assert student.pending_tasks(db) == []


def test_case_03():
    with closing(make_db()) as db:
        db.execute("INSERT INTO tasks VALUES (0, ?, 0)", ("Z",))
        assert student.pending_tasks(db) == [(0, "Z"), (1, "A"), (3, "C")]
