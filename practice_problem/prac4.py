# Write a Python class to represent a bank account, which has a balance and allows deposits and withdrawals.
import math


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposite(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdrawals(self, amount):
        self.balance = self.balance - amount
        return self.balance


# Write a Python class to represent a circle, which has a radius and can calculate its area and circumference.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        a = math.pi * self.radius**2
        return a

    def circumference(self):
        c = 2 * math.pi * self.radius
        return c


# Write a Python function to check if a given string is a palindrome.
def str_palindrome(c_str):
    a_str = c_str.lower()
    b = ' '
    for i in a_str:
        b = i + b
    if b == a_str:
        return f"{a_str} is a palindrome"
    return f"{a_str} is not a palindrome"


# Write a Python function to flatten a nested list.
def flatten(a_list):
    b_list = []
    for i in a_list:
        if isinstance(i, list):
            b_list.extend(i)
        else:
            b_list.append(i)
    return b_list


class UserBankAccount:
    def __init__(self, balance):
        self.balance = balance
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount
            self.history.append(f"Withdrew {amount}")

    def print_history(self):
        for transaction in self.history:
            print(transaction)


if __name__ == '__main__':
    # bank = BankAccount(2000)
    # obj = bank.deposite(2000)
    # print(obj)
    # obj1 = bank.withdrawals(1000)
    # print(obj1)

    # cir = Circle(6)
    # print(cir.area())
    # print(cir.circumference())

    # print(str_palindrome("abc"))

    # a_list = [2, 3, 5, 5, [5, 6, 7], 6]
    # print(flatten(a_list))

    bank = UserBankAccount(2000)
    obj = bank.deposit(2000)
    print(obj)
    obj1 = bank.withdraw(1000)
    print(obj)

    print(bank.print_history())