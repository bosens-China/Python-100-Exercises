def divide_result(a, b):
    try:
        return {"ok": True, "value": a / b}
    except ZeroDivisionError:
        return {"ok": False, "error": "division_by_zero"}
