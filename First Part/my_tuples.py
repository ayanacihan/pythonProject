fruits = ("grapes","apples","berries")
#for x in fruits:
#    print(x)
print(fruits[2])

animals = tuple(("lion","tiger","bear"))
print(animals)
print(len(animals))

#animals.add("dog") #this will trigger an alert. Because you can't add anything after you create a tuple.
#print(animals)

#animals[0] = "cheetah" #this will trigger an alert. Because you can't change the value after you create a tuple.
#print(animals)

del animals
print(animals) #it's already deleted, this will trigger an error