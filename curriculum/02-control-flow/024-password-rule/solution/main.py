def valid_password(text):
    has_letter = False
    has_digit = False
    for char in text:
        if "a" <= char <= "z" or "A" <= char <= "Z":
            has_letter = True
        if "0" <= char <= "9":
            has_digit = True
    return len(text) >= 8 and has_letter and has_digit
