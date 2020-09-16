fruits = ["berries", "apples", "peaches", "oranges"]
vegetables = ["kale", "broccoli", "lettuce"]

fruits.extend(vegetables)
print(fruits)

vegetables.append("bean")
print(vegetables)

vegetables.sort()
fruits.sort()

print(vegetables, fruits)
print(vegetables)
print(fruits)

vegetables.sort(reverse=True)
print(vegetables)

print(fruits.count("berries"))

print(fruits.index("berries"))
print(fruits)
print(vegetables)

fruits.insert(0, "banana")
fruits.sort()
print(fruits)

fruits.pop()
print(fruits)

vegetables.remove("kale")
print(vegetables)

#del vegetables
#print(vegetables)