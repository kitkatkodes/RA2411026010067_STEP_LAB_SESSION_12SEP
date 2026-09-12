"""
Warm-up Question 1: Adding a 4th account type
To add a 4th account type, we would have to open this file and locate the calculate method. We would then need to add another elif condition specifically checking if the account_type equals the new type. Finally, we would have to add the mathematical formula for the new account type directly inside that new block.
"""

class InterestCalculator:
    def calculate(self, account_type, balance):
        if account_type == "Savings":
            return balance * 0.04
        elif account_type == "Current":
            return balance * 0.01
        elif account_type == "Salary":
            return balance * 0.05
        return 0.0