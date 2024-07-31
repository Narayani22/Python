def Display(No):
    i = 0

    if(No <= 0):
        print("Invalid input")
        return

    for No in range(No):
        print("Jay Ganesh...")

def main():
    print("Enter frequency : ")
    A = int(input())

    Display(A)

# Starter
if __name__ == "__main__":
    main()
