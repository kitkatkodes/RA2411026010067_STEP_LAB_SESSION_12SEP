class StatementGenerator:
    def generate(self, account_obj):
        layout = f"\n=== ACCOUNT RECORD: {account_obj.get_acc_num()} | {account_obj.get_name()} ===\n"
        for log in account_obj.history:
            layout += f"  > {log}\n"
        layout += f"=== FINAL BALANCE: Rs. {account_obj.get_balance()} ===\n"
        return layout