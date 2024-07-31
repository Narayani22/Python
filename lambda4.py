# Name = lambda parameters : Logic
# Name(___, ___, .....)

CubeX = lambda A : A**3

def main():
    print("Enter the number : ")
    No1 = int(input())

    Ret = CubeX(No1)
    print("Cube is : ",Ret)
    
if __name__ == "__main__":
    main()