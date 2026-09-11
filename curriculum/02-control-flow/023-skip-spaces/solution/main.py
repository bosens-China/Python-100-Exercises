def compact(text):
    result = ""
    for char in text:
        if char.isspace():
            continue
        result += char
    return result
