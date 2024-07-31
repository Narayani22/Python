# Assignment No-3 Q.4

# Defination of Function
def Frequency(Data,Value):
    Freq = 0

    for no in Data:
        if(no == Value):
            Freq = Freq + 1
    
    return Freq

def main():
    print("Enter the length of list :")
    size = int(input())

    Arr = list()
    print("Enter the elements of list :")
    
    for i in range(size):
        no = int(input())
        Arr.append(no)

    print("Enter element to find the frequency : ")
    Value = int(input())

    Result = Frequency(Arr,Value)
    print("Frequency of element is : ",Result)

if __name__ == "__main__":
    main()