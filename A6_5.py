import threading

def Display(start, end):
    for i in range(start, end + 1):
        print(i)

def ReverseDisplay(start, end):
    for i in range(start, end - 1, -1):
        print(i)

def main():

    thread1 = threading.Thread(target = Display, args = (1, 50,))
    thread2 = threading.Thread(target = ReverseDisplay, args = (50, 0,))
 
    thread1.start()
    thread1.join()
    
    thread2.start()
    thread2.join()

    print("End of main process")

if __name__ == "__main__":
    main()