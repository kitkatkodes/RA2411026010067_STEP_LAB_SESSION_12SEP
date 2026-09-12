"""
Warm-up Question 3: Dependency Inversion
In the original design, the bank class directly created concrete classes like new InMemoryAccountRepository().
We need to change the constructor so it takes an AccountRepository abstraction instead. 
This way, the bank never directly creates a concrete repository itself and relies entirely on the interface.
"""

class Bank:
    def __init__(self, repository):
        self.repository = repository
        
    def open_account(self, account_number, name, balance):
        # The bank does not know or care if this writes to a file, database, or memory
        self.repository.save(account_number, name, balance)