def format_name(name, uppercase=False):
    result = name.strip()
    if uppercase:
        return result.upper()
    return result
