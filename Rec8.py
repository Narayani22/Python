i = 1

def DisplayR(Num):
    global i
    
    if(Num >= 1):
        print(Num)
        Num = Num - 1
        DisplayR(Num)

def main():
    print("Enter the number : ")
    No = int(input())

    DisplayR(No)

if __name__ == "__main__":
    main()