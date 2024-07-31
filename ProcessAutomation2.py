import psutil

def DisplayProcess():
    print("List of running processess are : ")

    print("___________________________________________________________")

    for proc in psutil.process_iter(['pid' , 'name' , 'username']):
        print(proc.info)

    print("___________________________________________________________")

def main():
    DisplayProcess()

if __name__ == "__main__":
    main()