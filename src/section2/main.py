from savings_interest_policy import SavingsInterestPolicy
from current_interest_policy import CurrentInterestPolicy
from salary_interest_policy import SalaryInterestPolicy
from bank import Bank

class DummyNotificationService:
    def send(self, recipient, message):
        print(f"To: {recipient} | {message}")

def main():
    balance = 1000.0
    
    savings_policy = SavingsInterestPolicy()
    current_policy = CurrentInterestPolicy()
    salary_policy = SalaryInterestPolicy()

    print(f"Savings Interest: {savings_policy.calculate(balance)}")
    print(f"Current Interest: {current_policy.calculate(balance)}")
    print(f"Salary Interest: {salary_policy.calculate(balance)}")

    notifier = DummyNotificationService()
    bank = Bank(notifier)
    bank.perform_operation("Interest policies applied successfully")

if __name__ == "__main__":
    main()