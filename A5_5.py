# Assignment No-5 Q.5
i = 1
Fact = 1

def Factorial(No):
    global i
    global Fact

    if(No >= 1):
        Fact = Fact * No
        No = No - 1
        Factorial(No)

    return Fact

def main():
    print("Enter the number : ")
    Value = int(input())

    Ret = Factorial(Value)

    print("Factorial is : ",Ret)

if __name__ == "__main__":
    main()