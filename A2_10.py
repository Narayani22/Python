# Assignment No-2 Q.10

# Defination of Function
def CountDigits(No):
    Sum = 0
    #iDigit = 0

    while(No != 0):
        Sum = Sum + No % 10
        No = No // 10
    return Sum

def main():
    print("Enter the Number: ")
    Num = int(input())

    Result = CountDigits(Num)
    print("Number of digits are: ",Result)

if __name__ == "__main__":
    main()

# Defination of Function