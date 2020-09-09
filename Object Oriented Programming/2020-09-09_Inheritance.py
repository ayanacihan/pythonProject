class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

florist = Person("Jane","Flowers") #we instantiated an object from the class Person.
florist.printname() #we called the method of Person class.

