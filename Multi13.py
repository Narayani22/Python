import multiprocessing
import os 
import time

def Fun(No):
    Sum = 0
    print("PID is : ",os.getpid())
    for i in range(No):
        Sum = Sum + (No*No*No)

    return Sum 

def main():
    starttime = time.time()

    Arr = [1000,2000,3000,4000,5000,6000,7000,8000,9000]
    Result = []

    for Value in Arr:
        Result.append(Fun(Value))

    print(Result)
    endtime = time.time()
    print("Time required for execution : ",endtime-starttime)
    
if __name__ == "__main__":
    main()    