def complete_task(db, task_id):
    cursor = db.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    db.commit()
    return cursor.rowcount > 0
