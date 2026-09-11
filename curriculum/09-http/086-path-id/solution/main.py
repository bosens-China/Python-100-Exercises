def task_id(path):
    if not path.startswith("/tasks/"):
        return None
    value = path[len("/tasks/") :]
    if not value or not all("0" <= char <= "9" for char in value):
        return None
    number = int(value)
    return number if number > 0 else None
