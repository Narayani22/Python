import threading

def EvenDisplay(No):
    even_factors = [i for i in range(1, No + 1)
        if(No % i == 0 and i % 2 == 0)]
    even_factors_sum = sum(even_factors)
    print("Sum of even factors:", even_factors_sum)

def OddDisplay(No):
    odd_factors = [i for i in range(1, No + 1)
        if(No % i == 0 and i % 2 != 0)]
    odd_factors_sum = sum(odd_factors)
    print("Sum of odd factors:", odd_factors_sum)


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