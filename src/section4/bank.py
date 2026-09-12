"""
Warm-up Question 3: Dependency Inversion
Previously, the primary class hardcoded the creation of a specific storage component, binding it permanently to that implementation. By passing an abstract repository through the constructor, the core logic relies on the interface contract rather than the database details.
"""
class Bank:
    def __init__(self, data_store):
        self.data_store = data_store
        
    def open_account(self, acc_num, client_name, funds):
        self.data_store.save(acc_num, client_name, funds)