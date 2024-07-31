def Prime(no):
    for i in range(2,no):
        if(no % i) == 0:
            return False
        else:
            return True 

def ListPrime(Data):
    Sum = 0
    for no in Data:
        if Prime(no):
            Sum = Sum + no
            return Sum
