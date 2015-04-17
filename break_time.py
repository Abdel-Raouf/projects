import time
import webbrowser

total_breaks = 3

break_count = 0


print ("this program starts on " + time.ctime())
while (break_count<total_breaks) :

    time.sleep(2*60*60)
    webbrowser.open('https://www.youtube.com/watch?v=CevxZvSJLk8')
    break_count = break_count + 1
