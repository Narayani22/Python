import sys
import os
import time 

def DirectoryWatcher(DirName):

    flag = os.path.isabs(DirName)

    if (flag == False):
        print("Path is not a absolute path")
        DirName = os.path.abspath(DirName)
        print("Converted absolute path is : ",DirName)

    exist = os.path.isdir(DirName)

    if(exist == True):
        for foldername, subfoldername, filename in os.walk(DirName):
            print("Current folder is : ",foldername)
            
            for subname in subfoldername:
                print("Sub folder name is : ",subname)

            for name in filename:
                print("File name is : ",name)
    else:
        print("There is no such directory")
        
def main():
    print("-------------------------------------------------------")
    print("------------------ Directory Watcher ------------------")
    print("-------------------------------------------------------")

    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to perform Directory traversal")
            exit()

        if(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage of the script : ")
            print("Name_of_File  Name_Of_Directory")
            exit()
        
        try:
            starttime = time.time()

            DirectoryWatcher(sys.argv[1])

            endtime = time.time()

            print("Time required to execute the script is : ",endtime-starttime)

        except Exception as onj2:
            print("Unable to perform the task due to ", obj2)
            
    else:
        print("Invalid option")
        print("Use --h option to get the help and use --u option to get the usage of the application")
        exit()

    print("-------------------------------------------------------")
    print("---------- Thank you for using our script -------------")
    print("-------------- Marvellous Infosystems -----------------")
    print("-------------------------------------------------------")

if __name__ == '__main__':
    main()