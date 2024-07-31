i = 1

def DisplayR(Num):
    global i
    
    if(i <= Num):
        print(i)
        i = i + 1
        DisplayR(Num)

def main():
    print("Enter the number : ")
    No = int(input())

    DisplayR(No)

if __name__ == "__main__":
    main()