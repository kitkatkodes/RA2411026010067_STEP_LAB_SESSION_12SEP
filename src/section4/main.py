from repository import FileAccountRepository
from bank import Bank

def main():
    # We swap dependencies entirely from the outside
    repo = FileAccountRepository()
    bank = Bank(repo)
    
    bank.open_account("999", "CustomerName", 500.0)
    print("Account saved successfully through file repository.")

if __name__ == "__main__":
    main()