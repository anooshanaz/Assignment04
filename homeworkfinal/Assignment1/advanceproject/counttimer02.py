#count down timer

import time

def count_down_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d} {:02d}'.format(mins,secs)
        print(time_format,end='\r')
        time.sleep(1) #1 sec delay
        seconds -= 1
    print("00:00 \n Time's up's")

#user_input_timmer
total_seconds = int(input("Enter time seconds for count down: "))
count_down_timer(total_seconds)


