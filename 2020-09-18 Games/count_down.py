#This script is a countdown clock application
from tkinter import * #tkinter is highly configurable
from tkinter import ttk #Why did we import ttk even though we imported * of tkinter? #ttk is not higly configurable
from tkinter import font
import time
import datetime

global endTime #Global variable creation

def quit(*args): #When you are not sure how many arguments will take your function, you write *args
    root.destroy()

def cant_wait():
#Get the time remaining until the event
    timeLeft = endTime - datetime.datetime.now()
#Remove the miliseconds part
    timeLeft = timeLeft - datetime.timedelta(microseconds=timeLeft.microseconds)
#Show the time left
    txt.set(timeLeft)
#Trigger the countdown after 1000ms
    root.after(1000, cant_wait)
#Use the tkinter lib for showing the clock
root = Tk() #buttons are widgets put in root. Here root is the main window
root.attributes("-fullscreen", False)
root.configure(background='black')
root.bind("x", quit)
root.after(1000, cant_wait)
#Set the end date and time for the countdown
endTime = datetime.datetime(2020, 9, 30, 0, 0) #first 0 is hours, second 0 is minutes

fnt = font.Font(family='Helvetica', size=90, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground='white', background='black')
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()