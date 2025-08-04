class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            return f"Deposited: ${amount:.1f}"
        else:
            return "Deposit amount must be positive."

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return f"Withdrew {amount} successfully."
        else:
            return "Insufficient funds."

    def display_balance(self):
        return f"Current Balance:{self.__account_balance}"
        
my_account = BankAccount()

print(my_account.deposit(200))




