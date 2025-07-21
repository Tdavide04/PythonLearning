class Account():
    def __init__(self, account_id: str, balance: float) -> None:
        self.account_id: str = account_id
        self.balance: float = balance

    def deposit(self, amount: float):
        self.balance += amount

    def get_balance(self):
        return self.balance
    
class Bank():
    def __init__(self) -> None:

        self.accounts: dict = {}

    def create_account(self, account_id):
        self.account = Account(account_id, 0)
        if account_id not in self.accounts:
            self.accounts[account_id] = self.account
            return self.account
        else:
            raise ValueError("Account with this ID already exists")
        
    def deposit(self,account_id: str, amount: float):
        
        if account_id in self.accounts:
            self.account.balance += amount
        else:
            raise ValueError(f"Account not found")
    
    def get_balance(self, account_id):

        if account_id in self.accounts:
            return self.account.balance
        else:
            raise ValueError(f"Account not found")

bank = Bank()
account1 = bank.create_account("123")
print(account1.get_balance())