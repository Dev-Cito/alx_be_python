

class BankAccount :
    def __init__(self, account_balance = 0) :
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
    def withdraw(self, amount):
        if amount > self.account_balance :
            return False
        elif amount < self.account_balance :
            return True
            self.account_balance -= amount
        else :
            print("Something went wrong!")
    def display_balance(self):
        return f"Current Balance:{self.account_balance}"

    
my_account = BankAccount()
print(my_account.deposit(200))
print(my_account.withdraw(10))
print(my_account.display_balance())




class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        return f"Deposited {amount} successfully."

    def withdraw(self, amount):
        if amount > self.account_balance:
            return "Insufficient balance."
        else:
            self.account_balance -= amount
            return f"Withdrew {amount} successfully."

    def display_balance(self):
        return f"Current balance: {self.account_balance}"


my_account = BankAccount()

print(my_account.deposit(200))
print(my_account.withdraw(100))
print(my_account.display_balance())


