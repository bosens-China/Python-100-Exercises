def delete_task(db, task_id):
    cursor = db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    db.commit()
    return cursor.rowcount > 0
