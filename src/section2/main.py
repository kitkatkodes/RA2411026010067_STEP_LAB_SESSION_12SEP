from savings_interest_policy import SavingsInterestPolicy
from current_interest_policy import CurrentInterestPolicy
from salary_interest_policy import SalaryInterestPolicy
from bank import Bank

class ConsoleNotificationService:
    def send(self, target_user, txt):
        print(f"[Log] {target_user} : {txt}")

def main():
    base_funds = 1000.0
    
    savings = SavingsInterestPolicy()
    current = CurrentInterestPolicy()
    salary = SalaryInterestPolicy()

    print(f"Savings Yield: {savings.calculate(base_funds)}")
    print(f"Current Yield: {current.calculate(base_funds)}")
    print(f"Salary Yield: {salary.calculate(base_funds)}")

    service = ConsoleNotificationService()
    my_bank = Bank(service)
    my_bank.trigger_process("Monthly interest calculation finished.")

if __name__ == "__main__":
    main()