def transform_all(items, transform):
    result = []
    for item in items:
        result.append(transform(item))
    return result
