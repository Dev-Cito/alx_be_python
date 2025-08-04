class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
    
    def deposit(self, amount):
        self.account_balance += amount
        return f"Deposited: ${amount}"
    
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        return f"Current Balance: ${self.account_balance:.2f}"

# Test code - you might need something like this
if __name__ == "__main__":
    # Example that would produce "Current Balance: $250.00"
    account = BankAccount(250)
    print(account.display_balance())
