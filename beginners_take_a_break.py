import time
import schedule
import webbrowser

total_breaks = 7
break_count = 0

print("This program started on "+time.ctime())
while break_count < total_breaks:
    time.sleep(3600)
    webbrowser.open("https://www.youtube.com/watch?v=ZbZSe6N_BXs")
    break_count = break_count + 1

schedule.every().day.at("08:00").do(break_count)