def pending_tasks(db):
    return db.execute(
        "SELECT id, title FROM tasks WHERE done = 0 ORDER BY id"
    ).fetchall()
