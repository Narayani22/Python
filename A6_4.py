import threading

def SmallDisplay(Value):
    small_chars = sum(1 for char in Value if char.islower())
    print("TID of small thread ",threading.get_ident())
    print("Number of small characters are : ",small_chars)
    
def CapitalDisplay(Value):
    capital_chars = sum(1 for char in Value if char.isupper())
    print("TID of captial thread ",threading.get_ident())
    print("Number of capital characters are : ",capital_chars)
    
def DigitDisplay(Value):
    digits = sum(1 for char in Value if char.isdigit())
    print("TID of digit thread ",threading.get_ident())
    print("Number of digits are : ",digits)

def main():
    print("Enter the string:")
    Value = input()

    small = threading.Thread(target = SmallDisplay, args = (Value,))
    capital = threading.Thread(target = CapitalDisplay, args = (Value,))
    digit = threading.Thread(target = DigitDisplay, args = (Value,))
 
    small.start()
    capital.start()
    digit.start()

    small.join()
    capital.join()
    digit.join()
    
    print("End of main process")

if __name__ == "__main__":
    main()