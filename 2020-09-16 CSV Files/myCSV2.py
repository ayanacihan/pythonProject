#the years.csv is created after we run the code.

import csv
data = ["Month", "1958", "1959", "1960"]
x = [
["JAN", 340, 360, 417],
["FEB", 318, 342, 291],
["MAR", 400, 300, 200],
]
y = "years.csv"
with open(y, 'w') as work:
    z = csv.writer(work)
    z.writerow(data)
    z.writerows(x)
