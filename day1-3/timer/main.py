from datetime import timedelta, datetime 
from time import sleep

#TODO: implement a basic timer object with start, stop, and elapsed

class Timer:
    def __init__(self, amount: timedelta):
        self.amount = amount
    
    def runTimer(self):
        end = self.amount + datetime.now()
        while datetime.now() < end:
            print(f"{end - datetime.now()} seconds are remaining")
            sleep(1)
        print("TIME IS UP!")


def main():
    ten_second_timer = Timer(timedelta(0,10))
    ten_second_timer.runTimer()

if __name__ == "__main__":
    main()