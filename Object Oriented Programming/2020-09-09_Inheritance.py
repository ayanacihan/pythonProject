class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)

florist = Person("Jane","Flowers") #we instantiated an object from the class Person.
florist.printname() #we called the print method of Person class.

#class Lawyers(Person): #we inherited the parent class Person and created a child class. because we did not create an init method, it inherits all methods of parent class.
#    pass

class Lawyers(Person): #we inherited the parent class Person and created a child class. because we did not create an init method, it inherits all methods of parent class.
    def __init__(self, fname, lname): #we create init method.
        Person.__init__(self,fname,lname) #we can refer the parent class.
#        self.firstname = fname
#        self.lastname = lname

    def printinfo(self):
        print(self.firstname, self.lastname)

happy_lawyers = Lawyers("Jack","Smiley") #we instantiated the class Lawyers.
happy_lawyers.printinfo() #we called the print method of Person class.

happy_lawyers.printname() #we can call the parent class print method as well.