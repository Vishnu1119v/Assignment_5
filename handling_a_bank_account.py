class Account:
    def __init__(self,title=None,Balance=0):
        self.title=title
        self.Balance=Balance
    def withdrawal(self, amount):
        self.Balance-=amount

    def deposit(self, amount):
        self.Balance+=amount
    
    def getBalance(self):
        return self.Balance

class SavingsAccount(Account):
    def __init__(self,title,Balance,interestRate):
        super().__init__(title,Balance)
        self.interestRate=interestRate
    def interestAmount(self):
        interest_amount=(self.interestRate*self.Balance)/100
        return interest_amount

demo1= SavingsAccount("Ashish", 2000, 5)
demo1.deposit(500)
print(f'balance after depositing 500 :{demo1.getBalance()}')

demo1.withdrawal(1000)
print(f'balance after withdrawing 1000 :{demo1.getBalance()}')

print(f'interest amount on the current balance: {demo1.interestAmount()}')
