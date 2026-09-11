def ticket_price(age):
    if age < 6:
        return 0
    if age < 18:
        return 1000
    if age < 65:
        return 2000
    return 1000
