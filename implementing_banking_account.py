class Account:
    def __init__(self,title=None,Balance=0):
        self.title=title
        self.Balance=Balance

class SavingsAccount(Account):
    def __init__(self,title,Balance,interestRate):  
        super().__init__(title,Balance)
        self.interestRate=interestRate
        

demo1 = SavingsAccount("Ashish", 2000, 5)
