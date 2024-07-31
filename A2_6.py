# Assignment No-2 Q.6

# Defination of Function
def Display(A):
    for i in range(A):
        for j in range(A - i):
            print(" * ", end=' ')
        print()

def main():
    print("Enter number : ")
    No = int(input())
    # Function Call
    Display(No)

# Starter
if __name__ == "__main__":
    main()