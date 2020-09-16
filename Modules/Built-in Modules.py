import random #this is a built-in module
import platform

x = random.random() #we used the random() method
print(x)

y = random.randint(0, 50) #we used randint method for randomizing the integer number
print(y)

j = platform.system()
print(j)