"""
Warm-up Question 1: Adding a 4th account type
To support a new type, we would have to modify this file directly by locating the calculation block, injecting an additional 'elif' statement for the new label, and hardcoding the math directly into that conditional branch.
"""
class InterestCalculator:
    def calculate(self, acc_type, current_balance):
        if acc_type == "Savings":
            return current_balance * 0.04
        elif acc_type == "Current":
            return current_balance * 0.01
        elif acc_type == "Salary":
            return current_balance * 0.05
        return 0.0