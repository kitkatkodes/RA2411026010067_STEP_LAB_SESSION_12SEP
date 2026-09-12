from bank_account import BankAccount
from account_repository import AccountRepository
from notification_service import NotificationService
from statement_generator import StatementGenerator

def main():
    my_account = BankAccount(101, "Ravi", 17, 200, "Savings")
    my_account.set_pin(1234)
    
    my_account.deposit(1000)
    my_account.withdraw(500, 1234)

    storage = AccountRepository()
    storage.save(my_account)

    alert_system = NotificationService()
    alert_system.send(my_account.get_name(), "The recent transaction was successful.")

    doc_gen = StatementGenerator()
    print(doc_gen.generate(my_account))

if __name__ == "__main__":
    main()