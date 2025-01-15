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
            return  f"Insufficient funds."
        self.account_balance = self.account_balance - amount
        return f"You've withdrawn {amount} and your new balance {self.account_balance}"
    
    def display_balance(self):
        result = ["Current Balance:"]
        return print(f"{result[0]} is {self.account_balance}")
    
account = BankAccount(200)  # Assume an initial balance of 200
print(account.withdraw(150))  # Output: You've withdrawn 150 and your new balance is 50
print(account.withdraw(100))  # Output: Insufficient funds.

