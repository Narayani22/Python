import os

def main():
    print("Enter the name of file that you want to create : ")
    Fname = input()

    if os.path.exists(Fname):
        print("Unable to create file as file is already existing")

    else:
        open(Fname, "x")
        print("File gets sucessfully created")

if __name__ == "__main__":
    main()

# Absolute path : c:/user/desktop/python/automation/marvellous.txt
# Relation path : Automations/Marvellous.txt