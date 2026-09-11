def validate_body(body):
    if not isinstance(body, dict) or not isinstance(body.get("title"), str):
        raise ValueError("需要字符串标题")
    title = body["title"].strip()
    if not 1 <= len(title) <= 80:
        raise ValueError("标题长度无效")
    return {"title": title}
