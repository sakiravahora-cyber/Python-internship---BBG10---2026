#1
class Wallet:
    def _init_(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__balance = initial_balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        print(f"Deposited {amount}. Current balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient balance.")
        self.__balance -= amount
        print(f"Withdrew {amount}. Current balance: {self.__balance}")


w = Wallet(500)
w.deposit(250)
w.withdraw(150)
print("Final Balance:", w.balance)

#2
class Fraction:
    def _init_(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator

    def _add_(self, other):
        new_num = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        new_den = self.denominator * other.denominator
        return Fraction(new_num, new_den)

    def _str_(self):
        return f"{self.numerator}/{self.denominator}"


f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
total = f1 + f2
print(f"{f1} + {f2} = {total}")

#Q3
class Inventory:
    def _init_(self, items=None):
        self._items = list(items) if items is not None else []

    def add_item(self, item):
        self._items.append(item)

    def _len_(self):
        return len(self._items)

    def _getitem_(self, index):
        return self._items[index]


inv = Inventory(["Notebook", "Pen", "Eraser"])
inv.add_item("Marker")

print("Total items:", len(inv))
print("First item:", inv[0])
print("Third item:", inv[2])

#Q4
class Point:
    def _init_(self, x, y):
        self.x = x
        self.y = y

    def _eq_(self, other):
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y

    def _str_(self):
        return f"({self.x}, {self.y})"


p1 = Point(3, 5)
p2 = Point(3, 5)
p3 = Point(4, 5)

print("Point 1:", p1)
print("Point 2:", p2)
print("Point 3:", p3)
print("p1 == p2:", p1 == p2)
print("p1 == p3:", p1 == p3)

#Q5
class Stack:
    def _init_(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if not self.__items:
            raise IndexError("Cannot pop from an empty stack.")
        return self.__items.pop()

    def _str_(self):
        return f"Stack(bottom -> top): {self.__items}"


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack)

popped = stack.pop()
print("Popped item:", popped)
print(stack)

#Q6
class Money:
    def _init_(self, amount, currency):
        self.amount = amount
        self.currency = currency.upper()

    def _validate_currency(self, other):
        if not isinstance(other, Money):
            raise TypeError("Can only compare Money with another Money object.")
        if self.currency != other.currency:
            raise ValueError(f"Cannot compare different currencies: {self.currency} vs {other.currency}")

    def _lt_(self, other):
        self._validate_currency(other)
        return self.amount < other.amount

    def _gt_(self, other):
        self._validate_currency(other)
        return self.amount > other.amount

    def _str_(self):
        return f"{self.amount} {self.currency}"


m1 = Money(100, "USD")
m2 = Money(250, "USD")
print("100 USD < 250 USD:", m1 < m2)
print("250 USD > 100 USD:", m2 > m1)

# Different currency test
m3 = Money(100, "INR")
try:
    print(m1 < m3)
except ValueError as e:
    print("Error:", e)
    
#Q7
import time


class Timer:
    def _enter_(self):
        self.start_time = time.perf_counter()
        return self

    def _exit_(self, exc_type, exc_val, exc_tb):
        self.end_time = time.perf_counter()
        elapsed = self.end_time - self.start_time
        print(f"Elapsed time: {elapsed:.6f} seconds")
        return False


with Timer():
    total = 0
    for i in range(1_000_000):
        total += i