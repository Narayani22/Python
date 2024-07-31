# Assignment No-3 Q.1

# Defination of Function
def Addition(Data):
    Sum = 0

    for no in Data:
        Sum = Sum + no
    
    return Sum

def main():
    print("Enter the length of list :")
    size = int(input())

    Arr = list()
    print("Enter the elements of list :")
    
    for i in range(size):
        no = int(input())
        Arr.append(no)

    print("Entered elements are : ",Arr)

    Result = Addition(Arr)
    print("Summation of all elements is : ",Result)

if __name__ == "__main__":
    main()