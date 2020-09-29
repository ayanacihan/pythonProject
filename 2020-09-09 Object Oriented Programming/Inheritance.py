class Person:
    def __init__(self,fname,lname): #parent class init method
        self.firstname = fname
        self.lastname = lname

    def printname(self): #parent class method
        print(self.firstname,self.lastname)

florist = Person("Jane","Flowers") #we instantiated an object from the class Person.
florist.printname() #we called the print method of Person class.

#class Lawyers(Person): #we inherited the parent class Person and created a child class. because we did not create an init method, it inherits all methods of parent class.
#    pass

class Lawyers(Person): #we inherited the parent class Person and created a child class. because we did not create an init method, it inherits all methods of parent class.
    def __init__(self, fname, lname, casetype): #we create child init method. we added 'casetype' attribute.
        Person.__init__(self,fname,lname) #we can refer the parent class.
        self.casetype = casetype

#       self.firstname = fname
#       self.lastname = lname

    def printinfo(self):
#       print(self.firstname, self.lastname)
        print("My name is",self.firstname,self.lastname) #we modified the printinfo method.
happy_lawyers = Lawyers("Jack","Smiley","criminal") #we instantiated the class Lawyers.
happy_lawyers.printinfo() #we called the print method of Person class.
happy_lawyers.printname() #we can call the parent class print method as well.
print(happy_lawyers.casetype)