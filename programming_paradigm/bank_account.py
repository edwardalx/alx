class BankAccount:
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance
    
    def deposit(self,amount):
        self.account_balance += amount
        return self.account_balance

    def withdraw(self,amount):
        if  self.account_balance > amount:
            self.account_balance -= amount
            return self.account_balance
        else:
            False
    
    def display_balance(self):
        result = ["Current Balance:"]
        return print(f"{result[0]} ${round(self.account_balance,2):.2f}")

myBank = BankAccount(50)
print(myBank.deposit(50))

myBank.display_balance()

print(myBank.withdraw(20))

myBank.display_balance()