
class Demo:
    Value = 22          # Class variable

    def __init__(self, A, B):   # instance method
        print("Inside constrctor")
        self.No1 = A    # instance variable
        self.No2 = B    # instance variable

    def Fun(self):          # instance method
        print("Value of No1 from Fun : ",self.No1)
        print("Value of No2 from Fun : ",self.No2)
        print("Value of Value from Fun : ",Demo.Value)

    def Gun(self):          # instance method
        print("Value of No1 from Gun : ",self.No1)
        print("Value of No2 from Gun : ",self.No2)
        print("Value of Value from Gun : ",Demo.Value)

obj1 = Demo(11,21)

obj2 = Demo(51,101)

obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()
