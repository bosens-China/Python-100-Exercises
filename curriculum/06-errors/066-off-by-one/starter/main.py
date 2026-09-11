def paginate(items, page, page_size):
    # 这段代码能执行，但第一页起点错误。
    start = page * page_size
    return items[start : start + page_size]
