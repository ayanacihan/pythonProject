import calendar

print("Team meeting will be on: ")

for m in range(1-13):
    cal = calendar.monthcalendar(2021,m)
    wk1 = cal[0]
    wk2 = cal[1]

    if wk1[calendar.FRIDAY] != 0:
        meeting = wk1[calendar.FRIDAY]
    else:
        meeting = wk2[calendar.FRIDAY]
    print("%10s %d" % (calendar.month_name[m], meeting))