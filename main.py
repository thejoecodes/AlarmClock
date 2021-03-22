#Alarm Clock Project
#importing required libraries

from tkinter import *
import datetime
import time
#winsound works only for windows operating system, for linux sound has to be hard-coded into /dev/audio folder
#for mac-os, I am still doing my research, though I lack the platform to experiment 😊
#import winsound

def alarm(set_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d%m%Y")
        print("The set date is: "+date)
        print(now)
        if now == set_timer:
            print("Wakey Wakey! Its time to chase your dreams!")
        print("\a")
        #winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break

def actual_time():
    set_timer = f"{hour.get()}:{mins.get()}:{sec.get()}"
    alarm(set_timer)

clock = Tk() #the Tk() is used in innitializing the tkinter module

clock.title("Simple Alarm Clock")
clock.geometry("400x200")
time_format = Label(clock, text="Enter Time in 24 hour format!", fg="red", bg="black", font="Aerial").place(x=60, y=120)
add_time = Label(clock, text="Hour Min Sec", font = 60).place(x=110)
set_alarm = Label(clock, text="When are you waking up?", fg="blue", relief="solid", font=("Helevetica",7,"bold")).place(x=0, y=29)

#the variable required to set the alarm
hour = StringVar()
mins = StringVar()
sec = StringVar()

#Time
hourTime = Entry(clock, textvariable = hour, bg="pink", width = 15).place(x=110, y=30)
minsTime = Entry(clock, textvariable = mins, bg="pink", width = 15).place(x=150, y=30)
secTime = Entry(clock, textvariable = sec, bg="pink", width = 15).place(x=200, y=30)

#Time input by user
submit = Button(clock, text="Set Alarm", fg="red", width=10, command=actual_time()).place(x=110, y=70)

clock.mainloop()


