#Child class can include the same name-methods as parent class does.
#This is an example of a polymorphic method.
def addNumbers(a,b,c=1):
    return a + b + c

print(addNumbers(8,6))

print(addNumbers(8,9,4))

class UK():
    def capital_city(self):
        print("London is the capital of UK")

    def language(self):
        print("English is the primary language of UK")

class Spain():
    def capital_city(self):
        print("Madrid is the capital of Spain")

    def language(self):
        print("Spanish is the primary language of Spain")

#In above classes we had the same-name methods. This is called polymorphism.

queen = UK() #we instantiated the UK class.
queen.capital_city()

zara = Spain() #we instantiated the Spain class.
zara.capital_city()

for country in (queen,zara): #treating as tuples
    country.capital_city()
    country.language()
#this code wrote capitals and languages of UK and Spain.

