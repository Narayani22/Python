# Name = lambda parameters : Logic
# Name(___, ___, .....)

def Addition(A,B):
    Ans = 0
    Ans = A + B
    return Ans

Add = lambda A,B : A+B
def main():
    Ret = Add(10,11)
    print("Addition is : ",Ret)
    
if __name__ == "__main__":
    main()