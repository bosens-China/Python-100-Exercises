# student 是本次执行的 main.py 模块；raises 用于验证异常类型。

import sqlite3
from contextlib import closing


def make_db():
    db = sqlite3.connect(":memory:")
    db.execute(
        "CREATE TABLE accounts (id INTEGER PRIMARY KEY, balance INTEGER NOT NULL CHECK(balance >= 0))"
    )
    db.executemany("INSERT INTO accounts VALUES (?, ?)", [(1, 100), (2, 20)])
    db.commit()
    return db


def test_case_01():
    with closing(make_db()) as db:
        assert student.transfer(db, 1, 2, 30) is None
        assert db.execute("SELECT balance FROM accounts ORDER BY id").fetchall() == [
            (70,),
            (50,),
        ]
        assert db.in_transaction is False


def test_case_02():
    with closing(make_db()) as db:
        for amount in [0, -1, 101]:
            with raises(ValueError):
                student.transfer(db, 1, 2, amount)
        with raises(ValueError):
            student.transfer(db, 1, 1, 1)
        assert db.execute("SELECT balance FROM accounts ORDER BY id").fetchall() == [
            (100,),
            (20,),
        ]


def test_case_03():
    with closing(make_db()) as db:
        with raises(KeyError):
            student.transfer(db, 1, 999, 30)
        with raises(KeyError):
            student.transfer(db, 999, 2, 30)
        assert db.execute("SELECT balance FROM accounts ORDER BY id").fetchall() == [
            (100,),
            (20,),
        ]


def test_case_04():
    with closing(make_db()) as db:
        db.execute(
            "CREATE TRIGGER reject_credit BEFORE UPDATE ON accounts WHEN NEW.id = 2 BEGIN SELECT RAISE(ABORT, 'blocked'); END"
        )
        with raises(sqlite3.IntegrityError):
            student.transfer(db, 1, 2, 30)
        assert db.execute("SELECT balance FROM accounts ORDER BY id").fetchall() == [
            (100,),
            (20,),
        ]
        assert db.in_transaction is False
