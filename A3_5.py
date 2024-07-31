# Assignment No-3 Q.5
import MarvellousNum

def main():
    print("Enter the length of list :")
    size = int(input())

    Arr = list()
    print("Enter the elements of list :")
    
    for i in range(size):
        no = int(input())
        Arr.append(no)

    print("Entered elements are : ",Arr)

    Result = MarvellousNum.ListPrime(Arr)
    print("Addition of all prime elements is : ",Result)

if __name__ == "__main__":
    main()