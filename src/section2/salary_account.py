from account import Account

class SalaryAccount(Account):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            return True
        return False