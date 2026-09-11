def unique(items):
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result
