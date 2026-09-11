"""
题目 035: 在取款时检查余额

要求:
升级 `BankAccount` 类。修改 `withdraw` 方法，
使其在尝试取出超过当前余额的金额时，引发一个 `ValueError` 异常，
并附带错误消息 `"Insufficient funds"`。

提示:
使用 `if` 语句检查取款金额是否大于余额。
如果是，使用 `raise ValueError("...")` 来引发异常。
"""

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    # 在这里修改你的代码
    def withdraw(self, amount):
        self.balance -= amount
