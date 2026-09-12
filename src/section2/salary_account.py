from account import Account

class SalaryAccount(Account):
    def __init__(self, acc_num, starting_balance):
        super().__init__(acc_num, starting_balance)

    def withdraw(self, txn_amount):
        if 0 < txn_amount <= self.available_balance:
            self.available_balance -= txn_amount
            return True
        print("Declined: Overdraft not permitted.")
        return False