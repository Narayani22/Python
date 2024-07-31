# Assignment No-2 Q.1
import Marvellous

def main():
    print("Enter first number : ")
    A = int(input())

    print("Enter second number : ")
    B = int(input())

    Ans = Marvellous.Addition(A,B)
    print("Addition is : ",Ans)

    Ans = Marvellous.Substraction(A,B)
    print("Substraction is : ",Ans)
    
    Ans = Marvellous.Multiplication(A,B)
    print("Multiplication is : ",Ans)

    Ans = Marvellous.Division(A,B)
    print("Division is : ",Ans)

main()