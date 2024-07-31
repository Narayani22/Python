# Assignment No-2 Q.5

# Defination of Function
def Prime(No):
    for i in range(2,No):
        if(No % i) == 0:
            return False
        else:
            return True 
            
def main():
    print("Enter the number : ")
    Value = int(input())

    Result = Prime(Value)
    if(Result == True):
        print("It is a prime number")
    else:
        print("It is not a prime number")

if __name__ == "__main__":
    main()