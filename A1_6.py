# Assignment No-1 Q.6

# Defination of Function
def ChkNum(No):
    if(No > 0):
        print("Positive Number")
    elif(No == 0):
        print("Zero Number")
    else:
        print("Negative Number")
        

def main():
    print("Enter number : ")
    A = int(input())

    # Function Call
    ChkNum(A)

# Starter
if __name__ == "__main__":
    main()