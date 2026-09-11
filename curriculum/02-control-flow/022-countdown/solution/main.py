def countdown(n):
    result = ""
    while n > 0:
        result += str(n) + " "
        n -= 1
    return result + "开始"
