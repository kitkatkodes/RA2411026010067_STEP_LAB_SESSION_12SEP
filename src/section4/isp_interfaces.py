from abc import ABC, abstractmethod

class Depositable(ABC):
    @abstractmethod
    def deposit(self, amt): pass

class Withdrawable(ABC):
    @abstractmethod
    def withdraw(self, amt): pass

class Transferable(ABC):
    @abstractmethod
    def transfer(self, amt, destination_acc): pass

class StatementProvider(ABC):
    @abstractmethod
    def print_statement(self): pass

class LoanEligible(ABC):
    @abstractmethod
    def apply_for_loan(self): pass

class ATM(Depositable, Withdrawable):
    def deposit(self, amt): pass
    def withdraw(self, amt): pass

class SavingsAccount(Depositable, Withdrawable, Transferable, StatementProvider):
    def deposit(self, amt): pass
    def withdraw(self, amt): pass
    def transfer(self, amt, destination_acc): pass
    def print_statement(self): return "Doc Generated"