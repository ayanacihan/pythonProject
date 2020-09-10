class Cars:
    def __init__(self,speed,color):
        self.__speed = speed #we set the value for the atribute
        self.__color = color

    def set_speed(self,value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

ford = Cars(250,"green") #create an object and instantiate
nissan = Cars(180,"black")
toyota = Cars(220,"white")

ford.set_speed(450)

ford.__speed = 750
print(ford.__speed)

#ford.set_speed(270) #there is no encapsulation, so we can call these variables.
#print(ford.get_speed()) #we can print the speed
#ford.speed = 320 #we changed the speed
#print(ford.get_speed())
#print(ford.__color) #we can not print the color. Because it's private.