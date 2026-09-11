def line_total(price, quantity):
    return price * quantity


def cart_total(items):
    return sum(line_total(item["price"], item["quantity"]) for item in items)
