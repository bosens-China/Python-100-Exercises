import pytest
from part_4_oop.exercise_073 import Account

@pytest.fixture
def account():
    """提供一个标准的 Account 实例，初始余额为 100。"""
    return Account("John Doe", 100)

def test_initialization():
    """测试账户初始化。"""
    acc = Account("Jane Doe", 50.75)
    assert acc.owner == "Jane Doe"
    assert acc.balance == 50.75

def test_default_balance_initialization():
    """测试默认初始余额为0。"""
    acc = Account("Public")
    assert acc.balance == 0

def test_negative_initial_balance():
    """测试使用负的初始余额时应引发 ValueError。"""
    with pytest.raises(ValueError):
        Account("Bad Guy", -100)

def test_deposit(account):
    """测试有效存款。"""
    account.deposit(50)
    assert account.balance == 150

def test_deposit_zero_or_negative(account):
    """测试无效（零或负数）存款。"""
    initial_balance = account.balance
    account.deposit(0)
    assert account.balance == initial_balance
    account.deposit(-50)
    assert account.balance == initial_balance

def test_withdraw(account):
    """测试有效取款。"""
    account.withdraw(30)
    assert account.balance == 70

def test_withdraw_insufficient_funds(account):
    """测试余额不足时的取款。"""
    initial_balance = account.balance
    account.withdraw(200)
    assert account.balance == initial_balance

def test_withdraw_exact_balance(account):
    """测试取走全部余额。"""
    account.withdraw(100)
    assert account.balance == 0

def test_withdraw_zero_or_negative(account):
    """测试无效（零或负数）取款。"""
    initial_balance = account.balance
    account.withdraw(0)
    assert account.balance == initial_balance
    account.withdraw(-50)
    assert account.balance == initial_balance

def test_str_representation(account):
    """测试 __str__ 方法的输出。"""
    assert str(account) == "Account owner: John Doe, Balance: 100"
    account.deposit(50)
    assert str(account) == "Account owner: John Doe, Balance: 150" 