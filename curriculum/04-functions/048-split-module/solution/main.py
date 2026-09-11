from pricing import subtotal


def checkout(price, quantity, fee):
    return subtotal(price, quantity) + fee
