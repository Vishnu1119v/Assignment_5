class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num2+self.num1
    def subtract(self):
        return self.num2-self.num1
    def multiply(self):
        return self.num2*self.num1
    def divide(self):
        return self.num2/self.num1
obj = Calculator(10, 94)
print(f'addition: {obj.add()}')
print(f'subtraction :{obj.subtract()}')
print(f'multiplication :{obj.multiply()}')
print(f'division :{obj.divide()}')
        
    
