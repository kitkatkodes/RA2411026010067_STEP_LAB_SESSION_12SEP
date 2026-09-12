from abc import ABC, abstractmethod

class Depositable(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

class Withdrawable(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass

class Transferable(ABC):
    @abstractmethod
    def transfer(self, amount, target_account):
        pass

class StatementProvider(ABC):
    @abstractmethod
    def print_statement(self):
        pass

class LoanEligible(ABC):
    @abstractmethod
    def apply_for_loan(self):
        pass


class ATM(Depositable, Withdrawable):
    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass


class SavingsAccount(Depositable, Withdrawable, Transferable, StatementProvider):
    def deposit(self, amount):
        pass

    def withdraw(self, amount):
        pass

    def transfer(self, amount, target):
        pass

    def print_statement(self):
        return "Statement printed"