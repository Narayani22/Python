def Display(No):
    i = 0

    if(No <= 0):
        print("Invalid input")
        return

    while(i < No):
        print("Jay Ganesh", end = " ")
        i = i + 1

def main():
    print("Enter frequency : ")
    A = int(input())

    Display(A)

# Starter
if __name__ == "__main__":
    main()
