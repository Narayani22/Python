
class Arithematic:
    def __init__(self, No1, No2): 
        self.Value1 = No1  
        self.Value2 = No2  

    def Addition(self):     
        Ans = self.Value1 + self.Value2
        print("Addition is : ", Ans)

    def Substraction(self):
        Ans = self.Value1 - self.Value2
        print("Substraction is : ", Ans) 

    def Multiplication(self):
        Ans = self.Value1 * self.Value2
        print("Multiplication is : ", Ans) 

    def Division(self):
        Ans = self.Value1 / self.Value2
        print("Division is : ", Ans) 

print("Enter first number")
A = int(input())

print("Enter second number")
B = int(input())

obj = Arithematic(A,B)

obj.Addition()
obj.Substraction()
obj.Multiplication()
obj.Division()