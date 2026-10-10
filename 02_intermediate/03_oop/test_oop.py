import pytest

from oop import BankAccount, SavingsAccount, Vector


def test_account_basics():
    acct = BankAccount("Ada", 100)
    acct.deposit(50)
    acct.withdraw(30)
    assert acct.balance == 120
    assert repr(acct) == "BankAccount(owner='Ada', balance=120)"


def test_account_default_balance():
    assert BankAccount("Bob").balance == 0


def test_balance_is_read_only():
    acct = BankAccount("Ada", 10)
    with pytest.raises(AttributeError):
        acct.balance = 999


@pytest.mark.parametrize("amount", [0, -5])
def test_invalid_amounts(amount):
    acct = BankAccount("Ada", 10)
    with pytest.raises(ValueError):
        acct.deposit(amount)
    with pytest.raises(ValueError):
        acct.withdraw(amount)


def test_overdraw():
    with pytest.raises(ValueError):
        BankAccount("Ada", 10).withdraw(11)


def test_savings_interest():
    acct = SavingsAccount("Ada", 200)
    assert acct.add_interest(0.05) == 10
    assert acct.balance == 210
    assert isinstance(acct, BankAccount)


def test_vector():
    a, b = Vector(1, 2), Vector(2, 2)
    assert a + b == Vector(3, 4)
    assert abs(Vector(3, 4)) == 5
    assert repr(Vector(3, 4)) == "Vector(3, 4)"
    assert Vector(1, 1) != Vector(1, 2)
