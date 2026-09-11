def add_task(db, title):
    cursor = db.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    db.commit()
    return cursor.lastrowid
