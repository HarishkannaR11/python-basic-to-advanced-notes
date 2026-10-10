import math


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount

    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self._balance})"


class SavingsAccount(BankAccount):
    def add_interest(self, rate):
        interest = self.balance * rate
        self.deposit(interest)
        return interest


class Vector:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return isinstance(other, Vector) and (self.x, self.y) == (other.x, other.y)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
