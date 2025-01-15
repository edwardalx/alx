class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance
    
    def deposit(self,amount):
        self.account_balance += amount
        return 

    def withdraw(self,amount):
        if  self.account_balance > amount:
            result = self.account_balance - amount
            return result
        else:
            False
    
    def display_balance(self):
        result = ["Current Balance:"]
        return print(f"{result[0]} ${self.account_balance}")

