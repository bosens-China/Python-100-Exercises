def route(method, path):
    if path != "/health":
        return {"status": 404, "body": {"error": "not_found"}}
    if method != "GET":
        return {"status": 405, "body": {"error": "method_not_allowed"}}
    return {"status": 200, "body": {"ok": True}}
