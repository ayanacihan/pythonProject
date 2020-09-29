from datetime import date

daysAhead = date.today()

birthday = date(2021, 1, 18)
#There are 2 options for calculating it.
#timetobirthday = birthday - daysAhead #subtracting the christmas and daysAhead
timetobirthday = date(2021, 1, 18) - daysAhead #subtracting the christmas and daysAhead

print("It's just", timetobirthday.days, "days till Birthday of my son")