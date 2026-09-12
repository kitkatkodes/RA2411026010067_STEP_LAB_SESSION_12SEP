from repository import FileAccountRepository
from bank import Bank

def main():
    text_db = FileAccountRepository()
    greenleaf_bank = Bank(text_db)
    
    greenleaf_bank.open_account("888", "Shreyasi", 750.0)
    print("New customer registered via File Repository.")

if __name__ == "__main__":
    main()