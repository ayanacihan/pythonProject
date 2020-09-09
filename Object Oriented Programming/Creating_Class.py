class Instructors:
    companyName = "Bluelime" #you don't have to create a variable.

    def __init__(self,course, duration): #built-in function. It's called initializer. All classes must have init method. we added another attribute 'duration'
        self.course = course #here, the value was initialized.
        self.duration = duration


    def printinfo(self): #self parameter is the reference. you can modify methods after creating. you can add/remove them.
        print("My company name is", Instructors.companyName) #

#class Pets:
#    pass
elearning = Instructors("Python for beginners",8) #instantiating, Instance-1

bls = Instructors("Django for beginners",7) #Instance-2
bls.course = "HTML" #we modified the value
bls.printinfo()
elearning.printinfo()

print(bls.course) #we accessed the attribute 'course'
print(elearning.course)

#del bls.duration #we can delete the attribute 'duration'

print(bls.duration)
print(elearning.duration)

