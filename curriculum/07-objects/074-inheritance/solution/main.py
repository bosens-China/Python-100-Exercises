class Customer:
    def __init__(self, name):
        self.name = name

    def payable(self, amount):
        return amount


class MemberCustomer(Customer):
    def payable(self, amount):
        return amount * 9 // 10
