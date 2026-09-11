def add_item(item, items=None):
    result = [] if items is None else items.copy()
    result.append(item)
    return result
