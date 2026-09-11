class Account:
    def __init__(self, balance=0):
        if balance < 0:
            raise ValueError("余额不能为负")
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("金额必须为正")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            raise ValueError("取款金额无效")
        self.balance -= amount
        return self.balance
