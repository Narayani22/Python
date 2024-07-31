# Assignment No-2 Q.7

# Defination of Function
def Display(A):
    for i in range(A + 1):
        for j in range(A + 1):
            print(j, end=' ')
        print()

def main():
    print("Enter number : ")
    No = int(input())
    # Function Call
    Display(No)

# Starter
if __name__ == "__main__":
    main()