def filter_tasks(tasks, completed=None):
    if completed not in (None, "true", "false"):
        raise ValueError("完成状态无效")
    expected = None if completed is None else completed == "true"
    return [
        task.copy() for task in tasks if expected is None or task["done"] == expected
    ]
