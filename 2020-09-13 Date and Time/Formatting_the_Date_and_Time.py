from datetime import date
from datetime import datetime
from datetime import time

today = datetime.now()

print(today) #this gives the date and time information.

print(today.strftime("The current year is: %Y")) #this gives only the year information
print(today.strftime("The current day is: %M")) #this displays only the day information
print(today.strftime("%a, %d, %y")) #this displays them seperately

print(today.strftime("%c")) #this time is local, directive c
print(today.strftime("%x")) #this is local date, directive x
print(today.strftime("%X")) #this is local time, directive X

print((today.strftime("%I:%M:%S%p"))) #hour / minute / second
print((today.strftime("%I:%M %p"))) #hour / minute