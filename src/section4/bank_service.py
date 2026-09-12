"""
Warm-up Question 1: The ATM class
If we have a fat interface, the ATM class is forced to implement methods it doesn't really need. 
We would have to write empty or dummy implementations for transfer, print_statement, and apply_for_loan 
just to make the code run, even though an ATM only handles deposits and withdrawals.
"""
from abc import ABC, abstractmethod

class BankService(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def transfer(self, amount, to_account):
        pass

    @abstractmethod
    def print_statement(self):
        pass

    @abstractmethod
    def apply_for_loan(self):
        pass


class ATM(BankService):
    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    # Forced to implement these but the ATM doesn't use them
    def transfer(self, amount, to_account):
        pass

    def print_statement(self):
        pass

    def apply_for_loan(self):
        pass