import time
t = int(input("\nEnter Time in Second : "))

def get_timer(t):
    while t >= 0:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer , end="\r")
        time.sleep(1)
        t -= 1
    
    

get_timer(t)
print(f"\nComplete the Time of {t} seconds.")