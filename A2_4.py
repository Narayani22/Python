# Assignment No-2 Q.4

# Defination of Function
def SumFact(No):
    iSum = 0

    for iCnt in range(1, No + 1):
        if(No % iCnt) == 0:
            iSum = iSum + iCnt
    return iSum

def main():
    print("Enter the number : ")
    Value = int(input())

    Result = SumFact(Value)
    print("Summation of factors is : ",Result)

if __name__ == "__main__":
    main()