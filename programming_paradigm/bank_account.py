class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance
    
    def deposit(self,amount):
        if amount <= 0:
            return "Enter a positive deposit amount"
        self.account_balance += amount
        return f"You deposited: {amount}, your new balance: {self.account_balance}"

    def withdraw(self,amount):
        if amount > self.account_balance:
            return  f"Your balance of  {self.account_balance} is not sufficent"
        self.account_balance -= amount
        return f"You've withdrawn {amount} and your new balance {self.account_balance}"
    
    def display_balance(self):
        return f"Your current balance: {self.account_balance} "

