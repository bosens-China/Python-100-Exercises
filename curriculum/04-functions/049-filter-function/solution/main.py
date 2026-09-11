def select(items, predicate):
    return [item for item in items if predicate(item)]
