def normalize_title(title):
    if not isinstance(title, str):
        raise ValueError("标题必须是字符串")
    value = title.strip()
    if not 1 <= len(value) <= 80:
        raise ValueError("标题长度必须为 1 到 80")
    return value


def new_task(identifier, title):
    if type(identifier) is not int or identifier <= 0:
        raise ValueError("ID 必须为正整数")
    return {"id": identifier, "title": normalize_title(title), "done": False}
