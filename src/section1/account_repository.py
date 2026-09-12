class AccountRepository:
    def save(self, account_obj):
        print(f"[System DB] Persisting details for Account {account_obj.get_acc_num()}...")