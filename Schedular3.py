import datetime
import time 
import schedule

def schedule_Minute():
    print("Schedular executes after each minute : ",datetime.datetime.now())

def main():
    print("Current time is ",datetime.datetime.now())

    schedule.every(1).minutes.do(schedule_Minute)
    
if __name__ == "__main__":
    main()