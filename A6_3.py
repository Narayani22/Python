import threading

def EvenDisplay(No):
    even_elements = [i for i in No if(i % 2 == 0)]
    even_elements_sum = sum(even_elements)
    print("Sum of even elements:", even_elements_sum)

def OddDisplay(No):
    odd_elements = [i for i in No if(i % 2 != 0)]
    odd_elements_sum = sum(odd_elements)
    print("Sum of odd elements:", odd_elements_sum)


def main():
    print("Enter the length of list :")
    size = int(input())

    Arr = list()

    print("Enter the elements of list :")
    
    for i in range(size):
        no = int(input())
        Arr.append(no)

    Even = threading.Thread(target = EvenDisplay, args = (Arr,))
    Odd = threading.Thread(target = OddDisplay, args = (Arr,))
 
    Even.start()
    Odd.start()

    Even.join()
    Odd.join()
    
    print("End of main process")

if __name__ == "__main__":
    main()