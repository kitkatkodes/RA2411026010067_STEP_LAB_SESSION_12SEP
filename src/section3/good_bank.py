from abc import ABC, abstractmethod

class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance


class Withdrawable(ABC):
    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(Account, Withdrawable):
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount


class CurrentAccount(Account, Withdrawable):
    def withdraw(self, amount):
        self.balance -= amount


class FixedDepositAccount(Account):
    # This class no longer implements withdraw() because it cannot honestly fulfill that contract
    pass


def test_loop_fixed():
    # Now we only iterate over Withdrawable accounts, completely avoiding the crash
    accounts = [
        SavingsAccount("1", 500),
        CurrentAccount("2", 1000)
    ]
    
    for acc in accounts:
        acc.withdraw(50)
        print(f"Successfully withdrew from account {acc.account_id}")
        
if __name__ == "__main__":
    test_loop_fixed()