def shipping_fee(amount, is_member):
    if is_member or amount >= 9900:
        return 0
    return 800
