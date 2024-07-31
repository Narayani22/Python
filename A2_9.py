# Assignment No-2 Q.9

# Defination of Function
def CountDigits(No):
    iCnt = 0
    #iDigit = 0

    while(No != 0):
        No = No // 10
        iCnt = iCnt + 1
    return iCnt

def main():
    print("Enter the Number: ")
    Num = int(input())

    Result = CountDigits(Num)
    print("Number of digits are: ",Result)

if __name__ == "__main__":
    main()