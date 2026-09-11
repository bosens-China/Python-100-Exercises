import pytest
from part_2_control_flow.exercise_034 import BankAccount

def test_bank_account_initialization():
    acc = BankAccount(initial_balance=100)
    assert acc.get_balance() == 100

def test_bank_account_deposit():
    acc = BankAccount(100)
    acc.deposit(50)
    assert acc.get_balance() == 150

def test_bank_account_withdraw():
    acc = BankAccount(100)
    acc.withdraw(30)
    assert acc.get_balance() == 70

def test_bank_account_multiple_operations():
    acc = BankAccount(200)
    acc.deposit(50)
    acc.withdraw(100)
    assert acc.get_balance() == 150
