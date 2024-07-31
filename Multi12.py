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

    Arr = [1000,2000,3000,4000,5000]
    Result = []

    p = multiprocessing.Pool()
    Result = p.map(Fun,Arr)
    p.close()
    p.join()

    print(Result)
    endtime = time.time()
    print("Time required for execution : ",endtime-starttime)
    
if __name__ == "__main__":
    main()    