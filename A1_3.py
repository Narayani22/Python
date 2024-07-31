# Assignment No-1 Q.3

# Defination of Function
def Add(A,B):
    Ans = A + B 
    return Ans

def main():
    print("Welcome to the application : ")
    print("Enter first number : ")
    No1 = int(input())

    print("Enter second number : ")
    No2 = int(input())

    # Function Call
    Result = Add(No1,No2)

    print("Addition is : ",Result)

# Starter   
if __name__ == "__main__":
    main()