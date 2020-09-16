fruits = {"grapes","apples","berries"}
for x in fruits:
    print(x)

animals = set(("lion","tiger","bear"))
print(animals)

print(len(animals))

fruits.add("oranges")
print(fruits)

fruits.update(["mango","kiwi"])
print(fruits)

fruits.remove("kiwi")
print(fruits)

fruits.clear()
print(fruits)

del animals
print(animals)