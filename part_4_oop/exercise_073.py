"""
### 73. 创建一个 `Bank` `Account` 类

- **描述:** 创建一个 `Account` 类，包含 `owner` 和 `balance` 属性。添加 `deposit()` 和 `withdraw()` 方法。确保取款时余额不能为负。
- **提示:** `withdraw` 方法需要检查取款金额是否大于余额。
- **期待:**
  - `acc.deposit(50)` 后余额增加。
  - `acc.withdraw(30)` 后余额减少。
  - `acc.withdraw(1000)` (当余额不足时) 会打印错误信息且余额不变。
"""

class Account:
    """一个代表银行账户的类。"""
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = balance

    def deposit(self, amount: float):
        """向账户存款。"""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        # 在这里写下你的代码
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount: float):
        """从账户取款。"""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        # 在这里写下你的代码
        if amount > self.balance:
            print("Withdrawal failed: Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
            
    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance}"


if __name__ == '__main__':
    acc = Account("John Doe", 100)
    print(acc)
    
    print("\n--- 操作 ---")
    acc.deposit(50)
    acc.withdraw(30)
    acc.withdraw(200) # 这次会失败
    acc.deposit(-20)   # 这次会失败
    acc.withdraw(-10)  # 这次会失败
    
    print(f"\nFinal state: {acc}") 