def CheckEven(No):
    if(No % 2 == 0):
        print("Number is even")
    else:
        print("Number is odd")

def main():
    print("Enter number : ")
    A = int(input())

    CheckEven(A)

# Starter
if __name__ == "__main__":
    main()
