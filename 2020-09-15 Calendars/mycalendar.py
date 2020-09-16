#The name of your Python file (here it's mycalendar.py)
import calendar

#cal = calendar.TextCalendar(calendar.MONDAY)
cal = calendar.HTMLCalendar(calendar.MONDAY) #this is
str = cal.formatmonth(2020,9)

print(str)