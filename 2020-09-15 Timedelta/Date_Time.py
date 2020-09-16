from datetime import datetime
from datetime import timedelta #this is timedelta class. Calculation.

today = datetime.now()

print(today)
print(str(today)) #this is string
print(str(today + timedelta(365)))
print(timedelta(days=365, hours=7, minutes=5, seconds=25))

#Date and time calculations with timedelta class.

print(str(today + timedelta(days=4, weeks=5)))

x = datetime.now() - timedelta(weeks=2)
y = x.strftime("%A %B %d, %Y") #for formatting we used '%'
print(y)

