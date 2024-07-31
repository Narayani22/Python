# Defination of Function
def ChkNum(No):
    return (No % 2 == 0)

CheckEvenX = lambda No : (No % 2 == 0)

def main():
    print("Enter number : ")
    A = int(input())

    # Function Call
    Ret = CheckEvenX(A)
    if(Ret == True):
        print("Even Number")
    else:
        print("Odd Number")

# Starter
if __name__ == "__main__":
    main()