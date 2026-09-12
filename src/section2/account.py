from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, acc_num, starting_balance):
        self.acc_num = acc_num
        self.available_balance = starting_balance

    def deposit(self, txn_amount):
        if txn_amount > 0:
            self.available_balance += txn_amount
            return True
        return False

    @abstractmethod
    def withdraw(self, txn_amount):
        pass