def response(status, body):
    return {
        "status": status,
        "headers": {"Content-Type": "application/json"},
        "body": body.copy(),
    }
