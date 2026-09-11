def parse_page(query):
    text = query.get("page", "1")
    if (
        not isinstance(text, str)
        or not text
        or not all("0" <= char <= "9" for char in text)
    ):
        raise ValueError("页码格式无效")
    page = int(text)
    if not 1 <= page <= 1000:
        raise ValueError("页码越界")
    return page
