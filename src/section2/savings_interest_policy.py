from interest_policy import InterestPolicy

class SavingsInterestPolicy(InterestPolicy):
    def calculate(self, available_balance):
        return available_balance * 0.04