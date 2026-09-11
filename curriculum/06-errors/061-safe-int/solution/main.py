def parse_int(text):
    try:
        return int(text)
    except ValueError:
        return None
