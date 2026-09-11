import sqlite3


def register(db, name):
    try:
        with db:
            db.execute("INSERT INTO users (name) VALUES (?)", (name,))
        return True
    except sqlite3.IntegrityError:
        return False
