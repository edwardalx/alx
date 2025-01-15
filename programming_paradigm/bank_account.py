class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance
    
    def deposit(self,amount):
        self.account_balance += amount
        return 

    def withdraw(self,amount):
        if amount > self.account_balance:
            return  False
        self.account_balance -= amount
        return 
    
    def display_balance(self):
        result = ["Current Balance:"]
        return print(f"{result[0]} {self.account_balance}")

