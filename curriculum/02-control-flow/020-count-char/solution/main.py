def count_char(text, target):
    count = 0
    for char in text:
        if char == target:
            count += 1
    return count
