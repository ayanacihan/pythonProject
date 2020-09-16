from datetime import date

daysAhead = date.today()

xmas = date(daysAhead.year, 12, 25)

timetoxmas = xmas - daysAhead #subtracting the christmas and daysAhead

print("It's just", timetoxmas.days, "days till Christmas 2020")