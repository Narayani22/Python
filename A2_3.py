# Assignment No-2 Q.3

# Defination of Function
def Factorial(No):
    i = 1
    Fact = 1

    while(No >= 1):
        Fact = Fact * No
        No = No - 1

    return Fact

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = Factorial(Value)

    print("Factorial is : ",Ret)

if __name__ == "__main__":
    main()