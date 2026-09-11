def handle(store, method, path, body=None):
    if path == "/tasks":
        if method == "GET":
            return {"status": 200, "body": store.list()}
        if method == "POST":
            if not isinstance(body, dict):
                return {"status": 400, "body": {"error": "invalid_title"}}
            try:
                task = store.add(body.get("title"))
            except ValueError:
                return {"status": 400, "body": {"error": "invalid_title"}}
            return {"status": 201, "body": task}
        return {"status": 405, "body": {"error": "method_not_allowed"}}
    prefix = "/tasks/"
    value = path[len(prefix) :] if path.startswith(prefix) else ""
    if not value or not all("0" <= char <= "9" for char in value) or int(value) <= 0:
        return {"status": 404, "body": {"error": "not_found"}}
    identifier = int(value)
    if method not in ("GET", "PATCH", "DELETE"):
        return {"status": 405, "body": {"error": "method_not_allowed"}}
    matches = [task for task in store.list() if task["id"] == identifier]
    if not matches:
        return {"status": 404, "body": {"error": "not_found"}}
    if method == "GET":
        return {"status": 200, "body": matches[0]}
    if method == "PATCH":
        if not isinstance(body, dict) or body.get("done") is not True:
            return {"status": 400, "body": {"error": "invalid_done"}}
        return {"status": 200, "body": store.complete(identifier)}
    store.delete(identifier)
    return {"status": 204, "body": None}
