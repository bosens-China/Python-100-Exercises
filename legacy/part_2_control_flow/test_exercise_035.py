import pytest
from part_2_control_flow.exercise_035 import BankAccount

def test_withdraw_insufficient_funds():
    acc = BankAccount(100)
    with pytest.raises(ValueError, match="Insufficient funds"):
        acc.withdraw(150)

def test_withdraw_sufficient_funds():
    acc = BankAccount(100)
    acc.withdraw(50)
    assert acc.get_balance() == 50

def test_balance_unchanged_after_failed_withdraw():
    acc = BankAccount(100)
    with pytest.raises(ValueError):
        acc.withdraw(150)
    assert acc.get_balance() == 100
