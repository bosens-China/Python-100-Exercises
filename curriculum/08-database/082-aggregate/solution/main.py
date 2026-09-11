def task_counts(db):
    result = {"pending": 0, "completed": 0}
    for done, count in db.execute("SELECT done, COUNT(*) FROM tasks GROUP BY done"):
        result["completed" if done else "pending"] = count
    return result
