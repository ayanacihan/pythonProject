import calendar

cal = calendar.TextCalendar(calendar.MONDAY)

for days in cal.itermonthdays(2020,9):
    print(days)

#local time is also available
for months in calendar.month_name:
    print(months)

for day in calendar.day_name:
    print(day)

for day_abbr in calendar.day_abbr:
    print(day_abbr)
