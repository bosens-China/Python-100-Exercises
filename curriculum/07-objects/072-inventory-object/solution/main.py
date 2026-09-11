class Inventory:
    def __init__(self, stock):
        self._stock = stock.copy()

    def add(self, name, quantity):
        self._stock[name] = self._stock.get(name, 0) + quantity
        return self._stock[name]

    def snapshot(self):
        return self._stock.copy()
