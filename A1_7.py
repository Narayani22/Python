# Assignment No-1 Q.7

# Defination of Function
def ChkNum(No):
    if(No % 5 == 0):
        return True
    else:
        return False

def main():
    print("Enter number : ")
    A = int(input())

    # Function Call
    Ret = ChkNum(A)

    if(Ret == True):
        print("Number is divisible by 5")
    else:
        print("Number is not divisible by 5")

# Starter
if __name__ == "__main__":
    main()