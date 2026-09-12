class AccountRepository:
    def save(self, account):
        print(f"[DB] Saving account {account.get_account_number()} to MySQL...")