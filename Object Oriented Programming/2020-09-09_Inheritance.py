class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

florist = Person("Jane","Flowers") #we instantiated an object from the class Person.
florist.printname() #we called the print method of Person class.

class Lawyers(Person): #we inherited the parent class Person and created a child class. because we did not create an init method, it inherits all methods of parent class.
    pass

happy_lawyers = Lawyers("Jack","Smiley") #we instantiated the class Lawyers
happy_lawyers.printname() #we called the print method of Person class.