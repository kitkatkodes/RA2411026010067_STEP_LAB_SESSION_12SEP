class Account:
    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance
        
    def withdraw(self, amount):
        pass


class SavingsAccount(Account):
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount


class FixedDepositAccount(Account):
    def withdraw(self, amount):
        # We override this just to throw an exception since FDs cannot be withdrawn early
        raise NotImplementedError("Withdrawal is not supported for Fixed Deposits")


def test_loop():
    accounts = [
        SavingsAccount("1", 500),
        FixedDepositAccount("2", 1000)
    ]
    
    # This loop will crash when it hits the FixedDepositAccount
    for acc in accounts:
        acc.withdraw(50)
        print(f"Successfully withdrew from account {acc.account_id}")

if __name__ == "__main__":
    test_loop()