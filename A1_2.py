# Assignment No-1 Q.2

# Defination of Function
def ChkNum(No):
    if(No % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    print("Enter number : ")
    A = int(input())

    # Function Call
    ChkNum(A)

# Starter
if __name__ == "__main__":
    main()