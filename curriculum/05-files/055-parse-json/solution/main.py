import json


def enabled_names(text):
    rows = json.loads(text)
    return [row["name"] for row in rows if row["enabled"]]
