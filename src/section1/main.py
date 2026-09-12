from bank_account import BankAccount
from account_repository import AccountRepository
from notification_service import NotificationService
from statement_generator import StatementGenerator

def main():
    account = BankAccount(101, "Ravi", 17, 200, "Savings")
    account.set_pin(1234)
    
    account.deposit(1000)
    account.withdraw(500, 1234)

    repo = AccountRepository()
    repo.save(account)

    notifier = NotificationService()
    notifier.send(account.get_name(), "Transaction complete")

    generator = StatementGenerator()
    print(generator.generate(account))

if __name__ == "__main__":
    main()