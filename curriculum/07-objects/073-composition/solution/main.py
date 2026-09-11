class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self._items = []

    def add(self, product, quantity=1):
        self._items.append((product, quantity))

    def total(self):
        return sum(product.price * quantity for product, quantity in self._items)
