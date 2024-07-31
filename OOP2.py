
class Demo:
    Data1 = 11          # Class variable
    Data2 = 21          # Class variable

    def __init__(self, A, B):   # instance method
        print("Inside constrctor")
        self.No1 = A    # instance variable
        self.No2 = B    # instance variable

    def Display(self):          # instance method
        print("Value of No1 from display : ",self.No1)
        print("Value of No2 from display : ",self.No2)
        print("Value of Data1 from display : ",Demo.Data1)
        print("Value of Data2 from display : ",Demo.Data2)

    @classmethod
    def Fun(cls):       # class method
        print("Value of Data1 from Fun : ",Demo.Data1)
        print("Value of Data2 from Fun : ",Demo.Data2)

    @staticmethod
    def Gun():       # static method
        print("Inside static method")

Demo.Fun()
Demo.Gun()
obj = Demo(5,10)
obj.Display()
