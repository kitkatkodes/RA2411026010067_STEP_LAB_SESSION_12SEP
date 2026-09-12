"""
Warm-up Question 1: Reasons to change
1. Modifying the persistence mechanism or database layer.
2. Switching the notification method, like moving from email to SMS.
3. Updating the display format of the transaction statements.
4. Adjusting internal business logic such as minimum balance thresholds.

Warm-up Question 2: Job description
This class should solely manage the state of a customer balance by validating and processing deposits and withdrawals.
"""

class BankAccount:
    def __init__(self, acc_num, client_name, client_age, initial_funds, acc_type):
        if client_age < 18:
            client_age = 18
            
        min_required = 500.0 if acc_type == "Savings" else 1000.0
        if initial_funds < min_required:
            initial_funds = min_required
            
        self.acc_num = acc_num
        self.client_name = client_name
        self.client_age = client_age
        self.current_balance = initial_funds
        self.acc_type = acc_type
        self.is_active = True
        self.security_pin = None
        self.history = []

    def deposit(self, txn_amount):
        if not self.is_active or txn_amount <= 0:
            print("Error: Invalid deposit attempt.")
            return False
            
        self.current_balance += txn_amount
        self.history.append(f"+ {txn_amount} | Available: {self.current_balance}")
        return True

    def withdraw(self, txn_amount, input_pin):
        if not self.is_active:
            print("Error: Account disabled.")
            return False
            
        if self.security_pin is not None and (input_pin is None or input_pin != self.security_pin):
            print("Error: Authentication failed.")
            return False
            
        if txn_amount <= 0:
            return False
            
        min_required = 500.0 if self.acc_type == "Savings" else 1000.0
        if self.current_balance - txn_amount < min_required:
            print("Error: Insufficient funds to maintain minimum balance.")
            return False
            
        self.current_balance -= txn_amount
        self.history.append(f"- {txn_amount} | Available: {self.current_balance}")
        return True

    def get_acc_num(self):
        return self.acc_num

    def get_name(self):
        return self.client_name

    def get_balance(self):
        return self.current_balance

    def set_pin(self, new_pin):
        if 1000 <= new_pin <= 9999:
            self.security_pin = new_pin
            return True
        return False