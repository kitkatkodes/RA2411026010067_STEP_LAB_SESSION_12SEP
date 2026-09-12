from interest_policy import InterestPolicy

class CurrentInterestPolicy(InterestPolicy):
    def calculate(self, available_balance):
        return available_balance * 0.01