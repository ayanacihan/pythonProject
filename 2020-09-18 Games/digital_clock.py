#We are creating a digital clock
from tkinter import * #tkinter is used for interfaces. * is importing the all classes from tkinter object
from tkinter import ttk
from tkinter import font
import time
import datetime

def quit(*args): #* is used pass several arguments not keywords of python
    root.destroy()

def clock_time():
#Get the time remaining until the event
    time = datetime.datetime.now()
    time = (time.strftime("%H:%M:%S"))
#    txt.set(time)

    root.after(1000, clock_time())

root = Tk() #root is kind of a basket you put all of your widgets
root.attributes("-fullscreen",False)
root.configure(background='black')
root.bind("x",quit)
#root.after(1000,clock_time())
fnt = font.Font(family="Helvetica", size=60, weight='bold')
txt = StringVar()
lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="white", background="black")
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()