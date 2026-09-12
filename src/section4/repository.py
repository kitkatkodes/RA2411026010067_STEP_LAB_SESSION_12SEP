from abc import ABC, abstractmethod

class AccountRepository(ABC):
    @abstractmethod
    def save(self, account_number, name, balance):
        pass

class FileAccountRepository(AccountRepository):
    def save(self, account_number, name, balance):
        with open("accounts.txt", "a") as file:
            file.write(f"{account_number},{name},{balance}\n")