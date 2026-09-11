def merge_stock(left, right):
    result = left.copy()
    for name, count in right.items():
        result[name] = result.get(name, 0) + count
    return result
