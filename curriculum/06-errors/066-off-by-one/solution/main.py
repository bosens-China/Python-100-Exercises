def paginate(items, page, page_size):
    start = (page - 1) * page_size
    return items[start : start + page_size]
