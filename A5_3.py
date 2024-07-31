# Assignment No-5 Q.3

def DisplayR(Num):
    
    if(Num != 0):
        print(Num,end= " ")
        Num = Num - 1
        DisplayR(Num)

def main():
    print("Enter the number : ")
    No = int(input())

    DisplayR(No)

if __name__ == "__main__":
    main()