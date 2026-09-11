def first_digit(text):
    for char in text:
        if "0" <= char <= "9":
            return char
    return ""
