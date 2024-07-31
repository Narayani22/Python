# Defination of Function
def ChkNum(No):
    if(No % 2 == 0):
        return True
    else:
        return False

# EvenOdd = lambda No : 
def main():
    print("Enter number : ")
    A = int(input())

    # Function Call
    Ret = EvenOdd(A)
    if(Ret == True):
        print("Even Number")
    else:
        print("Odd Number")

# Starter
if __name__ == "__main__":
    main()