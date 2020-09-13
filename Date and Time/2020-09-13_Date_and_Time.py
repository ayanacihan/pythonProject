from datetime import date #name your file different than the module you import.
from datetime import time
from datetime import datetime

today = date.today() #we called the date class and the today method.
print("Today is", today)

print("The date components are", today.day, today.month, today.year) #we called the day, month and year seperately.

print("The weekday number is", today.weekday())