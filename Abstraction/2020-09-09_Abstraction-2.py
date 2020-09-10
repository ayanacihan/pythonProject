#Abstract Classes: contain one or more abstract methods
#Abstract classes can not be instantiated.
from abc import ABC, abstractmethod #we imported ABC

class Shape(ABC):
    @abstractmethod #abstraction
    def area(self):
        pass

    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self,side):
        self.__side = side

    def area(self):
        return self.__side * self.__side #multiply it by itself

    def perimeter(self):
        return 4 * self.__side

#myshape = Shape() #we can not instantiate the abstract class.
mysquare = Square(5) #we can not instantiate the abstract class, it gives error.
print(mysquare.area())
print(mysquare.perimeter())