def flatten(rows):
    result = []
    for row in rows:
        for item in row:
            result.append(item)
    return result
