# Assignment No-4 Q.3
from functools import reduce

CheckNum = lambda No : (70 <= No <= 90)

Increase = lambda No : No + 10

Add = lambda A,B : A * B

def main():
    Data = []

    print("Enter number of elements : ")
    Size = int(input())

    print("Enter the elements : ")
    iCnt = 0
    for iCnt in range(0,Size):
        No = int(input())
        Data.append(No)

    print("Data from input list : ",Data)

    FData = list(filter(CheckNum,Data))
    print("Data after filter activity : ",FData)

    MData = list(map(Increase,FData))
    print("Data after map activity : ",MData)

    RData = reduce(Add,MData)
    print("Data after reduce activity : ",RData)

if __name__ == "__main__":
    main()
