def create_task(body, save):
    if not isinstance(body, dict) or not isinstance(body.get("title"), str):
        return {"status": 400, "body": {"error": "invalid_title"}}
    title = body["title"].strip()
    if not 1 <= len(title) <= 80:
        return {"status": 400, "body": {"error": "invalid_title"}}
    identifier = save(title)
    return {"status": 201, "body": {"id": identifier, "title": title, "done": False}}
