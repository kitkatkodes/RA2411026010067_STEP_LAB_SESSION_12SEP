from abc import ABC, abstractmethod

class AccountRepository(ABC):
    @abstractmethod
    def save(self, acc_num, client_name, funds):
        pass

class FileAccountRepository(AccountRepository):
    def save(self, acc_num, client_name, funds):
        with open("bank_data.txt", "a") as db_file:
            db_file.write(f"{acc_num} | {client_name} | {funds}\n")