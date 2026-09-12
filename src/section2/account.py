from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self.balance