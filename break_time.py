import time
import webbrowser

total_breaks = 3
break_count = 0

while (break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("http://www.youtube.com/watch?v=dQw4w9WgXcQ")

    print ("It is " + time.ctime() + ". Take a break!")
    break_count = break_count + 1
