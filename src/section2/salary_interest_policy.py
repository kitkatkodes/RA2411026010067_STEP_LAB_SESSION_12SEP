from interest_policy import InterestPolicy

class SalaryInterestPolicy(InterestPolicy):
    def calculate(self, available_balance):
        return available_balance * 0.05