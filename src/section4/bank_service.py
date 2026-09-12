"""
Warm-up Question 1: The ATM class
If we force a monolithic interface, the ATM hardware class is burdened with implementing methods it simply cannot execute. We would end up writing blank functions for loan applications and statements just to satisfy the compiler, even though the hardware only processes cash.
"""
from abc import ABC, abstractmethod

class BankService(ABC):
    @abstractmethod
    def deposit(self, amt): pass

    @abstractmethod
    def withdraw(self, amt): pass

    @abstractmethod
    def transfer(self, amt, destination_acc): pass

    @abstractmethod
    def print_statement(self): pass

    @abstractmethod
    def apply_for_loan(self): pass

class ATM(BankService):
    def deposit(self, amt): pass
    def withdraw(self, amt): pass

    # Useless implementations forced by poor design
    def transfer(self, amt, destination_acc): pass
    def print_statement(self): pass
    def apply_for_loan(self): pass