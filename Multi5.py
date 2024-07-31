import multiprocessing

def EvenDisplay(No):
    print("List of even numbers : ")
    x = 2
    for i in range(No):
        print(x)
        x = x + 2

def OddDisplay(No):
    print("List of odd numbers : ")
    x = 1
    for i in range(No):
        print(x)
        x = x + 2

def main():
    print("Enter the number:")
    Num = int(input())

    p1 = multiprocessing.Process(target = EvenDisplay, args = (Num,))
    p2 = multiprocessing.Process(target = OddDisplay, args = (Num,))

# Not a good way of programming, it will execute in a serial way
   
    p1.start()
    p1.join()

    p2.start()
    p2.join()
    
    print("End of main process")

if __name__ == "__main__":
    main()
