import threading

def EvenDisplay(No):
    print("List of even numbers : ")
    x = 2
    for i in range(No):
        print("Even : ",x)
        x = x + 2

def OddDisplay(No):
    print("List of odd numbers : ")
    x = 1
    for i in range(No):
        print("Odd : ",x)
        x = x + 2

def main():
    print("Enter the number:")
    Num = int(input())

    Even = threading.Thread(target = EvenDisplay, args = (Num,))
    Odd = threading.Thread(target = OddDisplay, args = (Num,))
 
    Even.start()
    Odd.start()

    Even.join()
    Odd.join()
    
    print("End of main process")

if __name__ == "__main__":
    main()
