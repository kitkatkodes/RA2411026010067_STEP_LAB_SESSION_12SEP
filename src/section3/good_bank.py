from abc import ABC, abstractmethod

class Account:
    def __init__(self, acc_id, funds):
        self.acc_id = acc_id
        self.funds = funds

class Withdrawable(ABC):
    @abstractmethod
    def withdraw(self, amt):
        pass

class SavingsAccount(Account, Withdrawable):
    def withdraw(self, amt):
        if self.funds >= amt:
            self.funds -= amt

class CurrentAccount(Account, Withdrawable):
    def withdraw(self, amt):
        self.funds -= amt

class FixedDepositAccount(Account):
    # Removed withdraw method completely to honor LSP
    pass

def run_test_fixed():
    acc_list = [
        SavingsAccount("A1", 500),
        CurrentAccount("A2", 1000)
    ]
    
    for account in acc_list:
        account.withdraw(50)
        print(f"Cash dispensed for account {account.acc_id}")
        
if __name__ == "__main__":
    run_test_fixed()