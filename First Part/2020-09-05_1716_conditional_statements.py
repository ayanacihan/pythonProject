
a = 7


b = 8

if a < b:
    print(a, "is smaller than", b)

elif a > b:
    print(a, "is bigger than", b)

else:
    print(a, "is equal to", b)

#i = 1

#while i < 7:
#    print(i)
#    i += 1

#fruits = ["grapes","berries","oranges"]
#for x in fruits:
#    print(x)

colors = ["green","yellow","purple"]
#fruits = ["grapes","berries","oranges"]

#for x in colors:
#    for y in fruits:
#        print(x,y)

i = 1

while i < 8:
    print(i)
    if i==6:
        break
    i += 1

i = 0

while i < 8:
    i += 1
    if i==4:
        continue
    print(i)

fruits = ["grapes","berries","oranges"]

for x in fruits:
    print(x)
    if x == "berries":
        break

for x in fruits:
    if x == "berries":
        continue
    print(x)

for x in range(8): #range() function creates random numbers
    print(x)

else:
    print("Loop is over. Bye!")

#for x in range(8):
#    print(x)

for x in range(2,8):
     print(x)

for x in range(2,40,4):
     print(x)