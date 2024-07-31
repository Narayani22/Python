# Assignment No-2 Q.2

# Defination of Function
def Display(A):
    for i in range(A):
        print(" * " * A)

def main():
    print("Enter number : ")
    No = int(input())
    # Function Call
    Display(No)

# Starter
if __name__ == "__main__":
    main()