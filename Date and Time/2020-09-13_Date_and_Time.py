from datetime import date #name your file different than the module you import.
from datetime import time
from datetime import datetime

today = date.today() #we called the date class and the today method.
print("Today is", today)

print("The date components are", today.day, today.month, today.year) #we called the day, month and year seperately.

print("The weekday number is", today.weekday()) #this method displays the current day.

days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"] #this prints the days.
for x in days:
    print(x)

print("The weekday is", days[today.weekday()]) #this prints the day.

today = datetime.now() #we called the now method from datetime class of datetime module.
print("The current time is", today)

t = datetime.time(datetime.now()) #this only will display the time not the date
print(t)