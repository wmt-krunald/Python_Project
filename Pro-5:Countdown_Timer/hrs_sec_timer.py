import time
t = int(input("\nEnter Time in Seconds : "))

def get_timer(t):
    while t >= 0:
        hrs = t // 3600
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}:{:02d}'.format(hrs, mins, secs)
        print(timer , end="\r")
        time.sleep(1)
        t -= 1

get_timer(t)
print(f"\nComplete the Time of {t} seconds.")