class BankAccount:
    """A simple bank account.

    - `BankAccount(owner, balance=0)`
    - `balance` is a read-only property.
    - `deposit(amount)`: amount must be > 0, else raise ValueError.
    - `withdraw(amount)`: raise ValueError if amount <= 0 or exceeds the balance.
    - `repr()` looks like: BankAccount(owner='Ada', balance=100)
    """

    def __init__(self, owner, balance=0):
        raise NotImplementedError


class SavingsAccount(BankAccount):
    """A BankAccount that can earn interest.

    `add_interest(rate)` deposits balance * rate (e.g. rate=0.05 adds 5%)
    and returns the interest amount.
    """

    def add_interest(self, rate):
        raise NotImplementedError


class Vector:
    """A 2D vector supporting: `+`, `==`, `abs()` (length), and a nice repr.

    repr looks like: Vector(3, 4)
    """

    def __init__(self, x, y):
        raise NotImplementedError
