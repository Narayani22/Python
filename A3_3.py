# Assignment No-3 Q.3

# Defination of Function
def Minimum(Data):
    Min = Data[0]

    for no in Data:
        if(no < Min):
            Min = no
    
    return Min

def main():
    print("Enter the length of list :")
    size = int(input())

    Arr = list()
    print("Enter the elements of list :")
    
    for i in range(size):
        no = int(input())
        Arr.append(no)

    print("Entered elements are : ",Arr)

    Result = Minimum(Arr)
    print("Minimum from all elements is : ",Result)

if __name__ == "__main__":
    main()