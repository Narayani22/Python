
class Circle:
    PI = 3.14          # Class variable

    def __init__(self, A):   # instance method
        self.Radius = A    # instance variable
        self.Area = 0.0   # instance variable
        self.Circumference = 0.0    # instance variable

    def CalculateArea(self):          # instance method
        Area = self.PI * self.Radius * self.Radius
        print("Area of Circle is : ",Area)

    def CalculateCircumference(self):          # instance method
        Circumference = 2 * self.PI * self.Radius 
        print("Circumference of Circle is : ",Circumference)

    def Display(self):
        print("Radius is : ",self.Radius)
        print("Area is : ",self.Area)
        print("Circumference is : ",self.Circumference)

print("Enter Radius")
A = int(input())

obj = Circle(A)

obj.Display()
obj.CalculateArea()
obj.CalculateCircumference()