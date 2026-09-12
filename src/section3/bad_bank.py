class Account:
    def __init__(self, acc_id, funds):
        self.acc_id = acc_id
        self.funds = funds
        
    def withdraw(self, amt):
        pass

class SavingsAccount(Account):
    def withdraw(self, amt):
        if self.funds >= amt:
            self.funds -= amt

class FixedDepositAccount(Account):
    def withdraw(self, amt):
        raise NotImplementedError("Early withdrawals are strictly prohibited for FDs.")

def run_test():
    acc_list = [
        SavingsAccount("A1", 500),
        FixedDepositAccount("A2", 1000)
    ]
    
    for account in acc_list:
        account.withdraw(50)
        print(f"Cash dispensed for account {account.acc_id}")

if __name__ == "__main__":
    run_test()