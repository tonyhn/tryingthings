class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def addNum(self):
        return float(self.a+ self.b)
    
    def multiplyNum(self):
        return float(self.a*self.b)
    
    def subNum(self):
        return self.a-self.b


a = float(input("Enter the first number... "))
b = float(input("Enter the second number... "))
calc = Calculator(a,b)
print(calc.addNum())
print(calc.multiplyNum())