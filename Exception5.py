
def main():
    Ans = 0

    try:
        print("Enter first number : ")
        No1 = int(input())

        print("Enter second number : ")
        No2 = int(input())

        Ans = No1 / No2

    except ZeroDivisionError as zobj:
        print("Exception occured ",zobj)

    except ValueError as vobj:
        print("Exception occured ",vobj)
    
    finally:
        print("Inside finally block")
        
    print("Division is : ",Ans)

if __name__ == "__main__":
    main()