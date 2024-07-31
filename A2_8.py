# Assignment No-2 Q.8

# Defination of Function
def Display(A):
    for i in range(A + 1):
        for j in range(i + 1):
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