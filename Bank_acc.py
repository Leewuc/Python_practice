class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self,amount):
        if self.account_number == True:
            self.balance += amount
    def withdraw(self,amount):
        if self.account_number == True:
            self.balance -= amount 
    def display_balance(self):
        return self.balance
ba = BankAccount(123,3000)
print(ba.account_number,ba.balance)