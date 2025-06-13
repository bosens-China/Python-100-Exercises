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
    # 在这里写下你的代码
    pass


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