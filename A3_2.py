# Assignment No-3 Q.2

# Defination of Function
def Maximum(Data):
    Max = Data[0]

    for no in Data:
        if(no > Max):
            Max = no
    
    return Max

def main():
    print("Enter the length of list :")
    size = int(input())

    Arr = list()
    print("Enter the elements of list :")
    
    for i in range(size):
        no = int(input())
        Arr.append(no)

    print("Entered elements are : ",Arr)

    Result = Maximum(Arr)
    print("Maximum from all elements is : ",Result)

if __name__ == "__main__":
    main()