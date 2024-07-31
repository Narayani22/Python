import datetime
import time 
import schedule

def schedule_Minute():
    print("Schedular executes after each minute : ",datetime.datetime.now())

def schedule_Hour():
    print("Schedular executes after each hour : ",datetime.datetime.now())

def schedule_Sunday():
    print("Schedular executes after each Sunday : ",datetime.datetime.now())

def main():
    print("Current time is ",datetime.datetime.now())

    schedule.every(1).minutes.do(schedule_Minute)
    schedule.every(1).hour.do(schedule_Hour)
    schedule.every(1).sunday.do(schedule_Sunday)
    
    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()